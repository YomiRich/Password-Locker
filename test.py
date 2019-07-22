import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

     Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user =  User("Yomi","Instagram","Password")

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Yomi")
        self.assertEqual(self.new_user.account,"Instagram")
        self.assertEqual(self.new_user.password,"Password")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)
