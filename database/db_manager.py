import sqlite3
from config import DB_NAME
def get_connection():
    return sqlite3.connect(DB_NAME)
def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS roles (
        RoleID INTEGER PRIMARY KEY AUTOINCREMENT,
        RoleName TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        LastName TEXT NOT NULL,
        Name TEXT NOT NULL,
        MiddleName TEXT,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        Phone TEXT,
        Login TEXT NOT NULL,
        RoleID INTEGER,
        FOREIGN KEY (RoleID) REFERENCES roles(RoleID)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS task_status (
        StatusID INTEGER PRIMARY KEY AUTOINCREMENT,
        StatusName TEXT NOT NULL,
        UserID INTEGER,
        TaskID INTEGER,
        FOREIGN KEY (UserID) REFERENCES users(UserID),
        FOREIGN KEY (TaskID) REFERENCES tasks(TaskID)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS priorities (
        PriorityID INTEGER PRIMARY KEY AUTOINCREMENT,
        PriorityName TEXT NOT NULL,
        UserID INTEGER,
        TaskID INTEGER,
        FOREIGN KEY (UserID) REFERENCES users(UserID),
        FOREIGN KEY (TaskID) REFERENCES tasks(TaskID)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
        TaskName TEXT NOT NULL,
        UsersID INTEGER,
        CreateDate TEXT,
        Deadline TEXT,
        StatusID INTEGER,
        PriorityID INTEGER,
        FOREIGN KEY (UsersID) REFERENCES users(UserID),
        FOREIGN KEY (StatusID) REFERENCES task_status(StatusID),
        FOREIGN KEY (PriorityID) REFERENCES priorities(PriorityID)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        CommentID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        CreateDate TEXT,
        TaskID INTEGER,
        CommentText TEXT,
        FOREIGN KEY (UserID) REFERENCES users(UserID),
        FOREIGN KEY (TaskID) REFERENCES tasks(TaskID)
    )
    ''')
    conn.commit()
    conn.close()