def mean(args) -> None:
    if not args:
        print("ERROR")
        return
    print(f"mean: {sum(args) / len(args)}")


def median(args) -> None:
    if not args:
        print("ERROR")
        return
    n = len(args)
    if n % 2 == 0:
        median1 = args[n//2]
        median2 = args[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = args[n//2]
    print(f"median: {median}")


def std(args) -> None:
    if not args:
        print("ERROR")
        return
    mean = sum(args) / len(args)
    var = (sum(pow(x - mean, 2) for x in args) / len(args))
    print(f"std: {var ** 0.5}")


def var(args) -> None:
    if not args:
        print("ERROR")
        return
    mean = sum(args) / len(args)
    var = sum(pow(x - mean, 2) for x in args) / len(args)
    print(f"var: {var}")


def quartile(args) -> None:
    if not args:
        print("ERROR")
        return
    n = len(args)
    q1 = (n - 1) // 4
    q3 = (3 * n - 1) // 4
    print(f"quartile: {[args[q1], args[q3]]}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """statistics acception *args value and can in kwargs
    Mean, Median, Quartile, Standard Deviation (std) and Variance (var)"""
    try:
        if args:
            args = sorted(args)
    except Exception:
        return
    dispatch = {'mean': mean, 'median': median, 'std': std,
                'var': var, 'quartile': quartile}
    for i in list(kwargs.values()):
        try:
            dispatch[i](args)
        except Exception:
            pass
