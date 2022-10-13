import psycopg2
from django.shortcuts import render


def main(request):
    return render(request, 'card/main.html')


def aries(request):
    try:
        connect = psycopg2.connect(
            user="postgres",
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_aries ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_leo ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_sagittarius ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_taurus ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_virgo ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_capricorn ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_gemini ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_libra ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_aquarius ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_cancer ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_scorpio ORDER BY random()")
        data = cursor.fetchmany()

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
            password="**************",
            host="127.0.0.1",
            port="5432",
            database="horoscope"
        )

        cursor = connect.cursor()
        cursor.execute("SELECT text FROM card_pisces ORDER BY random()")
        data = cursor.fetchmany()

        cursor.close()
        connect.close()
        print("Данные отправлены....")
        print("Соединение с PostgreSQL закрыто")

    except psycopg2.OperationalError as error:
        print(f'Error connect {error}!!!')

    return render(request, 'card/pisces.html', {'data': data})