import random
WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]
def ask_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")
def choose_mode():
    while True:
        choice = input("Play against (1) Computer or (2) Another player? ").strip()
        if choice in ("1", "2"):
            return choice == "1"
        print("Please enter 1 or 2.")
def choose_letter():
    while True:
        letter = input("Player 1, choose your letter (X or O): ").strip().upper()
        if letter in ("X", "O"):
            return letter, ("O" if letter == "X" else "X")
        print("Please enter X or O.")
def display_board(board):
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i + 3]))
        if i < 6:
            print("---+---+---")
    print()
def is_position_available(board, pos):
    return board[pos] not in ("X", "O")
def check_win(board, letter):
    return any(all(board[i] == letter for i in line) for line in WIN_LINES)
def check_draw(board):
    return all(cell in ("X", "O") for cell in board)
def get_human_move(board, name, letter):
    while True:
        move = input(f"{name} ({letter}), choose a position (1-9): ").strip()
        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Invalid input. Enter a number from 1 to 9.")
            continue
        pos = int(move) - 1
        if not is_position_available(board, pos):
            print("That position is already taken. Try again.")
            continue
        return pos
def get_computer_move(board, comp, human):
    free = [i for i in range(9) if is_position_available(board, i)]
    # smart moves: win, then block, then center, then random
    for letter in (comp, human):
        for pos in free:
            board[pos] = letter
            won = check_win(board, letter)
            board[pos] = str(pos + 1)
            if won:
                return pos
    if 4 in free:
        return 4
    return random.choice(free)
def play_game():
    vs_computer = choose_mode()
    p1, p2 = choose_letter()
    names = {p1: "Player 1", p2: "Computer" if vs_computer else "Player 2"}
    if not ask_yes_no("Do you want to start playing the game?"):
        print("Game cancelled.")
        return

    board = [str(i) for i in range(1, 10)]
    current = "X"  # X always starts
    print("\nThe board positions are numbered 1-9 as shown below.")

    while True:
        display_board(board)
        if vs_computer and names[current] == "Computer":
           human = p1
           pos = get_computer_move(board, current, human)
           print(f"Computer ({current}) chose position {pos + 1}")
        else:
           pos = get_human_move(board, names[current], current)

        board[pos] = current

        if check_win(board, current):
           display_board(board)
           print(f"Result: {names[current]} ({current}) wins!")
           break
        if check_draw(board):
            display_board(board)
            print("Result: It's a draw!")
            break
        current = "O" if current == "X" else "X"
def main():
    print("===== Tic-Tac-Toe =====")
    while True:
        play_game()
        if not ask_yes_no("Do you want to play another game?"):
            print("Thanks for playing. Goodbye!")
            break
if __name__ == "__main__":
    main()