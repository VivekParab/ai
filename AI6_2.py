class Layout:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('------')

    def is_valid_move(self, position):
        row, col = (position - 1) // 3, (position - 1) % 3
        return self.board[row][col] == '-'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        # Rows, columns
        for i in range(3):
            if self.board[i][0] != '-' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True  # Row win
            if self.board[0][i] != '-' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True  # Column win
        # Diagonal win
        if self.board[0][0] != '-' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != '-' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != '-' for i in range(3) for j in range(3))

    def minimax(self, player):
        if self.check_win():
            return 1 if player == 'O' else -1
        elif self.is_board_full():
            return 0

        if player == 'O':
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '-':
                        self.board[i][j] = player
                        best_score = max(best_score, self.minimax('X'))
                        self.board[i][j] = '-'
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '-':
                        self.board[i][j] = player
                        best_score = min(best_score, self.minimax('O'))
                        self.board[i][j] = '-'
            return best_score

    def find_best_move(self):
        best_score = float('-inf')
        move = -1

        for i in range(1, 10):
            if self.is_valid_move(i):
                self.board[(i - 1) // 3][(i - 1) % 3] = 'O'
                score = self.minimax('X')
                self.board[(i - 1) // 3][(i - 1) % 3] = '-'
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def computer_move(self):
        move = self.find_best_move()
        self.board[(move - 1) // 3][(move - 1) % 3] = 'O'

    def game_play(self):
        while not self.is_board_full() and not self.check_win():
            print("Player", self.current_player + "'s turn.")

            if self.current_player == 'X':
                try:
                    position = int(input("Enter a position (1-9): "))
                    if 1 <= position <= 9:
                        if self.is_valid_move(position):
                            self.board[(position - 1) // 3][(position - 1) % 3] = self.current_player
                        else:
                            print("Invalid move. Try again.")
                            continue
                    else:
                        print("Position should be between 1 and 9.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
            
            else:
                self.computer_move()

            if self.check_win():
                self.print_board()
                print("Player", self.current_player, "wins!")
                break
            elif self.is_board_full():
                print("It's a draw!")
                break
            else:
                self.switch_player()

            print("Current board:")
            self.print_board()


layout = Layout()
layout.game_play()
