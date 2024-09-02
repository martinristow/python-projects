def delay_function(function):
    def wrapper():
        function()
        function()
        function()
    return wrapper


@delay_function
def say_hello():
    print("Hello")

say_hello()
