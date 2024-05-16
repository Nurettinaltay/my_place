answer_1 = 36
answer_2 = 7
answer_3 = 16
question_1 = int(input('What is the answer of 6*6? : '))
if question_1 == answer_1:
  print('That is correct')
elif not question_1 == answer_1:
     print('That is false, you failed the test!')
     exit()
question_2 = int(input('What is the answer of 14/2? : '))
if question_2 == answer_2:
  print('That is also correct')
elif not question_2 == answer_2:
  print('That is false, you failed the test!')
  exit()
question_3 = int(input('What is the answer of 8+8? : '))
if question_3 == answer_3:
    print('Correct! You passed the test!')
elif not question_3 == answer_3:
  print('That is false, you failed the test!')
  exit()