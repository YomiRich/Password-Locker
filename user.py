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
        
