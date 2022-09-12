from flask import Flask, render_template
import time


app = Flask(__name__)


# Пузырьковая сортировка
n = 36
mas = [3, 7, 5, 2, 8, 1, 5, 7, 5, 25, 13, 16, 23, 14, 6, 4, 3, 4, 7, 11, 9, 6, 7, 2, 1, 8, 33, 6, 3, 2, 4, 7, 8, 5, 4, 1]
count = 0

startTime = time.time()

for run in range(n - 1):
    for i in range(n - 1):
        if mas[i] > mas[i + 1]:
            count += 1
            mas[i], mas[i + 1] = mas[i + 1], mas[i]


time.sleep(1)
endTime = time.time()
totalTime1 = (endTime - startTime)


# Вставками
lst = [3, 7, 5, 2, 8, 1, 5, 7, 5, 25, 13, 16, 23, 14, 6, 4, 3, 4, 7, 11, 9, 6, 7, 2, 1, 8, 33, 6, 3, 2, 4, 7, 8, 5, 4, 1]
startTime = time.time()


def insertion_sort(lst):
    for item in range(1, len(lst)):
        current_value = lst[item]
        position = item

        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position -= 1
        lst[position] = current_value
    return lst


time.sleep(1)
endTime = time.time()
totalTime2 = (endTime - startTime)


# Выбором
lst = [3, 7, 5, 2, 8, 1, 5, 7, 5, 25, 13, 16, 23, 14, 6, 4, 3, 4, 7, 11, 9, 6, 7, 2, 1, 8, 33, 6, 3, 2, 4, 7, 8, 5, 4, 1]
startTime = time.time()

for i in range(0, len(lst)-1):
    min_index = i
    for j in range(i+1, len(lst)):
        if lst[min_index] > lst[j]:
            min_index = j
    if min_index != i:
        temp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = temp


time.sleep(1)
endTime = time.time()
totalTime3 = (endTime - startTime)


# Слиянием
startTime = time.time()


def merge_to_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s)//2
    left = merge_sort(s[:middle])
    rigth = merge_sort(s[middle:])

    return merge_to_list(left, rigth)


lst = [3, 7, 5, 2, 8, 1, 5, 7, 5, 25, 13, 16, 23, 14, 6, 4, 3, 4, 7, 11, 9, 6, 7, 2, 1, 8, 33, 6, 3, 2, 4, 7, 8, 5, 4, 1]


time.sleep(1)
endTime = time.time()
totalTime4 = (endTime - startTime)


# Быстрая
startTime = time.time()


def quick_sort(s):

    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    return quick_sort(left) + center + quick_sort(right)


lst = [3, 7, 5, 2, 8, 1, 5, 7, 5, 25, 13, 16, 23, 14, 6, 4, 3, 4, 7, 11, 9, 6, 7, 2, 1, 8, 33, 6, 3, 2, 4, 7, 8, 5, 4, 1]

time.sleep(1)
endTime = time.time()
totalTime5 = (endTime - startTime)


@app.route('/')
def index():
    return render_template('index.html', total=totalTime1, total2=totalTime2, total3=totalTime3, total4=totalTime4,
                           total5=totalTime5)


if __name__ == "__main__":
    app.run(debug=True)