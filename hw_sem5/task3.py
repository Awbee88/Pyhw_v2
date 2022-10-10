# Создайте программу для игры в ""Крестики-нолики"".

from random import randint

board = list(range(1,10))
def set_board():
    for i in range(3):
        print('-'*13)
        print(f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
    print('-'*13)

def who_first():
    rand_num = randint(1, 2)
    if rand_num == 1:
        return 1, 'Игрок 1 ходит первым(X)'
    elif rand_num == 2:
        return 2, 'Игрок 2 ходит первым(X)'

def take_input(play_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставить " + play_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Введите число: ")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = play_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False


player1 = 'Игрок 1'
player2 = 'Игрок 2'
temp = who_first()
if temp[0] == 1:
    print(temp[1])
elif temp[0] == 2:
    print(temp[1])

counter = 0
win = False
while not win:
    set_board()
    if counter % 2 == 0:
        take_input("X")
    else:
        take_input("O")
    counter += 1
    if counter > 4:
        tmp = check_win(board)
        if tmp:
            print(f'Игрок со знаком {tmp} выиграл!')
            win = True
            break
    if counter == 9:
        print("Ничья!")
        break
set_board()