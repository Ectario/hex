#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, binascii


def usage(status):
    print("Usage :\n\
        *- hex -d to decode the hexadecimal, hex to encode in hexadecimal -*\n\n\
        ~$ hex -d < textInHexa.txt\n\
        OR\n\
        ~$ echo \"7475746f0a\" | hex -d\n\
        OR\n\
        ~$ hex < textInASCII.txt\n\
        OR\n\
        ~$ echo \"tuto\" | hex\n")
    sys.exit(status)

def decode(hexa):
    if type(hexa) == hex:
        print(hexa)
        return
    try:
        bytes_object = bytes.fromhex(hexa)
        ascii_string = bytes_object.decode("utf8")
        print(ascii_string)
    except Exception as e:
        print(f'An error occurs :\n{str(e)}\n',file=sys.stderr)
        usage(2)
    exit(0)

def encode(msg : str):
    encoded = binascii.hexlify(msg.encode())
    print(encoded.decode("utf8"))



if __name__ == "__main__":
    try:
        msg = sys.stdin.read()
    except KeyboardInterrupt:
        print("\nQuit forced\n")
        usage(0)
    except Exception as e:
        print(f'An error occurs :\n{str(e)}\n',file=sys.stderr)
        usage(2)
        
    if msg == None:
        usage(2)

    if len(sys.argv) == 2:
        if sys.argv[1]=='-d':
            decode(msg)
        else:
            usage(2)
    elif len(sys.argv) == 1:
        encode(msg)
    else:
        usage(2)


    