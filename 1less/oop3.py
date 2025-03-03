'''
Реализуйте класс <Человек>.
Необходимо хранить в полях класса:
  ФИО,
  дату рождения,
  контактный телефон,
  домашний адрес,
  ежемесячный доход.
Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса.
'''
from random import randint
#man1 = Person()
#man2 = Person()
class Person:
    # конструктор, инициализатор класса
    # self === this
    def __init__( self ): # конструктор по умолчанию
        fio   = 'fhvkdhvkdh'
        self.fio   = 'noname'
        self.bdate = ''  # дата рождения
        self.phone = '+7__________' #
        self.address = 'unknown'
        self.salary = randint( 200_000, 2_000_000 )
        pass # def __init__( self )
    # Методы-аксессоры для доступа к переменнемы/атрибутам класса
    # set-методы, мктоды-модификаторы
    # сеттер для атрибута self.fio
    def set_fio( self, new_fio : str ) -> None:
        self.fio = new_fio

    # сеттер для атрибута self.bdate
    def set_birth_date( self, new_date ):
        self.bdate = new_date

    def set_phone( self, new_phone : str ):
        # +77071234567 - 12
        #  87071234567 - 11
        if (new_phone[:2] == '+7' and len(new_phone) == 12) or \
           (new_phone[0]  == '8'  and len(new_phone) == 11):
            self.phone = new_phone
        else:
            # ошибка инициализации атрибута phone с печать ошибки на экран
            print( 'Ошибка: неправильный телефон!' )
            # если надо, то можно сгенерировать исключение
            #raise ValueError('Ошибка: неправильный телефон!')
        pass # def set_phone( self, new_phone : str )

    #
    def set_address( self, new_addr : str ):
        self.address = new_addr

    def set_salary( self, new_salary : int ) -> None:
        if new_salary <= 0 or new_salary > 10_000_000:
            print( 'Ошибка: неверная зарплата!' )
            #raise ValueError( 'Ошибка: неверная зарплата!' )
            return  # ==> return None
        self.salary = new_salary

    # get-методы, методы-инспекторы
    def get_fio( self ) -> str:
        return self.fio
        #return self.first + " " + self.lstname + " " + self.family
    def get_birth_date( self ) -> str: # 01.02.2025
        return self.bdate
    def get_phone( self ) -> str:
        return self.phone
    def get_address(self) -> str:
        return self.address
    def get_salary(self) -> int:
        return self.salary
    #---------------------------------------

    def input( self ) -> None:
        '''
        # 1 вариант ввода данных без контроля
        self.fio     = input( 'Введите ФИО: ' )
        self.bdate   = input( 'Введите дату рождения: ' )
        self.address = input( 'Введите адрес: ' )
        self.phone   = input( 'Введите телефон: ' )  # eflvhdvhkdh
        self.salary  = int( input('Введите зарплату: ') )
        '''
        # 2 вариант - с контролем вводим данных
        #  ФЛК - Форматно-логический контроль
        temp = input( 'Введите ФИО: ' )
        self.set_fio( temp )
        temp = input( 'Введите дату рождения: ' )
        self.set_birth_date( temp )
        temp = input('Введите адрес: ')
        self.set_address( temp )
        temp = input( 'Введите телефон: ' )
        self.set_phone( temp )
        temp = int( input('Введите зарплату: ') )
        self.set_salary( temp )
        pass # def input( self )

    # man1.print()
    def print( self ) -> None:
        print(  'Информация о персоне' )
        '''
        # 1 вариант вывода - через прямой доступ к атрибутам класса
        print( f'ФИО: { self.fio }' )
        print( f'Дата рождения: { self.bdate }' )
        print( f'Адрес: { self.address }' )
        print( f'Телефон: { self.phone }' )
        print( f'Зарплата: { self.salary }' )
        '''
        # 2 вариан - через геттеры (get-methods)
        print(f'ФИО: { self.get_fio() }')
        print( f'Дата рождения: { self.get_birth_date() }' )
        print( f'Адрес: { self.get_address() }' )
        print( f'Телефон: { self.get_phone() }' )
        print( f'Зарплата: { self.get_salary() }' )
        pass # def print( self )

    pass # class Person

# Пример работы с классом Person
man1 = Person() # создать экземпляр класса Person
man2 = Person() # создать другой экземпляр класса Person
man1.print()  # вызов метода print для экземпляра man1
man2.print()  # вызов метода print для экземпляра man2
print()
man1.input()
print()
man2.input()
print("-"*20)
man1.print()
man2.print()
