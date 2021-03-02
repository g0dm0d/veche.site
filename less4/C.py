year = int(input())
print('Школота') if year >= 0 and year <= 19 else 0
print('Скукота') if year >= 20 and year <= 59 else 0
print('Рохля') if year >= 60 and year <= 99 else 0
print('Вы в Вальхалле') if year > 99 else 0