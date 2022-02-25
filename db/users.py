import db_utils

def create_tables(sql_path):
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

def verify_password(password, user):
    """
    This function verifies the password that was
    entered

    """
    actual_password = user[3]
    return password == actual_password

def create_new_user(username, email, password):
    """
    This creates a new user in the database and makes sure that the
    username is unique

    """
    if (get_user(username) != None):
        return False
    sql_command = """
    INSERT INTO users(username, email, password, number_of_games_played, number_of_games_won, win_percentage, total_points) VALUES
    (%s, %s, %s, 0, 0, 0.0, 0);
    """
    values = [username, email, password]
    db_utils.exec_commit(sql_command, values)
    return True

def main():
    create_tables()

if (__name__ == "__main__"):
    main()