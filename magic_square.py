# Magic Square is that kind of square in which sum of each row, sum of each column and sum of both the diagonals is equal.
# You have to write this program that takes a nested list as input and checks whether it is a magic square or not?
magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]
i=0
while i<len(magic_square):
    j=0
    row=0
    column=0
    while j<len(magic_square):
        row=row+magic_square[i][j]
        column=column+magic_square[j][i]
        d=0
        while d<len(magic_square):
            d1=0
            d2=0
            c=0
            while c<len(magic_square):
                d1=d1+magic_square[d][c]
                d2=d2+magic_square[c][d]
                d1=d2
                c=c+1
            d=d+1
        j=j+1
    i=i+1
print("row",row)
print("column",column)
print("decimal",d1)
if row==column==d1:
    print("it is a magic square")
else:
    print("it is not a magic square")