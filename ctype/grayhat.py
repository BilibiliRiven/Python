from ctypes import *
msvcrt = cdll.msvcrt
msg = "Hello world!\n"
msvcrt.printf("Testing: %s", msg)