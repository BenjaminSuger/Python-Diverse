def callLimit(limit: int):
    """decorator callLimit"""
    count = 0

    def callLimiter(function):
        """callLimiter start closure"""

        def limit_function(*args: any, **kwds: any):
            """decorator engine"""
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
            else:
                function(*args, **kwds)
        return limit_function
    return callLimiter
