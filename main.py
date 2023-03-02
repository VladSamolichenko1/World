print("Мене звати Влад")
print("Мені 12 але скоро буде 13")
print("Моє день народження 06.03")
print("Я живу в Обухові")
print("Мене звати Влад")
print("Кожен день я прокидаюсь в 7:00")

result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}

for key in data:
    res = divider(key, data(key)
    result.append(res)