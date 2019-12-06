# import numpy as np
# import pandas as pd
# from tabulate import tabulate
import sys
import os

def main():
    try:
        columns, rows = os.get_terminal_size(0)
    except OSError:
        columns, rows = os.get_terminal_size(1)

    sys.stdout.write('cols:{}\nrows:{}\n'.format(columns, rows))


if __name__ == "__main__":
    main()