scale = 2.5

r = float(input("Write input: "))
h = int(r*2 + 10)
w = int((r*2 + 10) * scale) 

canvas = [ [' '] * w for row in range(h)]

margin_row = 5
margin_col = 5
# row_zero = int(margin_row + r)
# col_zero = int(margin_col + r)

for row in range(int(2*r) + 1):
    row_Y = row - r
    col_X = (r**2 - row_Y**2)**0.5
    col = round((col_X + r) * scale)
    canvas[row + margin_row][col + margin_col] = '-'
    col = round((r - col_X) * scale)
    canvas[row + margin_row][col + margin_col] = '-'


for row in canvas:
    print("".join(row))

