# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
#
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passengers(self, *args):
#         print(type(args))
#         for i in args:
#             self.passengers.append(i)
#
#     def print_passengers_names_self(self):
#         if self.passengers != []:
#             print(f"Names of {self.brand} passengers")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")
#
#
# vlad = Human()
# danilo = Human("danilo")
# oleg = Human("Oleg")
#
# car = Auto("BWM")
#
# car.add_passengers(vlad, danilo, oleg)
# car.print_passengers_names_self()
import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, hobby=None):
        self.name = name
        self.gladness = 50
        self.money = 100
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car
        self.hobby = hobby


    def get_hobby(self):
        self.hobby = Hobby(hobby_list)

    def het_home(self):
        self.home = House()

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def het_car(self):
        self.car = Auto(brands_of_cars)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety += 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
                return
        if manage == "fuel":
            print("I boight fuel")
            self.money -= 100
            self.car.fuel += 100
        if manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("delicious!")
            self.money += 15
            self.gladness += 10
            self.satiety += 2

    def play(self):
        if self.hobby.hobby == "Football":
            self.gladness += self.hobby.hobby_gladness
            self.money -= self.hobby.hobby_money
            self.satiety -= self.hobby.hobby_satiety
        if self.hobby.hobby == "Play computer games":
            self.gladness += self.hobby.hobby_gladness
            self.money -= self.hobby.hobby_money
        if self.hobby.hobby == "Reading books":
            self.gladness += self.hobby.hobby_gladness
            self.money -= self.hobby.hobby_money

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -=5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}`s life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "`s indexes"
        print(f"{human_indexes:-^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:-^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:-^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")
        hobby_indexes = "Hobby indexes"
        print(f"{hobby_indexes:-^50}", "\n")
        print(f"Gladness - {self.hobby.hobby_gladness}")
        print(f"Money - {self.hobby.hobby_money}")
        print(f"Satiety - {self.hobby.hobby_satiety}")



    def is_alive(self):
        if self.gladness <= 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the House")
            self.het_home()
        if self.car is None:
            self.het_car()
            print("I boought a car")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job{self.job.job} with salaty{self.job.salary}")
        if self.hobby is None:
            print("I found hobby")
            self.get_hobby()
        self.days_indexes(day)
        dice = random.randint(1,5)
        if self.satiety < 20:
            print("I will go to eat")
            self.eat()
        elif self.gladness <20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much... \nSo I will clean the house")
                self.clean_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money <0:
            print("Start working")
            self.work()
        elif self .car.strength < 15:
            print("I need to repait my car")
            self.to_repair()
        if dice == 1:
            print("let's chill")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time")
        elif dice == 4:
            print("Time for treats")
            self.shopping("delicacies")
        elif dice == 5:
            print("I found my hobby")
            self.hobby()


class Hobby:
    def __init__(self, hobby_list):
        self.hobby = random.choice(list(hobby_list))
        self.hobby_gladness = hobby_list[self.hobby]["hobby_gladness"]
        self.hobby_money = hobby_list[self.hobby]["hobby_money"]
        self.hobby_satiety = hobby_list[self.hobby]["hobby_satiety"]

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]




job_list = {"Java Developer": {"salary": 50, "gladness_less": 10},
            "Python Developer": {"salary": 70, "gladness_less": 3},
            "C++ Developer": {"salary": 45, "gladness_less": 25},
            "C# Developer": {"salary": 60, "gladness_less": 1}}

brands_of_cars = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}}

hobby_list = {
    "Football": {"hobby_gladness": 30, "hobby_money": 30, "hobby_satiety": 8},
    "Play computer games": {"hobby_gladness": 30, "hobby_money": 10, "hobby_satiety": 5},
    "Reading books": {"hobby_gladness": 10, "hobby_money": 5, "hobby_satiety": 2}}


vlad = Human("Vlad")

for day in range(1, 8):
    if vlad.live(day) == False:
        break