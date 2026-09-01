import os # temporaire 
import time

def ft_tqdm(lst: range) -> None:
    pass


if __name__ == "__main__":
    for percentage in range(0, 101):
        left = f"\r{percentage:>3}%|"
        right =  "| 333/333 [00:01<00:00, 177.76it/s]"
        #f"| {n}/{total} [{elapsed}<{remaining}, {rate}it/s]"
        columns = os.get_terminal_size().columns - len(left) - len(right)
        #percentage =  
        middle = columns * '██'  #int(columns * percentage / 100) * '██'
        print("\r" + left + middle + right, end='', flush=True)
        time.sleep(0.05)
    

    
