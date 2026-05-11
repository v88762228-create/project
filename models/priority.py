from database.db_manager import get_connection
class Priority:
    def __init__(self, id=None,user_id=None,task_id=None,priority_name=None):
        self.id = id
        self.user_id = user_id
        self.task_id = task_id
        self.priority_name = priority_name
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO priorities
                (UserID, TaskID, PriorityName)
                VALUES (?, ?, ?)
                ''', (
                self.user_id,
                self.task_id,
                self.priority_name))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE priorities
                SET UserID = ?,
                    TaskID = ?,
                    PriorityName = ?
                WHERE PriorityID = ?
                ''', (
                self.user_id,
                self.task_id,
                self.priority_name,
                self.id))
        conn.commit()
        conn.close()
    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM priorities WHERE PriorityID = ?",
            (self.id,))
        conn.commit()
        conn.close()
def get_all_priorities():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM priorities')
    rows = cursor.fetchall()
    conn.close()
    return [Priority(id=row[0],user_id=row[1],task_id=row[2],priority_name=row[3])for row in rows]