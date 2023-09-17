import random
# students = input('zadaj pocet studentov')
# questions = input('zadaj pocet otazok')
#
# students = int(students)
# questions = int(questions)

students = 20
questions = 20

print(students,questions)

fr = open("result.txt", "w", encoding="utf-8")
r = 0
temp = []
randomList1 = []
randomList2 = []
with open('result.txt') as fp:
    for i in range (1,students+1):
        i == str(i)
        x = str(random.randrange(1,questions+1))
        while x in randomList1:
             x = str(random.randrange(1,questions+1))
        y = str(random.randrange(1,students+1))
        while y in randomList2:
            y = str(random.randrange(1,students+1))
        res = str(i)+'. student: '+y+', otazka:'+x
        res2 = '\n'
        # fr.write(str(i)+'. student: '+y+', otazka:'+x+'\n')
        temp = res.split(':')
        if int(temp[-1]) % 2 != r % 2:
            fr.write(res+res2)
            randomList1.append(x)
            randomList2.append(y)
            r == int(x)



