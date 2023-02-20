class ResultQueen():

    def show_result(self, solution):

        board = []
        for i in range(8):
            second_list = []
            for j in range(8):
                second_list.append(0)
            board.append(second_list)

        for i in range(len(solution)):
            board[i][solution[i]] = 1

        
        for line in board:
            print(line)

        return board