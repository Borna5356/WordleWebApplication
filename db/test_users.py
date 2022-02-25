from importlib.resources import path
import unittest
import db_utils
import users

class TestChat(unittest.TestCase):

    def setUp(self):
        sql_path = "db/test_data.sql"
        users.drop_tables()
        users.create_tables(sql_path)
        
    
    def tearDown(self):
        """
        Disposes of the testing data and the tables

        """

        users.drop_tables()
    
    def test_get_user(self):
        #setup
        username = "Borneo"

        #invoke
        user = users.get_user(username)

        #analyze
        self.assertEqual(username, user[1], "get_user should have returned " + username + " but returned " + user[1])
    
    def test_verify_password_true(self):
        #setup
        username = "Borneo"
        password = "Tehran14!"
        user = users.get_user(username)
        expected = True

        #invoke
        actual = users.verify_password(password, user)

        #analyze
        self.assertEqual(expected, actual, "verify_password should have returned " + str(expected) + " but returned " + str(actual))

if (__name__ == "__main__"):
    unittest.main()