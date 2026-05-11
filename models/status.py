from database.db_manager import get_connection
class TaskStatus:
    def __init__(self, id=None,user_id=None,task_id=None,status_name=None):
        self.id = id
        self.user_id = user_id
        self.task_id = task_id
        self.status_name = status_name
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO task_status
                (UserID, TaskID, StatusName)
                VALUES (?, ?, ?)
                ''', (
                self.user_id,
                self.task_id,
                self.status_name))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE task_status
                SET UserID = ?,
                TaskID = ?,
                StatusName = ?
                WHERE StatusID = ?
                ''', (
                self.user_id,
                self.task_id,
                self.status_name,
                self.id))
        conn.commit()
        conn.close()
    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
        "DELETE FROM task_status WHERE StatusID = ?",
        (self.id,))
        conn.commit()
        conn.close()
def get_all_statuses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM task_status')
    rows = cursor.fetchall()
    conn.close()
    return [TaskStatus(id=row[0],user_id=row[1],task_id=row[2],status_name=row[3])for row in rows]