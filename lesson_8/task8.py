# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
#

import random

class Card():
    def __init__(self):
        self.numbers = []  # actual list of card numbers
        self.__gen_num_list()  # generates start list of card numbers
        self.card_owner_type = ""  # shows what type of player gets card object: "computer" or "human"
        self.active_numbers = 15  # shows quantity active numbers in card

    def __str__(self):
        str_0 = ' ------ Ваша карточка -----\n' if self.card_owner_type == 'human' else ' --- Карточка компьютера --\n'
        str_1 = ''
        for el in self.numbers:
            str_1 += ''.join([str(char).rjust(3) for char in el]) + '\n'
        str_3 = ' --------------------------\n'
        res_str = str_0 + str_1 + str_3
        return res_str

    def __gen_num_list(self):
        """This func generates list which includes 3 lists of 9 numbers in each list"""
        card_numbers = random.sample([i for i in range(1, 91)], 27)
        result_numbers = [sorted(card_numbers[:9]), sorted(card_numbers[9:18]), sorted(card_numbers[18:27])]
        for el in result_numbers:
            space_indx = random.sample([i for i in range(0, 8)], 4)
            for si in space_indx:
                el[si] = "   "
            self.numbers.append(el)
        return self.numbers


class Player():
    """Basic player class"""
    def __init__(self):
        self.actual_barrel = 0  # shows actual barrel number which must be checked in answer function
        self._player_type = ''  # player type: "computer" or "human"
        self.is_right_answer = 1  # if player's answer is correct - 1, if answer is wrong - 0

    def get_card(self, card):
        self.card = card
        self.card.card_owner_type = self._player_type

    def take_barrel(self, barrel_number):
        """This func gets barrel number \
         and sets this number to player's object's actual_barrel attribute"""
        self.actual_barrel = barrel_number
        return self.actual_barrel


class Human(Player):
    """Class for human players"""
    def __init__(self):
        super().__init__()
        self._player_type = 'human'

    def answer(self):
        """ Check function is a checking if there is an actual barrel in card. If player goes wrong - game is over"""
        user_answer = ''
        correct_answer = False
        while not correct_answer:
            user_answer = input("Зачеркнуть цифру? (y/n)")
            correct_answer = True if user_answer in ['n', 'y'] else False

        if user_answer == 'y':
            self.is_right_answer = 0
            for el in self.card.numbers:
                if self.actual_barrel in el:
                    el[el.index(self.actual_barrel)] = ' - '
                    self.is_right_answer = 1
                    self.card.active_numbers -= 1
        else:
            self.is_right_answer = 1
            for el in self.card.numbers:
                if self.actual_barrel in el:
                    el[el.index(self.actual_barrel)] = ' X '
                    self.is_right_answer = 0
        return self.is_right_answer


class Computer(Player):
    """Class for computer player"""
    def __init__(self):
        super().__init__()
        self._player_type = 'computer'

    def answer(self):
        """Check function is a checking if there is an actual barrel in card. Computer never goes wrong"""
        for el in self.card.numbers:
            if self.actual_barrel in el:
                el[el.index(self.actual_barrel)] = ' - '
                self.card.active_numbers -= 1
        return self.card


class Barrel_bag():
    """Class for loto bag"""
    def __init__(self):
        self.barrel_numbers = [i for i in range(1, 91)]  # generates list numbers from 1 to 90
        self.actual_barrel = 0  # barrel number which got from loto bag in this time

    def get_barrel(self):
        """This func gets random barrel number from barrel bag \
         and set this number to a player's  object's actual_barrel attribute  \
         After this barrel number is deleted from barrel bag"""
        self.actual_barrel = random.choice(self.barrel_numbers)
        self.barrel_numbers.remove(self.actual_barrel)
        return self.actual_barrel


def play_loto(pl_1, pl_2, card_1, card_2):
    """Game's logics function"""

    barrel_bag_1 = Barrel_bag()

    pl_1.get_card(card_1)
    pl_2.get_card(card_2)

    stop_game = False

    winner = ''

    while not stop_game:
        act_barrel = barrel_bag_1.get_barrel()
        print(f'Новый бочонок: {act_barrel} (осталось {len(barrel_bag_1.barrel_numbers)})')
        print(card_1)
        print(card_2)
        pl_1.take_barrel(act_barrel)
        pl_2.take_barrel(act_barrel)
        pl_1.answer()
        pl_2.answer()

        if pl_1.is_right_answer == 0:
            stop_game = True
            print('Игра окончена. Вы ошиблись и проиграли!')

        if card_1.active_numbers == 0 and card_2.active_numbers == 0:
            stop_game = True
            winner = None
            print('Игра окончена. Победила дружба!')
        elif card_1.active_numbers == 0:
            stop_game = True
            winner = pl_1._player_type
            print('Вы победили!')
        elif card_2.active_numbers == 0:
            stop_game = True
            winner = pl_2._player_type
            print('Победил компьютер!')

        print(f'у 1 игрока не закрыто {pl_1.card.active_numbers} полей')
        print(f'у 2 игрока не закрыто {pl_2.card.active_numbers} полей \n')

    print(card_1)
    print(card_2)

    return winner

card_1 = Card()
card_2 = Card()
pl_1 = Human()
pl_2 = Computer()

play_loto(pl_1, pl_2, card_1, card_2)
