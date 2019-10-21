# A simple tic tac toe program.
#
# Expected output:
# X | O | O
# ——————————
# O | X | O
# ——————————
# . | . | X
#
# Winner is X

# This function will read a file input
def read_board(file_location):
    f = open(file_location, "r")
    data = f.readlines()
    game = []
    data_array = []
    for i in data:
        i = i[:3]
        i = i.replace(" ", ".")
        data_array.append(i)
    f.close()
    return data_array

# This function will get the winner from a board array
def winner(board):
    d = board
    this = []
    win = 0
    this.append(d[0])
    this.append(d[1])
    this.append(d[2])
    this.append(d[0][0] + d[1][0] + d[2][0])
    this.append(d[0][1] + d[1][1] + d[2][1])
    this.append(d[0][2] + d[1][2] + d[2][2])
    this.append(d[0][0] + d[1][1] + d[2][2])
    this.append(d[0][2] + d[1][1] + d[2][0])
    for i in this:
        if i == "OOO":
            win += 1
            break
        if i == "XXX":
            win += 2
            break
    if(win == 1):
        return "Winner is O"
    elif(win == 2):
        return "Winner is X"
    else:
        return "Draw"

# This function will print out the board
def show_board(data):
    board = f""
    count = 0
    for i in data:
        string_data = i.strip()
        string_data = list(i)
        board += f"{string_data[0]} | {string_data[1]} | {string_data[2]}\n"
        if count < 2:
            board += "——————————\n"
        count += 1
    return board


# This is the main function
def main():
    data = read_board("board.txt")
    board = show_board(data)
    print(board)
    win = winner(data)
    print(win)


if __name__ == "__main__":
    main()
