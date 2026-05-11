from database.db_manager import get_connection
class User:
    def __init__(self, id=None, last_name=None,name=None, middle_name=None,email=None, password=None,phone=None, login=None,role_id=None):
        self.id = id
        self.last_name = last_name
        self.name = name
        self.middle_name = middle_name
        self.email = email
        self.password = password
        self.phone = phone
        self.login = login
        self.role_id = role_id
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO users
                (LastName, Name, MiddleName,
                Email, Password, Phone,
                Login, RoleID)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                self.last_name,
                self.name,
                self.middle_name,
                self.email,
                self.password,
                self.phone,
                self.login,
                self.role_id
                ))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE users
                SET LastName = ?,
                    Name = ?,
                    MiddleName = ?,
                    Email = ?,
                    Password = ?,
                    Phone = ?,
                    Login = ?,
                    RoleID = ?
                WHERE UserID = ?
                ''', (
                self.last_name,
                self.name,
                self.middle_name,
                self.email,
                self.password,
                self.phone,
                self.login,
                self.role_id,
                self.id))
        conn.commit()
        conn.close()
    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
        "DELETE FROM users WHERE UserID = ?",
        (self.id,))
        conn.commit()
        conn.close()
def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return [User(id=row[0],last_name=row[1],name=row[2],middle_name=row[3],email=row[4],password=row[5],phone=row[6],login=row[7],role_id=row[8]) for row in rows]