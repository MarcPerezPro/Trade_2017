#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
import subprocess as sub
import os

def GetValue(marketplace):
    path = "../push_index/.index.db"
    try:
        os.mkfifo(path)
    except OSError:
        pass
    
    my_value = -1
    fifo = open(path, "r")
    
    for line in fifo:
        if (line.split(':')[0] == marketplace):
            my_value = float(line.split(':')[1])
            break
    fifo.close()
    return my_value

def main():
    #    for line in sys.stdin:        
    #       sys.stdout.write("p2:" + line)
    #print(str(GetValue('crypto')))
    #print(str(GetValue('raw_material')))
    #print(str(GetValue('forex')))
    #print(str(GetValue('stock_exchange')))

    sys.stdout.write("BUY:1:crypto\n")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write("BUY:2:raw_material\n")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write("SELL:-10000:stock_exchange\n")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write("BUY:3:forex\n")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write("SELL:1:forex\n")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write("EXIT\n")
    sys.stdout.flush()
        
if (__name__ == '__main__'):
    main()
