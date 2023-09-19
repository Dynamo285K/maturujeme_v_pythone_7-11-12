fr = open('sutaz.txt', 'r', encoding= 'utf-8')

lines = len(fr.readlines())
print('Počet zúčastnených športovcov:', lines)

r = 0
g = ''

with open('sutaz.txt') as fp:
    for line in fp:
        x = line.split(' ')
        print('Súťažiaci',x[0],'dobehol do cieľa za',x[1],'sekund')
        if r == 0:
            r = x[1]
            g = x[0]
        elif r > x[1]:
            r = x[1]
            g = x[0]
    r = int(r)
    print(g,r // 60, 'min.', r % 60, 'sek.')
