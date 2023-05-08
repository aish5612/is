#
s = "SAEKONDHWA"
D = 3

grid =[["" for i in range(len(s))] for j in range(D)]

flag = 0
row = 0

for i in range(len(s)):
    grid[row][i] = s[i]

    if row == 0:
        flag = 0
    elif row == D-1:
        flag = 1

    if flag == 0:
        row += 1
    else:
        row -= 1

for i in grid:
    for j in i:
        print(j, end= "")
