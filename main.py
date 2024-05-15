# Вариант 16. Посчитать количество выживших женщин по каждому классу обслуживания

import streamlit as st
import matplotlib.pyplot as plt

st.image('Титаник.jpg')
st.header('Данные пассажиров Титаника')
st.write('Просмотр данных количества выживших женщин по каждому классу обслуживания, с диапазоном платы за проезд')
price = st.slider('Диапазон платы за проезд в $ 1000', 0, 1000,  (0, 1000))
def count_survivors(filename, price):
    first_class_survived = 0
    second_class_survived = 0
    third_class_survived = 0

    with open(filename) as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            if not price[0] <= float(parts[10]) <= price[1]:
                continue
            if parts[5] == 'female' and parts[1] == '1':
                if parts[2] == '1':
                    first_class_survived += 1
                elif parts[2] == '2':
                    second_class_survived += 1
                elif parts[2] == '3':
                    third_class_survived += 1

    print("Первый класс:", first_class_survived)
    print("Второй класс:", second_class_survived)
    print("Третий класс:", third_class_survived)
    return [first_class_survived, second_class_survived, third_class_survived]
classes = ['Первый класс', 'Второй класс', 'Третий класс']
survivors = count_survivors("data.csv", price)

fig, ax = plt.subplots()
ax.bar(classes, survivors)
ax.set_xlabel('Класс')
ax.set_ylabel('Количество выживших женщин')
ax.set_title('Количество выживших женщин по классам')

st.pyplot(fig)
