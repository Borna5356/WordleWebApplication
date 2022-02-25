import unittest
import db_utils
import users

class TestChat(unittest.TestCase):

    def setUp(self):
        users.drop_tables()
        users.create_tables()
        
    
    def tearDown(self):
        """
        Disposes of the testing data and the tables

        """

        users.drop_tables()
    
    def test_login(self):
        #setup
        username = "Borneo"
        password = "Tehran14"

        #invoke
        user = users.get_user(username)

        #analyze
        self.assertEqual(username, user[1], "get_user should have returned " + username + " but returned " + user[1])

if (__name__ == "__main__"):
    unittest.main()