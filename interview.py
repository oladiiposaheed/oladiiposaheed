monday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
#c = 0
S = []
#print(monday.count('GREEN'))
for i in monday:
    if (monday.count('GREEN') == 3 | monday.count('YELLOW') ==3 | monday.count('BROWN') ==3 | monday.count('BLUE') == 3 | monday.count('PINK') == 3):
        c = 1
        S.append(c)
    else:
        c = 0
        S.append(c)
s = ''.join([str(n) for n in S])
print(s)
#print(S)
