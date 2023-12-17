import sys
# # num_1 = 5  # Implicit data type
# # num_2 = int(5)  # Explicit data type
# # print(num_1 + num_2)
# # print(num_1 - num_2)
# # print(num_1 * num_2)
# # print(num_1 / num_2)
# # char_1 = "jatin bansal"
# # print(char_1[-5:2:-1])

# # Sequence data types
# # String
# # List

# # List
# # Just similar to an array in another programming language
# # Enclosed with square brackets []
# numbers = [0, 1, 2, 3, 4, 5, 6, 7]
# print(type(numbers))
# print(numbers)

# # List
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(type(numbers))
# print(numbers[0:7])
# print(numbers[0:9:2])

# fruits = ["apple", "orange", "banana"]
# print(fruits[0])
# print(fruits[1:])
# # apple hatayra baki vako name aauxa

# # Using a loop in fruits
# for i in fruits:
#     print(i)

# fruits.append("pear")
# # append function le paxadi add garxa
# print(fruits)

# fruits.insert(0, "strawberry")
# # insert function le aagadi add garxa
# print(fruits)

# fruits[1] = "cherry"
# # apple hatayara arko name rakhne
# print(fruits)

# numbers = [4, 5, 6, 7, 8, 9, 3, 4, 65]
# index_of_5 = numbers.index(5)
# print(index_of_5)
# print(numbers)

# ! CREATE A LIST NAMED FRUIT AND ASSIGN 3 FRUITS 
# ! PRINT THE LIST
# ! Add 2 more fruits to the list print list

# fruits = []
# print(fruits)
# fruits.insert(0,"apple")
# print(fruits)
# # fruits.pop(2)
# print(fruits)

# concatination

# num_1=[1,5,7,8,23,]
# num_2=[12,52,71,84,43,]
# print(num_1 + num_2)

# list=[1,2,3,4,5]
# my_tupple=(1,2,3,4,5)
# print("List size:",sys.getsizeof(list))
# print("tupple size:",sys.getsizeof(my_tupple))
# print(my_tupple[0])
# print(my_tupple[0])
a = range(1,5,1)
for items in a:
    print(items)
print(type(a))
print(a)
print(items)
