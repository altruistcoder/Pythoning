# Following are the examples of closures in Python:

# # Example 1:
# def outer_function():
#     message = "Hii"
#     def inner_function():
#         print(message)
#     return inner_function()
#
# outer_function()


# # Example 2:
# def outer_function(msg):
#     message = msg
#     def inner_function():
#         print(message)
#     return inner_function
#
#
# hi_func = outer_function('Hii')
# bye_func = outer_function("Bye")
# hi_func()
# bye_func()
# hi_func()
# bye_func()


# Example 3:
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function


hi_func = outer_function('Hii')
bye_func = outer_function("Bye")
hi_func()
bye_func()
