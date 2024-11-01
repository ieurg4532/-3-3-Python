b = str(input("Введіть речення: "))

words = b.split()

word = max(words, key=len)
if len(word) > 10:
    print("Найдовше слово має більше 10 символів")
else:
    print("Найдовше слово має 10 символів або менше")
