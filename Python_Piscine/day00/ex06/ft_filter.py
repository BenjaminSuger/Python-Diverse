'''
def ft_filter(f, iterable):
    """this is my first version done the cleanest
    and also I think the most close to filter()"""
    if f is None:
        f = bool
    for x in iterable:
        if f(x):
            yield x
'''
'''
def ft_filter(f, iterable):
    """this is the second version with generator expression
    but the subject won't accept this as it is not list comprehension"""
    if f is None:
        f = bool
    return (x for x in iterable if f(x))
'''


def ft_filter(f, iterable):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if f is None:
        f = bool
    return [x for x in iterable if f(x)]


if __name__ == "__main__":
    print(ft_filter.__doc__)
    list1 = [1, 2, 3, 4, 1, 3, 0]
    test = ft_filter(lambda x: x < 3, list1)
    for i in test:
        print(i)
    test2 = ft_filter(None, list1)
    for i in test2:
        print(i)
