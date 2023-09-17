fr = open("sutaz.txt", "r", encoding="utf-8")

lines = len(fr.readlines())
print('Počet zúčastnených športovcov:', lines)

temp = ''
with open('sutaz.txt') as fp:
    for line in fp:
        g = line.split(' ')
        temp = g[1]
        break

temp = int(temp)
topMeno = ''
with open('sutaz.txt') as fp:
    for line in fp:
        x = line.split(' ')
        print('Súťažiaci '+x[0]+' dobehol do cieľa za '+x[1]+'sekúnd')
        r = int(x[1])
        if r <= temp:
            temp = r
            topMeno = x[0]
    print(topMeno,temp//60, 'min.',temp%60, 'sek.')
