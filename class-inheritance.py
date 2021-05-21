"""Classes are designed to allow for more code reuse, but what if we need a class that
looks a lot like a class we already have? If the bulk of a class’s definition is useful,
but we have a new use case that is distinct from how the original class was used, we can
inherit from the original class. Think of inheritance as a remix —
it sounds a lot like the original, but there’s something… different about it."""


class User:
    is_admin = False

    def __init__(self, username):
        self.username = username


class Admin(User):
    is_admin = True


    """So this class Admin(User) is inheriting the class User"""