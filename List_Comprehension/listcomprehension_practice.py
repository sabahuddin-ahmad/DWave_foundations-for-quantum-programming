costs = [5,10,3,4]

items = [0,1,0,1]

values = [-costs[i]*items[i] for i in range(len(costs)) if items[i]==1]

print(values)
