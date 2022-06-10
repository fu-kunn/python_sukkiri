nums = list()
for n in range(3):
    date = int(input('{}個目の整数を入力してください>>' .format(n+1)))
    nums.append(date)
print(max(nums))    