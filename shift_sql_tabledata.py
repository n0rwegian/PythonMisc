from passlib.context import CryptContext
# from scipy.stats import rv_discrete
# import numpy as np
from random import choice, choices, randint
import string
from faker import Faker
import datetime


ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


prices = {
    1: 10000.0,
    2: 510.0,
    3: 420.0,
    4: 650.0,
    5: 60.0,
    6: 80000.0,
    7: 150.0,
    8: 30000.0,
    9: 1000.0,
    10: 5000.0,
    11: 431.0,
    12: 600.0,
    13: 1000.0,
    14: 2300.0,
    15: 5.0,
    16: 321.0,
    17: 106.0,
    18: 333.0,
    19: 121.0,
    20: 707.0
}

products_table = {
    1: (1, '$2b$12$sjDk4HeLYo9fA6WGB7Vs1u7', 'Pink fluffy slippers'),
    2: (2, '$2b$12$CTQj74ZnjpoWHa2ByJqFy.g', 'Axe'),
    3: (3, '$2b$12$DkaQOoBRPNyKQDsLyWW0teo', 'Sausage N1'),
    4: (4, '$2b$12$bQ93UhU4WaAo7myUjo3jKe2', 'Fireworks'),
    5: (5, '$2b$12$bvuAA5pEI3lA99FSa5ab8O1', 'Bread'),
    6: (6, '$2b$12$cciAD3dWihqs202lEzkQ4.A', 'TV set'),
    7: (7, '$2b$12$ogG/2WmauDBhvCY1l1BRxu4', 'Toilet paper'),
    8: (8, '$2b$12$/2FfE4479o0Cf3Lhp.JI4Ou', 'IBM PC'),
    9: (9, '$2b$12$.C2hoX3WNSOjI1r2HH/x9ej', 'Chess set'),
    10: (10, '$2b$12$f5XXV1mw0PU7URSMR2x9reX', 'NKVD finnish knife'),
    11: (11, '$2b$12$M7PRZac2kzshqlc6RujMl.f', 'Broom'),
    12: (12, '$2b$12$jnVrkNsHMC40LRTyjdzTIu9', 'Toy sword'),
    13: (13, '$2b$12$MR79p2HucImqtGOOF72GZej', 'Wonka candy'),
    14: (14, '$2b$12$sIdo8srF8K.J90fHhf3RYe5', 'Shotgun shells (pack.)'),
    15: (15, '$2b$12$/0FO61tXZJo5P6SD.Zgvhe6', 'Plastic bag 10 kg'),
    16: (16, '$2b$12$zCPaFSJb/zWMDPp8GDTGo.L', 'Butterbeer'),
    17: (17, '$2b$12$CSE4.w5UkuZ0/Hi7YAyZJOp', 'Coca-Cola'),
    18: (18, '$2b$12$rmik8sf45nepCEwOdxNxrej', 'Vodka'),
    19: (19, '$2b$12$MZhAo4x5XuQxiJYRiiUWEO/', 'Canned food'),
    20: (20, '$2b$12$9MknAqiGEAZ29UPtNra1IuR', 'Cat food'),
    21: (21, '$2b$12$HwsAT9SGYnJGnAhaakHAben', 'Chain saw'),
    22: (22, '$2b$12$4c9lOPmdallHUj60.Qvszuj', 'K.Marks: complete set of works')
}

employees = {
    1: (1, 'Darren', 'Smith', '555-555-5555', 'sYunHfuxVT@gmail.com', 'cashier', 1),
    2: (2, 'Tracy', 'Smith', '555-555-5555', 'lbAhmgUc@gmail.com', 'programmer', 'NULL'),
    3: (3, 'Tim', 'Rownam', '(844) 693-0723', 'AHhWZj@gmail.com', 'programmer', 'NULL'),
    4: (4, 'Janice', 'Joplette', '(833) 942-4710', 'vDpR@gmail.com', 'middle manager', 'NULL'),
    5: (5, 'Gerald', 'Butters', '(844) 078-4130', 'whHtoYm@gmail.com', 'middle manager', 'NULL'),
    6: (6, 'Burton', 'Tracy', '(822) 354-9973', 'qpo@gmail.com', 'senior manager', 'NULL'),
    7: (7, 'Nancy', 'Dare', '(833) 776-4001', 'hNVa@gmail.com', 'cashier', 1),
    8: (8, 'Tim', 'Boothe', '(811) 433-2547', 'llZ@gmail.com', 'cashier', 1),
    9: (9, 'Ponder', 'Stibbons', '(833) 160-3900', 'muDzAzqUib@gmail.com', 'hr', 'NULL'),
    10: (10, 'Charles', 'Owen', '(855) 542-5251', 'Wrbfd@gmail.com', 'programmer', 'NULL'),
    11: (11, 'David', 'Jones', '(844) 536-8036', 'vbWKE@gmail.com', 'junior manager', 2),
    12: (12, 'Anne', 'Baker', '844-076-5141', 'IwxssCuZY@gmail.com', 'programmer', 'NULL'),
    13: (13, 'Jemima', 'Farrell', '(855) 016-0163', 'MwWUN@gmail.com', 'hr', 'NULL'),
    14: (14, 'Jack', 'Smith', '(822) 163-3254', 'wdlhFUWF@gmail.com', 'hr', 'NULL'),
    15: (15, 'Florence', 'Bader', '(833) 499-3527', 'jpGDVrIAk@gmail.com', 'hr', 'NULL'),
    16: (16, 'Timothy', 'Baker', '833-941-0824', 'ExgyjW@gmail.com', 'programmer', 'NULL'),
    17: (17, 'David', 'Pinker', '811 409-6734', 'xeq@gmail.com', 'cashier', 2),
    18: (18, 'Matthew', 'Genting', '(811) 972-1377', 'VlN@gmail.com', 'boss', 'NULL'),
    19: (19, 'Anna', 'Mackenzie', '(822) 661-2898', 'nXf@gmail.com', 'cashier', 2),
    20: (20, 'Joan', 'Coplin', '(822) 499-2232', 'rfsxXYZrS@gmail.com', 'junior manager', 2),
    21: (21, 'Ramnaresh', 'Sarwin', '(822) 413-1470', 'fKaeTTeTqm@gmail.com', 'hr', 'NULL'),
    22: (22, 'Douglas', 'Jones', '844 536-8036', 'xEGsGS@gmail.com', 'accountant', 'NULL'),
    23: (23, 'Henrietta', 'Rumney', '(822) 989-8876', 'lsGRdofLxw@gmail.com', 'senior accountant', 'NULL'),
    24: (24, 'David', 'Farrell', '(855) 755-9876', 'HEYZ@gmail.com', 'middle manager', 'NULL'),
    25: (25, 'Henry', 'Worthington-Smyth', '(855) 894-3758', 'atXHuvhT@gmail.com', 'cashier', 3),
    26: (26, 'Millicent', 'Purview', '(855) 941-9786', 'rhwhUmixut@gmail.com', 'middle manager', 'NULL'),
    27: (27, 'Hyacinth', 'Tupperware', '(822) 665-5327', 'KZrkRpr@gmail.com', 'cashier', 3),
    28: (28, 'John', 'Hunt', '(899) 720-6978', 'pQdulT@gmail.com', 'middle manager', 'NULL'),
    29: (29, 'Erica', 'Crumpet', '(811) 732-4816', 'CBtJU@gmail.com', 'programmer', 'NULL'),
    30: (30, 'Darren', 'Smith', '(822) 577-3541', 'KNND@gmail.com', 'senior cashier', 3),
    31: (31, 'Heather', 'Wolfe', '(913) 689-7362', 'heatherwolfe@example.net', 'store manager', 1),
    32: (32, 'Phillip', 'Brock', '(913) 319-6992', 'phillikpbrock@gmail.com', 'store manager', 2),
    33: (33, 'James', 'Myers', '(923) 400-265', 'jmyers@gmail.com', 'store manager', 3),
}


shops = {
    1: (1, 'Novosibirsk-1', 'Novosibirsk region', 'Novosibirsk', 'Krasnyi prospect, 27', 31),
    2: (2, 'Novosibirsk-2', 'Novosibirsk region', 'Novosibirsk', 'Ilyicha, 12', 32),
    3: (3, 'Tomsk-1', 'Tomsk region', 'Tomsk', 'Lenina, 42', 33),
}

discounts = {1: 0, 2: 10, 3: 20, 4: 0, 5: 40, 6: 10, 7: 30, 8: 0, 9: 50, 10: 0, 11: 0, 12: 30, 13: 30, 14: 0, 15: 0, 16: 20, 17: 20, 18: 0, 19: 0, 20: 30}
job_names = ['cashier', 'senior cashier', 'junior manager', 'middle manager', 'senior manager', 'boss', 'big boss', "big boss's boss", 'ceo', 'hr',
             'senior hr', 'programmer', 'accountant', 'senior accountant']
dates = [[1, 0, 1, 1, 1, 0, 2, 2, 1, 0, 0, 0, 1, 0, 1, 1, 2, 2, 0, 2, 3, 1, 1, 1, 0, 1, 1, 1, 1, 2, 3], [2, 1, 2, 1, 4, 2, 2, 0, 0, 1, 1, 2, 3, 2, 1, 0, 3, 2, 1, 0, 1, 2, 0, 1, 1, 0, 1, 0, 0], [1, 1, 0, 1, 1, 3, 1, 1, 2, 1, 0, 0, 0, 1, 1, 1, 0, 1, 3, 1, 0, 1, 0, 1, 1, 1, 2, 0, 1, 2, 2]]
# cashiers = [v[0] for v in employees.values() if v[5] in ('cashier', 'senior cashier')]
cashiers = [1, 7, 8, 17, 19, 25, 27, 30]



def generate_data_for_products() -> None:
    names = {'Cat food', 'Shotgun shells (pack.)', 'Bread', 'Vodka', 'Toilet paper', 'Sausage N1', 'Canned food',
             'Coca-Cola', 'TV set', 'IBM PC', 'Chess set', 'Axe', 'Butterbeer', 'Fireworks', 'Pink fluffy slippers',
             'Broom', 'Wonka candy', 'Toy sword', 'NKVD finnish knife', 'Plastic bag 10 kg'}

    for index, name in enumerate(names, 1):
        print(f"({index}, '{pwd_context.hash(name)[:30]}', '{name}'),")


def generate_data_for_discounts() -> None:
    product_discounts = {}
    for i in range(20):
        for product in products_table:
            product_discounts[product] = choices([0, 10, 20, 30, 40, 50, 75, 100],
                                                 weights=[0.6, 0.05, 0.15, 0.09, 0.05, 0.03, 0.02, 0.01])
    print(product_discounts)


def generate_data_for_purchase_receipts() -> None:
    with open('purchase_receipts.txt.txt', 'w', encoding='utf-8') as f_out:
        for i in range(101, 131):
            number_of_purchases = choices(range(1, 11), weights=[0.05, 0.1, 0.15, 0.2, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05])
            for j in range(1, int(*number_of_purchases) + 1):
                f_out.write(f'({i}, {j}, {(x := randint(1, 20))}, {(y := randint(1, 10))}, {prices[x] * y}, {discounts[x]}),\n')


def random_char(char_num):
    return ''.join(choice(string.ascii_letters) for _ in range(char_num))


def generate_employees_table() -> None:
    with (open('file.txt', 'r') as f_in):
        data = f_in.readlines()
        employees = {}
        for i in range(1, len(data)):
            row = data[i].split(', ')
            employees[i] = i, row[2].strip("'"), row[1].strip("'"), row[-3].strip("'"), \
                random_char(randint(3, 10)) + "@gmail.com", \
                (x := job_names[int(*choices(range(14), \
                        weights=[0.2, 0.1, 0.1, 0.1, 0.1, 0.03, 0.02, 0.01, 0.01, 0.1, 0.02, 0.12, 0.07, 0.02]))]), \
                randint(1, 30) if x in ('cashier', 'senior cashier', 'junior manager') else 'NULL'


def generate_dates_of_purchases():
    dates = [[0] * 31, [0] * 29, [0] * 31]

    for _ in range(100):
        dates[(x := randint(0, 2))][randint(0, len(dates[x]) - 1)] += 1


def generate_datetimes_with_faker():
    fake = Faker()
    fk_dates = [fake.date_time_between_dates(datetime.date(2024, 4, 1), datetime.date(2024, 5, 1)) for _ in range(30)]
    with open('datetimes1.txt', 'w') as f_out:
        print(*(str(i) for i in sorted(fk_dates)), sep='\n', file=f_out)


def generate_purchases():
    with open('datetimes.txt', 'r') as f_datatimes, open('purchase_receipts.txt', 'r') as f_receipts:
        datetimes = f_datatimes.readlines()
        receipts = f_receipts.readlines()
    with open('purchases1.txt', 'w') as f_out:
        purchase_id = 1
        amount = 0
        cashiers_weights = [0.8 / len(cashiers)] * len(cashiers)
        cashiers.append('NULL')
        cashiers_weights.append(0.2)
        for row in receipts:
            row = tuple(row.strip()[1:-2].split(', '))
            if int(row[0]) == purchase_id:
                # print(row, '\t', row[5], float(row[4]) * (100 - int(row[5])) / 100)
                # print(float(row[4]) if int(row[5]) else float(row[4]) * (100 - int(row[5])) / 100)
                print(row, amount, float(row[4]) * (100 - int(row[5])) / 100, round(float(row[4]) * (100 - int(row[5])) / 100, 2))
                amount += float(row[4]) if not int(row[5]) else float(row[4]) * (100 - int(row[5])) / 100
            else:
                seller_id = choices(cashiers, cashiers_weights)
                print(f"({purchase_id}, '{datetimes[purchase_id - 1].strip()}', {round(amount, 2)}, {seller_id[0]}),", file=f_out)
                purchase_id = int(row[0])
                amount = float(row[4]) if not int(row[5]) else float(row[4]) * (100 - int(row[5])) / 100
        seller_id = choices(cashiers, cashiers_weights)
        print(f"({purchase_id}, '{datetimes[purchase_id - 1].strip()}', {amount}, {seller_id[0]}),", file=f_out)


def generate_cashier_with_faker(quantity):
    fake = Faker()
    for i in range(quantity):
        name = fake.first_name()
        last_name = fake.last_name()
        phone_number = fake.phone_number()
        email = fake.email()
        print(f"({i}, '{name}', '{last_name}', '{phone_number}', '{email}', 'cashier', 1)")

# generate_purchases()



