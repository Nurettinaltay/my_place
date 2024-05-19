#exercise-7-1

while True:
    user_input = input('Give me a number: ')
    if user_input.isnumeric():
        number = int(user_input)
        break
    else:
        print('Try again')

total = 0
for num in range(1, number + 1):
    total += num

print(f'The total sum from 1 to {number} is {total}')

#exercise-7-2
while True:
  user_input = input('Give me a number between 1 to 10:  ') 
  if user_input.isdigit():
      number =  int(user_input)
      if  1<= number <=10:
        break
  else:
        print('Give me a number between 1 to 10:  ')
table = []
for num in range(11):
  new_number = number*num
  table.append(new_number)
print(table)

#exercise-7-3
multiple_list = []
for num in range(2950, 5210):
   if num % 13 ==0 and num % 9 == 0:
      multiple_list.append(num)
print(f'Between 2950 and 5210 multiple numbers of 13 and 9 are: {multiple_list}')

#exercise-7-4
while True:
  user_input = input('Give me a number : ')
  if user_input.isdigit():
    number = int(user_input)
    break
  else:
    print('Give me a number: ')
even = []
odd = []
for num in range(number):
  if num % 2 == 0:
    even.append(num)
  else:
    odd.append(num)
print(f'This number has {len(odd)} odd digits and {len(even)} even digits.' )

#exercise-7-5
all_letters_set = set(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'))

while True: 
 password_request = input('Create a password between 4 and 6 characters: ')
 if 4 <= len(password_request) <= 6:
    password = set(password_request)
    if all_letters_set.issuperset(password):
        request = input('Enter your password:')
        print('That is correct')
        break
    else:
        print("That does not fulfill the  letter requirements, try again")
 
 else:
   print("That does not fulfill the lenth requirements, try again")