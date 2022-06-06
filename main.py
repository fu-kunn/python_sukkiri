def int_input(msg):
    return int(input('{}を入力してください>>' .format(msg)))

def calc_payment(amount, pepole=2):
    dnum = amount / pepole
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = int(pay + 100)
    payorg = amount - pay * (pepole - 1)
    return [int(pay), int(payorg)]

def show_payment(pay, payorg, pepole=2):
    print('***支払総額***')
    print('一人当たり{}円({}人)、幹事は{}円です' .format(pay, pepole - 1, payorg))

amount = int_input('支払総額'); pepole = int_input('参加人数')
[pay, payorg] = calc_payment(amount, pepole)
show_payment(pay, payorg, pepole)