import copy
import numpy


COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0

infinity = 1000000
weight = [
    [100, -5, 10,  5,  5, 10, -5, 100],
    [-5, -45,  1,  1,  1,  1, -45, -5],
    [10,  1,  3,  2,  2,  3,  1, 10],
    [5,  1,  2,  1,  1,  2,  1,  5],
    [5,  1,  2,  1,  1,  2,  1,  5],
    [10,  1,  3,  2,  2,  3,  1, 10],
    [-5, -45,  1,  1,  1,  1, -45, -5],
    [100, -5, 10,  5,  5, 10, -5, 100]
]
#don't change the class name
class AI(object):
 #chessboard_size, color, time_out passed from agent
 def __init__(self, chessboard_size, color, time_out):
    self.chessboard_size = chessboard_size
    #You are white or black
    self.color = color
  #the max time you should use, your algorithm's run time must not exceed the time limit.
    self.time_out = time_out
  # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
    self.candidate_list = []


 # The input is current chessboard.
 def go(self, chessboard):
 # Clear candidate_list, must do this step
    self.candidate_list.clear()
    if len(can_go(chessboard, self.color)):
        self.candidate_list = can_go(chessboard, self.color)
        place = alphabeta_search(chessboard, self.color, 5)

        self.candidate_list.remove(place)
        self.candidate_list.append(place)
 # if can_go(chessboard, 6, 4, self.color):
 #     self.candidate_list.append((6, 4))

    # print(self.candidate_list)
 #==================================================================
 #Write your algorithm here
def is_on_board(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7
# if place（x,y） turnover
def turn_over(chessboard, x ,y ,color):
    new_board = copy.deepcopy(chessboard)
    new_board[x][y] = color
    for x_direction, y_direction in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
      x_go = x + x_direction
      y_go = y + y_direction

      if not is_on_board(x_go, y_go):
           continue

      while chessboard[x_go][y_go] == -color:
          x_go += x_direction
          y_go += y_direction

          if not is_on_board(x_go, y_go):
            break

          if not is_on_board(x_go, y_go):
            continue

          if chessboard[x_go][y_go] == color:
            while True:
              x_go -= x_direction
              y_go -= y_direction
              if x_go == x and y_go == y:
                break
              new_board[x_go][y_go] = color;

    return new_board

# judge where to place
def can_go(chessboard, color):
    action_list= []
    for x in range(8):
          for y in range(8):
                if not is_on_board(x, y) or chessboard[x][y] != 0:
                  continue


                turn_over_chess = []
                for x_direction, y_direction in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                  x_go = x + x_direction
                  y_go = y + y_direction

                  if not is_on_board(x_go, y_go):
                       continue

                  while chessboard[x_go][y_go] == -color:
                      x_go += x_direction
                      y_go += y_direction

                      if not is_on_board(x_go, y_go):
                        break

                      if not is_on_board(x_go, y_go):
                        continue

                      if chessboard[x_go][y_go] == color:
                        while True:
                          x_go -= x_direction
                          y_go -= y_direction
                          if x_go == x and y_go == y:
                            break

                          turn_over_chess.append([x_go, y_go])

                if len(turn_over_chess) == 0:
                      continue
                else:
                    action_list.append((x,y))
    return action_list
def is_terminal (chessboard, player):
        if len(can_go(chessboard, player)) == 0:
            return False
        for i in range(8):
            for j in range(8):
               if chessboard[i][j] == 0:
                   return False
        return True
def step(chessboard):
    count = 0
    for x in range(8):
          for y in range(8):
              if chessboard[x][y] == 0:
                  count = count +1
    return 64-count
def chessnumber(chessboard, color):
    count = 0
    for x in range(8):
          for y in range(8):
              if chessboard[x][y] == color:
                  count = count +1
    return count

def alphabeta_search(chessboard, player,  d):

    def max_value(chessboard, player, alpha, beta, depth):
        if is_terminal(chessboard, player) or depth == 0:
            return calculate(chessboard, player)
        v = -infinity
        for a in can_go(chessboard, player):
            a_board = turn_over(chessboard, a[0], a[1], player)

            v2= min_value(a_board, -player, alpha, beta, depth-1)
            if v2 > v:
                v = v2
                alpha = max(alpha, v)
            if v >= beta:
                return v
        return v

    def min_value(chessboard, player, alpha, beta, depth):
        if is_terminal(chessboard, player) or depth == 0:
            return calculate(chessboard, -player)
        v = infinity
        for a in can_go(chessboard, player):
            a_board = turn_over(chessboard, a[0], a[1], player)
            v2 = max_value(a_board, -player, alpha, beta, depth-1)

            if v2 < v:
               v = v2
               beta = min(beta, v)
            if v <= alpha:
                return v
        return v

    if step(chessboard)>59:
        d = 64 - step(chessboard)
    elif step(chessboard)>24:
         d = 4
    else:
        d = 3

    best_score = -infinity-1
    beta = infinity
    best_action = None

    for a in can_go(chessboard, player):
        a_board = turn_over(chessboard, a[0], a[1], player)
        v = min_value(a_board, -player, best_score, beta, d-1)
        if v > best_score:
            best_score = v
            best_action = a

    return best_action


def calculate_edge(board, color):
    return  2
def calculate(board, color):

         count = 0
         for i in range(8):
             for j in range(8):
                 if color == board[i][j]:
                     count -= weight[i][j]
                 elif -color == board[i][j]:
                     count += weight[i][j]
         value = 0

         if step(board)<24:
             value = 3*count - 3*(len(can_go(board, -color)))
         elif step(board)<44:
             value = 3 * count - 7*(len(can_go(board, -color)))
         elif step(board)==64:
             if chessnumber(board, color)<32:
                 value = - infinity
             elif chessnumber(board, color)>32:
                 value = infinity
             else:
                 value = 0
         else:
             value = 3 * count -  5*(len(can_go(board, -color)))


         return value

if __name__ == '__main__':
    ai = AI(8, 1, 1000)
    my_chessboard = numpy.array(
        [  # 0  1  2  3  4  5  6  7
            [0, 0, 0, 0, 0, 0, 0, 0],  # 0
            [0, 0, 0, 0, 0, 0, 0, 0],  # 1
            [0, 0, 0, 0, 0, 0, 0, 0],  # 2
            [0, 0, 0, 1, -1, 0, 0, 0],  # 3
            [0, 0, 0, -1, 1, 0, 0, 0],  # 4
            [0, 0, 0, 0, -1, 1, -1, 0],  # 5
            [0, 0, 0, 0, 0, 0, -1, 0],  # 6
            [0, 0, 0, 0, 0, 0, -1, 0],  # 7
        ]
    )
    ai.go(my_chessboard)

 #Here is the simplest sample:Random decision
 # idx = np.where(chessboard == COLOR_NONE)
 # idx = list(zip(idx[0], idx[1]))
 #==============Find new pos========================================
 # Make sure that the position of your decision in chess board is empty.
 # If not, the system will return error.
 # Add your decision into candidate_list, Records the chess board
 # You need add all the positions which is valid
 # candiidate_list example: [(3,3),(4,4)]
 # You need append your decision at the end of the candiidate_list,
 # we will choice the last element of the candidate_list as the position you choose
 # If there is no valid position, you must return an empty list.