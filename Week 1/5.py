#Submit a solution for E-188812. Gunner.

def isPrime(dis):
    prime = True
    if dis > 1: 
        for x in range(2, dis // 2):
            if dis % x == 0:
                prime = False

        return prime
    else:
        return False            


n, f = map(int, input().split())

if (n < 500) and isPrime(n) and (f % 2 == 0): 
    print("Good job!")
else:
    print("Try next time!")

