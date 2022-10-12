import psycopg2
from django.shortcuts import render


def main(request):
    return render(request, 'card/main.html')


def aries(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_aries")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/aries.html', {'data': data})


def leo(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_leo")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/leo.html', {'data': data})


def sagittarius(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_sagittarius")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/sagittarius.html', {'data': data})


def taurus(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_taurus")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/taurus.html', {'data': data})


def virgo(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_virgo")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/virgo.html', {'data': data})


def capricorn(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_capricorn")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/capricorn.html', {'data': data})


def gemini(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_gemini")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/gemini.html', {'data': data})


def libra(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_libra")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/libra.html', {'data': data})


def aquarius(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_aquarius")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/aquarius.html', {'data': data})


def cancer(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_cancer")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/cancer.html', {'data': data})


def scorpio(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_scorpio")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/scorpio.html', {'data': data})


def pisces(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_pisces")
        data = cursor.fetchall()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/pisces.html', {'data': data})