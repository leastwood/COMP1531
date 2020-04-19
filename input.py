class UserInputError(Exception):
        def __init__(self, message):
            self.message = message

        def __str__(self):
            return self.message

def validate_user_name(input):
    length = len(input)
    if (length < 1 and length > 25):
        raise UserInputError("Length of username should be between 1 and 25")
    if input.find(" "):
        raise UserInputError("Username contains a space")
    return input
    
print(validate_user_name("liam"))
print(validate_user_name(""))

