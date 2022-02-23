import db_utils

def create_tables():
    sql_path = "db/wordle_db.sql"
    db_utils.exec_sql_file(sql_path)

def drop_tables():
    """
    Deletes any existing tables

    """
    conn =  db_utils.connect()
    cur = conn.cursor()
    drop_sql = """
        DROP TABLE IF EXISTS wordleStats;
        DROP TABLE IF EXISTS users;
     """
    cur.execute(drop_sql)
    conn.commit()
    conn.close()

def main():
    create_tables()

if (__name__ == "__main__"):
    main()