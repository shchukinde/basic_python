# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
# час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.
import sys

argv = sys.argv[1:]

print(f'Заработная плата: {argv[0]} * {argv[1]} + {argv[2]} = {int(argv[0]) * float(argv[1]) + float(argv[2])}')
print('Done!')

