current_player = "X"  # текущий игрок
board = [" "] * 9  # поле

print("Добро пожаловать в игру!")

def initialize_board():
    """
    Функция, инициализирующая поле
    """
    global board
    board = [" "] * 9


def draw_board():
    """
    Функция, рисующая поле в консоль
    """
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")


def check_win():
    """
    Функция проверки победы X или 0
    """
    global board
    if (board[0] == board[1] == board[2] and board[0] != " ") or \
       (board[3] == board[4] == board[5] and board[3] != " ") or \
       (board[6] == board[7] == board[8] and board[6] != " ") or \
       (board[0] == board[3] == board[6] and board[0] != " ") or \
       (board[1] == board[4] == board[7] and board[1] != " ") or \
       (board[2] == board[5] == board[8] and board[2] != " ") or \
       (board[0] == board[4] == board[8] and board[0] != " ") or \
       (board[6] == board[4] == board[2] and board[6] != " "):
        return True
    else:
        return False


def change_player():
    """
    Функция, меняющая игрока на противоположного
    """
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_input(input_str):
    """
    Функция проверки входных значений для хода
    :param input_str: номер ячейки
    :return: корректность
    """
    if input_str.isdigit():
        if int(input_str) < 1 or int(input_str) > 9:
            print("Некорректный ввод. Введите число от 1 до 9.")
            return False
        elif board[int(input_str)-1] != " ":
            print("Эта клетка уже занята, попробуйте снова")
            return False
        else:
            return True
    else:
        print("Некорректный ввод. Введите число от 1 до 9.")
        return False


def start_game():
    """
    Основная функция приложения, которая запускает игру
    """
    initialize_board()
    draw_board()
    while not check_win():
        print("Ходит игрок", current_player)
        input_str = input("Введите номер ячейки, куда хотите поставить " + current_player + ": ")
        if check_input(input_str):
            board[int(input_str)-1] = current_player
            draw_board()
            change_player()
    print("Игрок", current_player, "выиграл!")

if __name__ == '__main__':
   start_game()

