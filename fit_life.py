# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_IN_L = 1000
MIN_AGE = 18
MAX_AGE = 120
MIN_WEIGHT = 20
MAX_WEIGHT = 645
MIN_HEIGHT = 1.1
MAX_HEIGHT = 272

print("Здравствуйте!")
while True:
    user_name = input("Как Вас зовут? ").strip()
    if user_name:
        break
    print("Недопустимое значение. Попробуйте еще раз")
while True:
    user_age = input("Сколько Вам лет? ").strip()
    user_age = int(user_age)
    if MIN_AGE <= user_age <= MAX_AGE:
        break
    else:
        print("Недопустимое значение. Попробуйте еще раз")

while True:
    user_weight = input("Какой у Вас вес в кг? ")
    user_weight = float(user_weight.replace(',', '.'))
    if MIN_WEIGHT <= user_weight <= MAX_WEIGHT:
        break
    else:
        print("Недопустимое значение. Попробуйте еще раз")

while True:
    user_height = input("Какой у Вас рост в м?(например 1.74) ")
    user_height = float(user_height.replace(',', '.'))
    if MIN_HEIGHT <= user_height <= MAX_HEIGHT:
        break
    else:
        print("Введите еще раз")

bmi = round((user_weight / (user_height ** 2)), 1)
if bmi <= 16:
    bmi_classification = 'Выраженный дефицит массы тела'
elif 16 < bmi <= 18.5:
    bmi_classification = 'Недостаточная (дефицит) масса тела'
elif 18.5 < bmi <= 25:
    bmi_classification = 'Норма'
elif 25 < bmi <= 30:
    bmi_classification = 'Избыточная масса тела (предожирение)'
elif 30 < bmi <= 35:
    bmi_classification = 'Ожирение 1 степени'
elif 35 < bmi <= 40:
    bmi_classification = 'Ожирение 2 степени'
else:
    bmi_classification = 'Ожирение 3 степени'
water_ml = user_weight * WATER_PER_KG
water_l = round((water_ml / ML_IN_L), 1)
print("\n")
print("-" * 40)
print(f"Отчет для пользователя: {user_name}, {user_age} г.")
print("-" * 40)
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Интерпретация показателей ИМТ: {bmi_classification}")
print(f"Рекомендуемая норма воды: {water_l} л в день")
print("\n")
print("Расчет окончен. Будьте здоровы!")
