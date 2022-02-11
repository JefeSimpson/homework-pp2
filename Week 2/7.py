#Submit a solution for G-Demon slayer

n = int(input())

demons = []
for i in range(n):
    name, ability = list(map(str, input().split()))
    demons.append(ability)

m = int(input())

killers = []
for i in range(m):
    name, ability, k = list(map(str, input().split()))
    k = int(k)
    killers.append(ability)
    killers.append(k)

for i in range(len(killers)):
    if type(killers[i]) is int:
        x = killers[i]
        while(x != 0): 
            if killers[i - 1] in demons: 
                demons.remove(killers[i - 1])
            else:
                break
            x -= 1

print("Demons left: " + str(len(demons)))
        




            

