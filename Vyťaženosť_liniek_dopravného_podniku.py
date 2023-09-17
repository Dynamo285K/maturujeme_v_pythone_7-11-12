fr = open('bus_vytazenost.txt', 'r', encoding='utf-8' )

file = open('bus_vytazenost.txt', 'r')
firstLine = file.readline()

kapacita = int(firstLine)

lines = len(fr.readlines())
print('pocet zastavok:',lines-1)

res = ''
temp = ''
with open('bus_vytazenost.txt',encoding='utf-8') as fp:
    next(fp)
    for line in fp:
        x = line.split(' ')
        strx = x[2::]
        for i in strx:
            temp += i + ' '
            temp = temp.replace('\n', '')
        StripTemp = temp.rstrip(' ')
        temp = ''
        res += StripTemp + ','
        result = res.rstrip(',')
    print(result)


maximum = 0
result2 = ''
onboard = 0
res2 = ''
with open('bus_vytazenost.txt',encoding='utf-8') as fp:
    next(fp)
    for line in fp:
        x = line.split(' ')
        onboard = onboard + int(x[0]) - int(x[1])
        if onboard > maximum:
            maximum = onboard
        if onboard > 50:
            # print(x[2::])
            for i in x[2::]:
                res2 += i + ' '
                result2 = res2.replace('\n',' ')
                result2 = result2.rstrip(' ')
    print('prekrocili max kapacitu:', result2)
    print('najvacsi pocet cestujucich naraz:',maximum)


