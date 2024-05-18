#exercise-6-1:Write a program that turns two sets into one dictionary.
set_1 = {1, 2, 3, 4}
set_2 = {7, 8, 9,10}
sorted_set_1 = sorted(set_1)
sorted_set_2 = sorted(set_2)
new_dic = dict(zip(sorted_set_1,sorted_set_2))
print(new_dic)



#exercise-6-2:Write a program that checks if a key is already in a dictionary. If it is not, add it
#to the dictionary with a value of “empty”.
my_dict = {"dad": "Eise", "sister_1": "Iris",
"sister_2": "Nicky"}
members = input('key=')
if members in my_dict:
    print(f'{members} is in the dictionary!')
else:
    print(f'{members} is not in the dictionary!')
    my_dict[control]=''
    print('The new dictionary is:', my_dict)

#exercise-6-3-1:
red_set = {"apple", "crab", "rose", "strawberry"}
fruits_set = {"orange", "apple", "strawberry", "grape", "kiwi", "mandarin"}
red_fruits = red_set.intersection(fruits_set)
non_red_fruits = fruits_set.difference(red_set)
print("Red fruits:", red_fruits)
print("Non-red fruits:", non_red_fruits)

#exercise-6-3-2:
red_set = {"apple", "crab", "rose", "strawberry"}
fruits_set = {"orange", "apple", "strawberry", "grape", "kiwi", "mandarin"}
orange_set = {"basketball", "fanta", "orange", "autumn leaves", "mandarin"}

red_orange_objects = red_set.union(orange_set)

red_orange_fruits = red_orange_objects.intersection(fruits_set)

non_fruits = red_orange_objects.difference(fruits_set)

print("Red and orange fruits:", red_orange_fruits)
print("Objects without fruits:", non_fruits)

#exercise-6-3-3:
red_set = {"apple", "crab", "rose", "strawberry"}
fruits_set = {"orange", "apple", "strawberry", "grape", "kiwi", "mandarin"}
orange_set = {"basketball", "fanta", "orange", "autumn leaves", "mandarin"}

all_objects = red_set.union(orange_set).union(fruits_set)

all_objects_list = list(all_objects)

print("All objects and fruits:", all_objects_list)

#exercise-6-4:Write a program that checks whether a dictionary is empty.
#Example-1
my_dict1 = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}
if not my_dict1:
    print("This dictionary is empty")
else:
    print("This dictionary is not empty")

# Example-22
my_dict2 = {}
if not my_dict2:
    print("This dictionary is empty")
else:
    print("This dictionary is not empty")

#exercise-6-5:There is a dictionary of 5 integers. Write a program that gives the same
#dictionary, but with the values in ascending order.
#Note: I have wrote this code but it did not work. But I am sure it is closed to this one:)
my_dict = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}
new_my_dict = sorted(my_dict.values())
sorted_new_dict = dict(keys= my_dict.keys(), values= new_my_dict)
print("The sorted dictionary is:", sorted_new_dict)