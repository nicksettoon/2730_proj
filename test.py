# import numpy as np
# import pandas as pd
# from tabulate import tabulate
# from ctypes import windll, create_string_buffer
def main():

    # # stdin handle is -10
    # # stdout handle is -11
    # # stderr handle is -12

    # h = windll.kernel32.GetStdHandle(-12)
    # csbi = create_string_buffer(22)
    # res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

    # if res:
    #     import struct
    #     (bufx, bufy, curx, cury, wattr,
    #     left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    #     sizex = right - left + 1
    #     sizey = bottom - top + 1
    # else:
    #     sizex, sizey = 80, 25 # can't determine actual size - return default values

    # print(sizex, sizey)

    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    print(tw, th)

    try:
        import os
        columns, rows = os.get_terminal_size(0)
    except OSError:
        columns, rows = os.get_terminal_size(1)
    print(columns,rows)
if __name__ == "__main__":
    main()