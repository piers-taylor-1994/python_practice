class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

#-----------Using positional arguments-----------#
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
            if args[0].is_logged_in == True:
                function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Piers")
new_user.is_logged_in = True
create_blog_post(new_user)

#-----------Using keyword arguments-----------#

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
            if kwargs["user"].is_logged_in == True:
                function(user=kwargs["user"])
    return wrapper

@is_authenticated_decorator
def create_blog_post(**kwargs):
    print(f"This is {kwargs["user"].name}'s new blog post.")

new_user = User("Piers")
new_user.is_logged_in = True
create_blog_post(user=new_user)