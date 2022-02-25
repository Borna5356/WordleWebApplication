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
    
    def test_verify_password_false(self):
        #setup
        username = "Borneo"
        password = "Tehran14"
        user = users.get_user(username)
        expected = False

        #invoke
        actual = users.verify_password(password, user)

        #analyze
        self.assertEqual(expected, actual, "verify_password should have returned " + str(expected) + " but returned " + str(actual))
    
    def test_create_user_success(self):
        #setup
        username = "tester"
        email = "tester@gmail.com"
        password = "test"
        
        #invoke
        users.create_new_user(username, email, password)
        actual = users.get_user(username)

        #analyze
        self.assertEqual(username, actual[1], "create_user should have returned " + str(username) + " but returned " + str(actual[1]))

    def test_repeated_username(self):
        #setup
        username = "Borneo"
        email = "bke8431@rit.edu"
        password = "Tardis5356!!"
        expected = False

        #invoke
        actual = users.create_new_user(username, email, password)

        #analyze
        self.assertEqual(expected, actual, "create_user should have returned " + str(expected) + " but returned " + str(actual))
        
if (__name__ == "__main__"):
    unittest.main()