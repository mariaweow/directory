from application.db.people import get_employees as get_employees
from application.salary import calculate_salary as calculate_salary
from datetime import datetime

if __name__ == '__main__':
    print(f'На дворе нынче: {datetime.today().strftime("%d-%m-%Y")}')
    get_employees()
    calculate_salary()