_user_context = {}

def set_user_context(data: dict):
    global _user_context
    _user_context.update(data)

def get_user_context():
    return _user_context

def get_value(key, default=None):
    return _user_context.get(key, default)


def getToken():
    return _user_context["token"]

def getRepo():
    return _user_context["repo"]