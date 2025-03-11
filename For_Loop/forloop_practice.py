costs = [5,10,3,4]

items = [0,1,0,1]

value = 0

for i in range(4):
    value -= (costs[i]*items[i])

print(value)
