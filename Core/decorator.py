'''
Decorator in Python :
    Decorator in python  modify or enhance functions without changing their code.
    Basically decorator is in python is a function which take another function as parameter and change its behaviour without changing the code of parameter_function
'''

def requires_admin(func):
    def wrapper(user):
        if not user.get("is_admin",False):
            raise PermissionError("Acces denied only admin can delete")
        return func(user)
    return wrapper

@requires_admin
def delete_user(user):
    return "User deleted successfully"

user1 = {"name":'Rahul',"is_admin":True}
user2 = {"name":'Roshan',"is_admin":False}

print(delete_user(user1))
try:
    print(delete_user(user2))
except PermissionError as e:
    print(e)
