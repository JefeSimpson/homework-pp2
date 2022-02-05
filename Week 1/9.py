#Submit a solution for I-189327. Dimash that's too bad.

x = int(input())

for i in range(x):
    result = ""
    mail = input()
    if mail.find("@gmail.com") != -1:
        for j in range(len(mail) - 10):
            result += mail[j]
        print(result)  

