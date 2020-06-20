def get_max(a, b):
    """
    Returns max number among a and b.
    """
    return max(a, b)

def get_max_without_arguments():
    """
    Raise TypeError exception with message as an argument.
    """
    raise TypeError('error')


def get_max_with_one_argument(a):
    """
    Returns that value.
    """
    return a


def get_max_with_many_arguments(*args):
    """
    Return the largest number among args.
    """
    return max(args)

def get_max_with_one_or_more_arguments(first, *args):
    """
    Returns the largest number among first and args.
    """
    return max(first, max(args))


def get_max_bounded(*args, low, high):
    """
    Returns the largest number among args bounded by low & high.
    """
    return max([x for x in args if low < x < high])