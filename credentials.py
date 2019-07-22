import pyperclip


class credentials:
    '''
    class to save the user class information
    '''
    credentials_list = []

    def __init__(self, name, username, password):
        self.platform_name = name
        self.user_name = username
        self.password = password
        
    def save_credentials(self):
        '''
        method to save credential to credential list
        '''
        credentials.credentials_list.append(self)
