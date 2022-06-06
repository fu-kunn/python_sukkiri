amount = int(input('支払総額を入力してください'))
pepole= int(input('参加人数を入力してください'))

dnum = amount / pepole
pay = dnum // 100 * 100
if dnum > pay:
    pay = int(pay + 100)

payorg = amount - pay * (pepole - 1)


print('***支払総額***')
print('一人当たり{}円({}人)、幹事は{}円です' .format(pay, pepole - 1, payorg))