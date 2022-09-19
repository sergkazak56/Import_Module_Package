from application.salary import *
from application.db.people import *
import datetime
from geometry_543 import * # небольшой модуль для подсчета площади эллипса или круга. Можно дополнять своими геометрическими классами. Пакет от pypi.

# Знакомство с модулем datetime (задание 3)
def datetime_example():
    dt = datetime.datetime(2022, 9, 18)
    d = datetime.date(2009, 6, 11)
    t = datetime.time(15, 35, 0)
    day_birthday = dt.combine(d, t)
    print(f'Внучка родилась: {day_birthday}')
    day_now = dt.now()
    print(f'Сейчас: {day_now}')
    delta_years = day_now.year - day_birthday.year
    delta_months = day_now.month - day_birthday.month
    delta_days = day_now.day - day_birthday.day
    delta_sec = round((day_now - day_birthday).total_seconds() - (day_now - day_birthday).days * 24 * 60 * 60, 0)
    delta_hours = delta_sec // 3600
    delta_mins = delta_sec % 3600 // 60
    delta_secs = delta_sec % 3600 % 60
    print(f'Моей внучке сейчас: {delta_years} лет {delta_months} месяцев {delta_days} дней {int(delta_hours)}:{int(delta_mins)}:{int(delta_secs)}')
    weekday_dict = {0:'Понедельник', 1:'Вторник', 2:'Среда', 3:'Четверг', 4:'Пятница', 5:'Суббота', 6:'Воскресенье'}
    week_day = (day_now.toordinal() + 6) % 7
    print(f'Сегодня: {weekday_dict[week_day]}')
    print(f'Сегодня (ошибка см комментарий): {weekday_dict[dt.weekday()]}') # А вот метод weekday() почему-то работает неправильно


def ellipse_area(radius_small=0, radius_big=0):
    e = Ellipse(radius_small, radius_big)
    return e.calc_area()

def main():
    calculate_salary()
    get_employees()
    print()
    print('Примеры вызова функций и методов из модуля "datetime":')
    datetime_example()
    print()
    print('Пример вызова методов из модуля "geometry_543":')
    rs = float(input("Введите малый радиус эллипса (тип float): "))
    rb = float(input("Введите большой радиус эллипса (тип float): "))
    print(f'Площадь эллипса = {round(ellipse_area(rs, rb), 3)}')

if __name__ == '__main__':
    main()
