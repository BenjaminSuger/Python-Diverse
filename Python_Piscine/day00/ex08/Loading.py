from os import times, get_terminal_size


def ft_tqdm(lst: range) -> None:
    """replicate tqdm function as a generator"""
    n = 0
    total = len(lst)
    start = times().elapsed
    for i in lst:
        n += 1
        percentage = n * 100 // total
        elapsed = times().elapsed - start
        if elapsed > 0:
            rate = n / elapsed
        else:
            rate = 0
        if rate > 0:
            remaining = (total - n) / rate
        else:
            remaining = 0
        left = f"\r{percentage:>3}%|"
        right = (f"| {n}/{total} "
                 f"[{int(elapsed) // 60:02d}:{int(elapsed):02d}"
                 f"<{int(remaining) // 60:02d}:{int(remaining):02d}, "
                 f"{rate:.2f}it/s]")
        columns = get_terminal_size().columns - len(left) - len(right)
        middle_square = int(columns * n / total) * '█'
        middle_empty = (columns - len(middle_square)) * ' '
        print(left + middle_square + middle_empty + right, end='', flush=True)
        yield i
