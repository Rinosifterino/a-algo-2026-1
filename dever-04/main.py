import sys
sys.setrecursionlimit(2000)

def calc(n):
    if n == 1:
        return 2
    else:
        return 2 * calc(n - 1) + (n ** 2)
    
n = int(input("me de um numero:"))

print(calc(n))