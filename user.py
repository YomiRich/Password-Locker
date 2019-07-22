class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = []  # empty user list array

    def __init__(self, username,account,password):
        self.username = username
        self.account = account
        self.password = password

        """
        __init__ method that helps us define properties for our objects.
        """
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user_method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)       
