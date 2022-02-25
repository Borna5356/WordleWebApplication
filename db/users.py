import db_utils

def create_tables():
    sql_path = "db/wordle_db.sql"
    db_utils.exec_sql_file(sql_path)

def drop_tables():
    """
    Deletes any existing tables

    """
    sql_path = "db/drop_tables.sql"
    db_utils.exec_sql_file(sql_path)

def get_user(username):
    """
    This function uses the username to get 
    the user from the table 
    """

    sql_command = "SELECT * FROM users WHERE username=%s"
    values = [username]
    return db_utils.exec_get_one(sql_command, values)

def main():
    create_tables()

if (__name__ == "__main__"):
    main()