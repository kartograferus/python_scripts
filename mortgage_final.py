print('Добро пожаловать в программу подсчета ипотек!')
print('Здесь можно подсчитать ипотеку с дополнительными платежами')
print('и того, сколько вам придется платить')
print('\n')
expected_principal = float(input('Введите стоимость квартиры: '))#вводим стоимость квартиры
first_payment = float(input('Введите первый взнос: '))#вводим первый взнос
principal = expected_principal - first_payment#считаем тело кредита, далее эту переменную юзаем для основных подсчетов
fix_principal = principal#фиксируем тело кредита для будущих подсчетов
percent_rate = float(input('Введите процентную ставку: '))#вводим процентную ставку в обычном целочисленном формате
rate = round(percent_rate / 100, 2)#преобразуем ставку в удобоваримый формат
#print(rate) #дебажил всякое
payment = float(input('Введите ежемесячный платеж: '))#вводим ежемесячный платеж
extra_payment = float(input('Введите размер дополнительных платежей: '))#вводим размер ожидаемых доп платежей
extra_start_month = int(input('Введите месяц начала допплатежей: '))#месяц когда начнем вкидывать сверх обычного
extra_end_month = int(input('Введите месяц окончания допплатежей: '))#месяц когда закончим вкидывать сверх обычного
total_extra_paid = 0.0 #всего заплачено допплатежей
total_paid = 0.0 #всего заплачено
count_month = 1 #рассчет всех месяцев
last_pay = 0.0 #последний платеж, не трогать

#тут пойдут шняги для рассчетов разницы между максималкой-ипотекой и ипотекой с допгашением
principal_max = principal#для рассчетов максималки без допов
total_max_paid = 0.0#максимально могло быть заплачено
total_delta_paid = 0.0#сэкономленная сумма процентов
count_max_month = 1#максимальное количество месяцев, если допплатежей не было бы
count_delta_month = 0#сэкономленное количество месяцев благодаря допплатежам
last_max_pay = 0.0#последний макс платеж, не трогать


#база
while principal > 0 and principal > payment:
    if (count_month >= extra_start_month and count_month <= extra_end_month):
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        total_extra_paid = total_extra_paid + extra_payment
        print (count_month, total_paid, principal, payment+extra_payment)
        count_month = count_month + 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        print(count_month, total_paid, principal, payment)
        count_month = count_month + 1

if principal < payment:
    last_pay = principal
    total_paid = total_paid + principal
    print (count_month, total_paid, principal, last_pay)

#рассчет максималки
while principal_max > 0 and principal_max > payment:
    principal_max = principal_max * (1+rate/12) - payment
    total_max_paid = total_max_paid + payment
    count_max_month = count_max_month + 1

if principal_max < payment:
    last_max_pay = principal_max
    total_max_paid = total_max_paid + principal_max

count_delta_month = count_max_month - count_month#вот и посчитали разницу месяцев
total_delta_paid = total_max_paid - total_paid#посчитали разницу процентов

#конечный вывод инфы
print('\n')
print('Поздравляем! Вы купили квартиру в ипотеку')
print('Ваш первый взнос: ', round(first_payment, 2))
print('Сумма всех выплат:', round(total_paid, 2))
print('Сумма всех выплат вместе с первоначальным взносом: ', round(total_paid + first_payment, 2))
print('Всего выплат допплатежей:', round(total_extra_paid, 2))
print('Набежавшие проценты:', round(total_paid - fix_principal, 2))
print('Переплата процентов в соотношении к долгу:', round(((total_paid - fix_principal)/fix_principal*100), 2), '%')
print('Всего месяцев придется платить:', count_month)
print('\n')
print('Благодаря допплатежам, вы сэкономили:')
print('Процентов на сумму: ', round(total_delta_paid, 2))
print('Месяцев оплаты: ', count_delta_month)