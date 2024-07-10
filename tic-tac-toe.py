import numpy as np

#fun 1
def Show_xo(m):
    m_list = []
    internal_arry = m.flatten()
    for i in range(0, 9):
       if internal_arry[i] == "o":
           m_list.append('o')
       elif internal_arry[i] == "x":
           m_list.append('x')
       elif internal_arry[i] == " ":
           m_list.append(' ')
       else:
           return Exception("Board Error")
    
    return ("""
 {} | {} | {}
---+---+---
 {} | {} | {}
---+---+---
 {} | {} | {}
""".format(*m_list))



#fun 2
def who_won(m):

    check = [m[0].tolist(), m[1].tolist(), m[2].tolist(),
            m[:, 0].tolist(), m[:, 1].tolist(), m[:, 2].tolist(),
            np.diag(m).tolist(), np.fliplr(m).diagonal().tolist()]

    if np.any([x == ['x', 'x', 'x'] for x in check]):
        return 'x'
    elif np.any([x == ['o', 'o', 'o'] for x in check]):
        return 'o'
    else:
        return None

#fun 3
def next_move(m,player):
    while True:
        try:
            row, column = input(f"{player} turn, enter next move (x, y):").split(", ")             
            if row.isdigit() == True and column.isdigit() == True :
                row = int(row)
                column = int(column)
                if 1 <= row <=3 and 1 <= column <=3:
                    ro = row -1
                    col = column -1
                    if m[ro,col] == " ":
                        if player == "x":
                            m[ro,col] = "x"
                            break
                        if player == "o":
                            m[ro,col] = "o"
                            break
                        break
                    else:
                        print("Error: location is already taken. Please try again")
                else:
                    print("Illegal indices, must be between 1-3. Please try again")
            else: 
                print("Illegal indices, must be integers separated by a comma+space. Please try again")
        except:
            print("Illegal indices, must be integers separated by a comma+space. Please try again")


#code
m = np.array([[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]])

move = 0
who_won(m)
while who_won(m) == None and move < 9:
    next_move(m,"x")
    move += 1
    print(Show_xo(m))
    if who_won(m) == 'x' or who_won(m) == "o":
        print(f"{who_won(m)} won! Congratulations!")
        break

    if move == 9:
        print("Draw! Play again to see who is the best")
        break

    next_move(m,"o")
    print(Show_xo(m))
    move += 1
    if who_won(m) == 'x' or who_won(m) == "o":
        print(f"{who_won(m)} won! Congratulations!")
        break
