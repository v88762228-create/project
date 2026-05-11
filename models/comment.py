from database.db_manager import get_connection
class Comment:
    def __init__(self, id=None, user_id=None,create_date=None,task_id=None,comment_text=None):
        self.id = id
        self.user_id = user_id
        self.create_date = create_date
        self.task_id = task_id
        self.comment_text = comment_text
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO comments
                (UserID, CreateDate, TaskID, CommentText)
                VALUES (?, ?, ?, ?)
                ''', (
                self.user_id,
                self.create_date,
                self.task_id,
                self.comment_text))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE comments
                SET UserID = ?,
                    CreateDate = ?,
                    TaskID = ?,
                    CommentText = ?
                WHERE CommentID = ?
                ''', (
                self.user_id,
                self.create_date,
                self.task_id,
                self.comment_text,
                self.id))
        conn.commit()
        conn.close()
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM comments WHERE CommentID = ?",
                (self.id,))
            conn.commit()
            conn.close()
def get_comments_by_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT CommentID, UserID,
        CreateDate, TaskID,
        CommentText
        FROM comments
        WHERE TaskID = ?
        ''', (task_id,))
    rows = cursor.fetchall()
    conn.close()
    return [Comment(id=row[0],user_id=row[1],create_date=row[2],task_id=row[3],comment_text=row[4])for row in rows]