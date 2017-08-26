#!/usr/bin/python2
##About: This script brute forces Rot ciphers (i.e rot-13 etc)
##Usage: python brutuscaesar.py | grep -i "FLAG"

ciphertext = "%96 7=28 7@C E9:D 492= :D iQx>A6C2E@C xF=:FD r26D2C s:GFDQ]"  
size = len(ciphertext)  
for i in range(0,100):  
    result=""
    for c in ciphertext:
        if ord(c) > 126 or ord(c) < 33:
            result += c
        else:
            first = ord(c)+i
            if first > 90:
                first = 64 + (first - 90)
            result += chr(first)
    print(result)

