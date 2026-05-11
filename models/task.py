from database.db_manager import get_connection
class Task:
    def __init__(self, id=None, task_name=None, users_id=None,create_date=None, deadline=None,status_id=None, priority_id=None):
        self.id = id
        self.task_name = task_name
        self.users_id = users_id
        self.create_date = create_date
        self.deadline = deadline
        self.status_id = status_id
        self.priority_id = priority_id
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO tasks
                (TaskName, UsersID, CreateDate, Deadline, StatusID, PriorityID)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                self.task_name,
                self.users_id,
                self.create_date,
                self.deadline,
                self.status_id,
                self.priority_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE tasks
                SET TaskName = ?,
                UsersID = ?,
                CreateDate = ?,
                Deadline = ?,
                StatusID = ?,
                PriorityID = ?
                WHERE TaskID = ?
                ''', (
                self.task_name,
                self.users_id,
                self.create_date,
                self.deadline,
                self.status_id,
                self.priority_id,
                self.id))
        conn.commit()
        conn.close()
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE TaskID = ?",(self.id,))
            conn.commit()
            conn.close()
def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT TaskID, TaskName, UsersID,
        CreateDate, Deadline,
        StatusID, PriorityID
        FROM tasks
        ''')
    rows = cursor.fetchall()
    conn.close()
    return [Task(id=row[0],task_name=row[1],users_id=row[2],create_date=row[3],deadline=row[4],status_id=row[5],priority_id=row[6])for row in rows]
def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT TaskID, TaskName, UsersID,
        CreateDate, Deadline,
        StatusID, PriorityID
        FROM tasks
        WHERE TaskID = ?
        ''', (task_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Task(id=row[0],task_name=row[1],users_id=row[2],create_date=row[3], deadline=row[4],status_id=row[5],priority_id=row[6])
    return None