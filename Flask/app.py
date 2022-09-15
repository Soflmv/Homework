import time, random
from flask import Flask, render_template


app = Flask(__name__)


# Пузырьковая сортировка
def bubble_sort(mas):
    length = len(mas)
    count = 0

    for i in range(length):
        for j in range(0, length-i-1):
            # print(f"Сейчас сравниваем {mas[i]} и {mas[i + 1]}")
            if mas[j] > mas[j + 1]:
                count += 1
                mas[j], mas[j + 1] = mas[j + 1], mas[j]


n = 20
mas = [random.randint(1, 20) for i in range(n)]


# Вставками
def insertion_sort(lst):
    for item in range(1, len(lst)):
        current_value = lst[item]
        position = item

        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position -= 1
        lst[position] = current_value
    return lst


n = 20
lst = [random.randint(1, 20) for k in range(n)]


# Выбором
def selection_sort(obj):
    for i in range(0, len(obj)-1):
        smallest = i
        for j in range(i+1, len(obj)):
            if obj[j] < obj[smallest]:
                smallest = j
        obj[i], obj[smallest] = obj[smallest], obj[i]


n = 20
obj = [random.randint(1, 20) for m in range(n)]


# Слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


n = 20
nums = [random.randint(1, 20) for el in range(n)]


# Быстрая
def quick_sort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quick_sort(alist, start, p)
        quick_sort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


n = 20
lis = [random.randint(1, 20) for k in range(n)]


@app.route('/')
def index():
    # Сортировка пузырьком
    startTime = time.time()
    bubble_sort(mas)
    time.sleep(1)
    endTime = time.time()
    totalTime1 = (endTime - startTime).__round__(7)

    # Вставками
    startTime = time.time()
    insertion_sort(lst)
    time.sleep(1)
    endTime = time.time()
    totalTime2 = (endTime - startTime).__round__(7)

    # Выбором
    startTime = time.time()
    selection_sort(obj)
    time.sleep(1)
    endTime = time.time()
    totalTime3 = (endTime - startTime).__round__(7)

    # Слиянием
    startTime = time.time()
    merge_sort(nums)
    time.sleep(1)
    endTime = time.time()
    totalTime4 = (endTime - startTime).__round__(7)


    # Быстрая
    startTime = time.time()
    quick_sort(lis, start=0, end=20)
    time.sleep(1)
    endTime = time.time()
    totalTime5 = (endTime - startTime).__round__(7)

    return render_template('index.html',total=totalTime1, total2=totalTime2, total3=totalTime3, total4=totalTime4,
                           total5=totalTime5)


if __name__ == "__main__":
    app.run(debug=True)