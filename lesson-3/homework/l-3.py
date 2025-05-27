List = ["apple", "grape", "banana", "avacado", "cherry"]
print(List[2])

List1 = [1,2,3,4,7,10]
List2 = [2,3,4,11,9,10]
print(List1 + List2)

List = [1,2,3,8,10,13]
Listnew = List[0], List[2], List[-1]
print(Listnew)


favorite_movies = ["Catch me if you can", "The Great Gatsby", "The Wall of the street"
"The Inception", "Titanic"]
tuple = tuple(favorite_movies)
print(tuple)

cities = ["New York", "Tashkent", "Paris", "Moscow", "LA"]
if "Paris" in cities:
    print("Paris is in the cities")
else:
    print("Paris is not in the cities")
    
numbers = [1,2,4,6,7,8,10,13]
numbers1 = numbers
print (numbers1 + numbers)

numbers = [1,2,3,5,8,11]
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers[3:7])

blue = "blue"
colours = ['blue', 'orange', 'blue', 'red', 'green', 'yellow']
print(colours.count(blue))

lion = "lion"
animals = ('wolfe', 'dog', 'elephant', 'lion', 'crocodile')
print(animals.index(lion))

numbers = (1,2,3,4)
numbers1 = (1,3,4,6,7)
merged = numbers + numbers1
print(merged)

my_list = [10, 20, 30, 40, 50]
my_tuple = (1, 2, 3)

print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

numbers_tuple = (5, 10, 15, 20, 25)
numbers_list = list(numbers_tuple)

print(numbers_list)


numbers = (1,2,3,5,8,9,13)
print(max(numbers))
print(min(numbers))
words = ("apple", "banana", "cherry", "date", "fig")
reversed_words = words[::-1]

print(reversed_words)