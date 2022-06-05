numbers = [1, 1]
date = sum(numbers)
count = 2
while date <= 1000:
    numbers.append(date)
    date = date + numbers[count-1]
    count += 1
print(numbers)