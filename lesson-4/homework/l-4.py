print("1. Sort a Dictionary by Value")
d = {'apple': 10, 'banana': 5, 'orange': 7}
asc = dict(sorted(d.items(), key=lambda item: item[1]))
desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)

print("\n2. Add a Key to a Dictionary")
d = {0: 10, 1: 20}
d[2] = 30
print(d)

print("\n3. Concatenate Multiple Dictionaries")
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {}
for dic in (dic1, dic2, dic3):
    merged.update(dic)
print(merged)

print("\n4. Generate a Dictionary with Squares (1 to n)")
n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)

print("\n5. Dictionary of Squares (1 to 15)")
squares_15 = {x: x**2 for x in range(1, 16)}
print(squares_15)



print("\n1. Create a Set")
my_set = {1, 2, 3}
print(my_set)

print("\n2. Iterate Over a Set")
my_set = {10, 20, 30}
for item in my_set:
    print(item)

print("\n3. Add Member(s) to a Set")
my_set = {1, 2}
my_set.add(3)
my_set.update([4, 5])
print(my_set)

print("\n4. Remove Item(s) from a Set")
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)

print("\n5. Remove an Item if Present in the Set")
my_set = {1, 2, 3}
my_set.discard(3)
print(my_set)