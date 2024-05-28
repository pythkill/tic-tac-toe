EMPTY = " "
X = "X"
O = "O"

def draw_board(board):
    # Функция отображения доски
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


def take_input(board, player_token):
    # Функция получения пользовательского ввода
    while True:
        player_answer = input(f"Куда поставим {player_token}? ")
        if player_answer.isdigit():
            player_answer = int(player_answer)
            if 1 <= player_answer <= 9 and board[player_answer - 1] == str(player_answer):
                board[player_answer - 1] = player_token
                break
        else:
            print("Некорректный ввод. Введите число от 1 до 9, чтобы походить.")


def check_win(board):
    # Функция проверки на победителя
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for x, y, z in win_coord:
        if board[x] == board[y] == board[z] != EMPTY:
            return board[x]
    return False

def main():
    board = [str(i) for i in range(1, 10)]
    counter = 0

    for _ in range(9):
        draw_board(board)
        take_input(board, X if counter % 2 == 0 else O)
        counter += 1

        winner = check_win(board)
        if winner:
            print(f"{winner} выиграл!")
            break
    else:
        print("Ничья!")

    draw_board(board)

if __name__ == "__main__":
    main()
