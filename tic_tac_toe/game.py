from game_parts.parts import Board

from game_parts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    with open('results.txt', 'a') as f:
    f.write(result + '\n')



def main():

    game = Board()

    current_player = 'X'

    running = True
    game.display()


    while running:
        print(f'Ход делают {current_player}')



        while True:
            try:

                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
            
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                
                if game.board[row][column]  != ' ':
                    raise CellOccupiedError
            
            
            except FieldIndexError:

                print(
                    'Значение должно быть неотрицательным или меньше '
                    f'{game.field_size}'
                )
                print('Пожалуйста, введите значения строки и столбца заново.')
                continue


            except ValueError:

                print(
                    'Буквы вводить нельзя. Только числа. '
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue


            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break


        game.make_move(row, column, current_player)

        game.display()

        if game.check_win(current_player):
            result = f'Победили {current_player}'
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
            running = False

        if current_player == 'X':
            current_player = 'O'
        else: current_player = 'X'

if __name__ == '__main__':
    main()