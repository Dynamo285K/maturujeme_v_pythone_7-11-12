import random
from random import choice
import sys

fr = open('bus_vytazenost.txt', 'w', encoding='utf-8' )

students = int(input('zadaj pocet studentov'))
questions = int(input('zadaj pocet otazok'))

if students > questions:
    sys.exit('pozor studentov je viac ako otazok')

list_of_students = list(range(1,students+1))
random.shuffle(list_of_students)
# print(list_of_students)

list_of_questions = list(range(1,questions+1))
random.shuffle(list_of_questions)
# print(list_of_questions)

questions_result = [list_of_questions[0]]
for i in list_of_questions[1::]:
    indexos = list_of_questions.index(i)
    delenie = i % 2
    if questions_result[indexos-1] % 2 != delenie:
        questions_result.append(i)
    else:
        my_random_int = choice(list(set(range(1, questions+1)) - set(questions_result)))
        while my_random_int % 2 == questions_result[indexos-1] % 2:
            my_random_int = choice(list(set(range(1, questions+1)) - set(questions_result)))
        else:
            questions_result.append(my_random_int)
print('questions_result',questions_result)

with open('result.txt', 'w') as fp:
    for i in range(students):
        if i == students:
            fp.write(str(i+1)+'. student: '+str(list_of_students[i])+', otazka:'+str(questions_result[i]))
        else:
            fp.write(str(i+1)+'. student: '+str(list_of_students[i])+', otazka:'+str(questions_result[i])+'\n')
        # if i == students:
        #     fp.write(str(i+1)+'. student: '+str(list_of_students[i])+', otazka:'+str(list_of_questions[i]))
        # else:
        #     fp.write(str(i+1)+'. student: '+str(list_of_students[i])+', otazka:'+str(list_of_questions[i])+'\n')
