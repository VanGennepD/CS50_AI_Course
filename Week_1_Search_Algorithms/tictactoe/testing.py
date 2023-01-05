X = "X"
O = "O"
EMPTY = None

board = [["X", "X", EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, "X"]]
        
x_locations = []        
for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == "X":
                x_locations.append((i, j))

print(x_locations)