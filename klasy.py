class Car:  
#Taki zapis oznaczał wywołanie wbudowanej funkcji, konstruktora klasy Car. Konstruktor to specjalna funkcja, 
#której zadaniem jest tworzenie nowych instancji klasy.
    def __init__ (self, made, model_name, top_speed, color):
        self.made = made
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
        self._current_speed = 0
    #METODA REPR dla admina - pozwala zobaczyć cały bebech funkcji wraz z parametrami i argumentami
    def __repr__(self):
        return f"Car(make={self.made} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
    def __eq__(self, other):
        return any (
            (self.made == other.made,
            self.model_name == other.model_name,
            self.top_speed == other.top_speed,
            self.color == other.color)
        )
    # return all - zwraca True, jeśli wszystkie wartości do niej przekazane również są prawdziwe. W przeciwnym przypadku zwróci False.
    # return all - metoda all() przyjmuje zmienną, po której można iterować, czyli np. krotkę lub listę.
    # return any - zwróci True, jeśli którykolwiek z przekazanych argumentów będzie prawdą.
    def __gt__(self, other):
        return self.top_speed > other.top_speed
    

my_car = Car(made="Ford", model_name = "Mustang", top_speed = 250, color = "Yellow")
print(my_car.color)

car_one = Car(made="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(made="Ford", model_name="Mustang", top_speed=250, color="Red")
print(car_one == car_two)

car_one = Car(made="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(made="Ford", model_name="Mustang", top_speed=350, color="Red")
car_three = Car(made="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]
print(car_two > car_one)
by_speed = sorted(cars, key=lambda car: car.top_speed)
#WYRAŻENIE LAMBDA konstrukcja (w przypadku gdy potrzebujemy zbudować funkcję, która jest potrzebna tylko w określonych przypadkach, np. jako parametr do funkcji sortującej)
#def get_made(car):
#    return car.made
# równoważne: lambda car: car.make
by_made = sorted(cars, key=lambda car: car.made)
print(by_speed)
print(by_made)

print("---------------CARS END-------------------")

class Personality:
    def __init__ (self, name, surname, company, email, datalenght=0):
        self.name = name
        self.surname = surname
        self.company = company
        self.email = email
        self._datalenght = datalenght
       
    # METODA STR NA PRZEKAZANIE CAŁEJ ZAWARTOŚCI INSTANCJI JEDNĄ FUNKCJĄ BEZ ODNOSZENIA SIĘ DO POSZCZEGÓLNYCH PARAMETRÓW
    def __str__ (self):
        return f"{self.name}, {self.surname}, {self.company}, {self.email}"
    def __repr__(self):
        return f"Personality(name={self.name}, surname={self.surname}, company={self.company}, email={self.email})"
    def contactmethod (self):
        return f"Kontaktuje się z {self.name}, {self.surname}, z firmy {self.company}"
    def datalenghtis(self):
        return self.datalenght 
    @property
    def datalenght(self):
        print("Getting value ...")
        return self._datalenght
    @datalenght.setter
    def datalenght(self, value):
        print("Setting lenght:")
        self._datalenght == value
        value == len({self.surname})+ len({self.name})+1
    
#Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: 
# pierwsza (BaseContact) powinna przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. 
# Za pomocą kolejnej klasy (BusinessContact) rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby 
# – stanowisko, nazwa firmy, telefon służbowy.
class BaseContact (Personality):
    def __init__ (self, name, surname, company, email):
        super().__init__(name, surname, company, email)
    def contactmethod2 (self):  
        print(f"Piszę emaila na adres prywatny lub dzwonię na telefon służbowy:", {self.name}, {self.surname}, ":", {self.email}, "z firmy", {self.company})

class BusinessContact (Personality):
    def __init__ (self, position, phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.phone = phone
    def contactmethod3(self, name, surname, position):
        print(f"Kontaktuje się z", {self.name}, " ", {self.surname}, "-", {self.position})
    def labellenght (self, name, surname):
        return len(self.name) + len(self.surname) +1
        
class Class:
    def boundMethod(instance,param1):
        print("I'm a method bound to Class. Here is my Class's Reference:", instance,'Parameter:',param1)
instance = Class()
instance.boundMethod("any") # same as Class.boundMethod(instance,10)

print("---- DZIEDZICZENIE TESTY -----")
basecontact1 = BaseContact(name = "Tomasz", surname = "Chciałaś", company = "Forex", email = "chciałaś@tomasz.pl")
businesscontact1 = BusinessContact(name = "Grzegorz", surname = "Właściwy", company = "Enea", email = "grzegorz@wlasciwy.pl", position = "CEO", phone="666")
print(basecontact1)
print(businesscontact1)
#nie drkuje position i phone - why ?
print(basecontact1.contactmethod2)
print(businesscontact1.contactmethod3)
print(businesscontact1.labellenght)

#----INSTANCJE KLASY-----
businesscard1 = Personality(name = "Monika", surname = "Akinom", company = "Orbico", email ="monika@akinom.pl", datalenght=0)
businesscard2 = Personality(name="Anna", surname = "Akinom", company = "Axis", email = "anna@axis.pl", datalenght=0)
businesscard3 = Personality(name = "Kamil", surname = "Limak", company = "Bigo", email = "kamil@bigo.pl", datalenght=30)
businesscard4 = Personality(name = "Jacek", surname = "Kecaj", company = "Projekt", email="jacek@kecaj.pl", datalenght=0)
businesscard5 = Personality(name="Julia", surname = "Limak", company="Axis", email="julia@axis.pl", datalenght=0)
print("----LISTA WIZYTÓWEK---")
my_contacts = [businesscard1, businesscard2, businesscard3, businesscard4, businesscard5]
for contact in my_contacts:
    print(contact)

print("------SORTOWANIE DANYCH Z WIZYTÓWEK---------------")
by_name = sorted(my_contacts,  key=lambda Personality: Personality.name)
print(by_name)

by_surname = sorted(my_contacts, key=lambda Personality: Personality.surname)
print(by_surname)
print("---------------SORTING ENDS------------------")
# FUNKCJE SORTOWANIA ZADZIAŁY Z REPR A NIE ZADZIAŁAŁY Z METODĄ STR - DLACZEGO ?
print("---------------INFORMACJA O KONTAKCIE--------")
for i in my_contacts:
    print(i.contactmethod())

print("---------------LICZBA LITER OBLICZANIE ZWYKŁĄ FUNKCJĄ------------------")
for i in my_contacts:
    print(len(i.name)+len(i.surname)+1)

print("---------------LICZBA LITER OBLICZANA FUNKCJĄ W CIELE KLASY-----------------")
result1=businesscard1.datalenghtis()
print(result1)



print("---------------FAKEPEOPLE EXCERSISES------------------")
#Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. 
# Niech ta funkcja przyjmuje dwa parametry: 
# rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.
class FakePeople:
    def __init__ (self, namee, address):
        self.namee = namee
        self.address = address
    def __str__(self):
        return f'{self.namee}, {self.address}'
  
from faker import Faker
fake = Faker()
fake.name()
fake.address()
fakepeoplelist=list([])
for ii in range (5):
    print(fake.name(), fake.address(), end = '\n')
#businesscard6 = FakePeople(namee = "fake.name", address = "fake.address")
print ("----------------------------------")




  

#https://naukapython.pl/co-kazdy-powinien-wiedziec-o-iteratorach-w-pythonie/