def check_type(func):
    def wrapper(*args, **kwargs):
        values = list(args) + list(kwargs.values())
        if not values:
            return func(*args, **kwargs)
        first_type = type(values[0])
        for value in values:
            if type(value) is not first_type:
                return "Аргументи мають бути одного типу"   
        return func(*args, **kwargs)
    return wrapper
