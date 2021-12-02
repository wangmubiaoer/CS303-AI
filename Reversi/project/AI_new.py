import numpy as np
import random
import time

#don't change the class name
class AI(object):
  COLOR_BLACK=-1
  COLOR_WHITE=1
  COLOR_NONE=0
  random.seed(0)

  weight = [
      [70, -20, 20, 20, 20, 20, -15, 70],
      [-20, -30, 5, 5, 5, 5, -30, -15],
      [20, 5, 1, 1, 1, 1, 5, 20],
      [20, 5, 1, 1, 1, 1, 5, 20],
      [20, 5, 1, 1, 1, 1, 5, 20],
      [20, 5, 1, 1, 1, 1, 5, 20],
      [-20, -30, 5, 5, 5, 5, -30, -15],
      [70, -15, 20, 20, 20, 20, -15, 70]
  ]

  #chessboard_size, color, time_out passed from agent
  def __init__(self, chessboard_size, color, time_out):
    self.chessboard_size = chessboard_size
    #You are white or black
    self.color = color
  #the max time you should use, your algorithm's run time must not exceed the time limit.
    self.time_out = time_out
  # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
    self.candidate_list = []

  def is_on_board(x,y):
     return x >= 0 and x <= 7 and y >= 0 and y <= 7


  def can_go(self,chessboard,x,y,color):
     if not self.is_on_board(x, y) or chessboard[x][y] != 0:
         return False

     op_color = 1 if color == -1 else -1
     turn_over_chess = []
     for x_direction,y_direction in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
         x_go = x + x_direction
         y_go = y + y_direction

         if not self.is_on_board(x_go, y_go):
             continue

         while chessboard[x_go][y_go] == op_color:
             x_go += x_direction
             y_go += y_direction

             if not self.is_on_board(x_go, y_go):
                  break

         if not self.is_on_board(x_go, y_go):
             continue

         if chessboard[x_go][y_go] == self.color:
              while True:
                  x_go -= x_direction
                  y_go -= y_direction
                  if x_go == x and y_go == y:
                      break
                  chessboard[x_go][y_go] = color
                  turn_over_chess.append([x_go, y_go])

     if len(turn_over_chess) == 0:
             return False

     return chessboard

  def calculate(self, color, board):
         if color == 1:
             OPcolor = -1
         else:
             OPcolor = 1

         count = 0
         for i in range(8):
             for j in range(8):
                 if color == board[i][j]:
                     count -= self.weight[i][j]
                 elif OPcolor == board[i][j]:
                     count += self.weight[i][j]
         return count

  def alphaBeta(self, board, color, a, b, depth):
      # 递归终止
      if depth == 0:
          return None, self.calculate(board, self, color)



      action_list = []
      for i in range(8):
          for j in range(8):
              if self.can_go(self, board, i, j, color):
                  action_list.append((i, j))


      if len(action_list) == 0:
          op_action_list = []
          for i in range(8):
              for j in range(8):
                  if self.can_go(self, board, i, j, -color):
                      op_action_list.append((i, j))
          if len(op_action_list) == 0:
              return None, self.calculate(self, board, color)
          return self.alphaBeta(board, -color, a, b)
      if color == self.color:

         for p in action_list:

            flipped_board = self.can_go(board, p[0], p[1], color)
            p1, current = self.alphaBeta(flipped_board, -color, a, b, depth-1)

            if current > a:
                a = current
                if a >= b:
                      break

         return p, a

      else:

          for p in action_list:

              flipped_board = self.can_go(board, p[0], p[1], color)
              p1, current = self.alphaBeta(flipped_board, -color, a, b, depth - 1)

              if current < b:
                 b = current
                 if b<= a:
                      break
          return p, b









  # The input is current chessboard.
  def go(self, chessboard):
  # Clear candidate_list, must do this step
    self.candidate_list.clear()
    self.candidate_list = []
 #==================================================================
 #Write your algorithm here
    t = time.time()

    for i in range(8):
      for j in range (8):
         if self.can_go(self, chessboard, i, j, self.color):
               self.candidate_list.append((i, j))
    if len(self.candidate_list)!= 0:
       place, weight = self.alphaBeta(self, chessboard, self.color, -99999, 99999, 1)

       self.candidate_list.remove(place)
       self.candidate_list.append(place)









#==============Find new pos========================================
 # Make sure that the position of your decision in chess board is empty.
 # If not, the system will return error.
 # Add your decision into candidate_list, Records the chess board
 # You need add all the positions which is valid
 # candiidate_list example: [(3,3),(4,4)]
 # You need append your decision at the end of the candiidate_list,
 # we will choice the last element of the candidate_list as the position you choose
 # If there is no valid position, you must return an empty list.
