weight = int(input("体重(kg)を入力"))
height = float(input("身長(m)を入力"))

bmi = weight / height / height
print("BMIは{}です".format(bmi))