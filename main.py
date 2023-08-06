import random

print("Гра почалась")

first_list = ["вода", "чай", "печиво", "футбол", "ультрас"]
question = random.choice(first_list)  # метод обирає рандомне слово

word = question  # змінна яка зберігає слово

attempt = int(input("Скільки ви хочете отримати спроб для розвязання:>"))

stars = []
for i in range(len(word)):
    stars.append("*")  # приймаж answer і робить з нього ******* в змінній stars
print(stars)

n = 1
win = False
while not win:
    answer = str(input("Введіть букву або слово:> "))
    if len(answer) > 0:
        for a in answer:
            if answer == stars:
                win = True
                print("Ви перемогли!")
        else:
            print("Ви помилились(")
    if n == attempt:
        print("Спроби закінчились")
        break
    elif n <= attempt:
        n += 1
        print("Спробуйте ще) ")

    for i in range(len(question)):
        if answer == question[i]:
            stars[i] = answer
    print(stars)
