#!/bin/python

N = int(raw_input())

if(N % 2 != 0):
    print("Weird")
if(N % 2 == 0 and N in range(2, 6)):
    print("Not Weird")
if(N % 2 == 0 and N in range(6, 21)):
    print("Weird")
if(N % 2 == 0 and N > 20):
    print("Not Weird")
