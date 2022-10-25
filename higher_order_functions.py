def add_tw0_nums(x, y):  # normal function which returns data
    return x + y


def add_three_nums(x, y, z):  # normal function which returns data
    return x + y + z


def get_appropriate_function(num_len):  # function which returns functions depending on the logic
    if num_len == 3:
        return add_three_nums
    else:
        return add_tw0_nums


if __name__ == "__main__":
    args = [1, 2, 3]
    num_len = len(args)
    res_function = get_appropriate_function(num_len)
    print(res_function)       # <function add_three_nums at 0x7f8f34173668>
    print(res_function(*args))  # unpack the args, output 6

    args = [1, 2]
    num_len = len(args)
    res_function = get_appropriate_function(num_len)
    print(res_function)       # <function add_tw0_nums at 0x7f1630955e18>
    print(res_function(*args))  # unpack the args, output 3
