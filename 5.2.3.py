import itertools
money= [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
ways= itertools.combinations(money, 7)
count=0
for way in ways:
    if sum(way)==100:
        count+=1
print(count)