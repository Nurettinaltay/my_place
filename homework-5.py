#exercises-5-1
my_lst = [1, 2, 3, 4, 5, 6]

number_to_remove = [0, 2, 3]
new_lst = []

for number in range(len(my_lst)):
    if number not in number_to_remove:
        new_lst.append(my_lst[number])

print("The new list is:", new_lst)

#exercises-5-2
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
new_tuple = tuple_1 + tuple_2
print("The new tuple is:", new_tuple)

#exercises-5-3
my_list1 = [6, 2, 7, 4, 3, 'd', 'hello', 'x']
tuple_1 = tuple(my_list1[:len(my_list1)//2])
tuple_2 = tuple(my_list1[len(my_list1)//2:])

print("Tuple 1 is:", tuple_1)
print("Tuple 2 is:", tuple_2)

#exercises-5-4
# I tried to write this code with sort() but could not make the conclusion

#exercises-5-5-1
my_list = [2, 2, 3, 3, 4]

average = sum(my_list) / len(my_list)

print("The average is:", average)

#exercises-5-5-2
my_list = [2, 2, 3, 3, 4,]

average = sum(my_list) / len(my_list)
print("First average is:", average)
number_added= 5 * (len(my_list) + 1) - sum(my_list)
print('Number to added', number_added)

my_list.append(number_added)
print("Added", number_added, ", new list is", my_list)
new_average= sum(my_list) / len(my_list)
print("The average is now: ", new_average)

#exercises-5-6
# Sorry I could not understand the question:)