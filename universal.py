class Room:
    def __init__( self, *args, **kwargs ):
        self.__number = 1
        self.__area   = 20
        self.__place  = 12
        self.__name   = "Noname"
        
        # print(f"{len(args)}")
        # for i in args:
        #     print(i)
        # for key, val in kwargs.items():
        #     print(f"{key}: {val}")
        
        if len(args) > 0: self.__number = args[0]
        if len(args) > 1: self.__area = args[1]
        if len(args) > 2: self.__place = args[2]
        if len(args) > 3: self.__name = args[3]

        # for key, val in kwargs.items():
        if "name" in kwargs: self.__name = kwargs["name"]
        if "area" in kwargs: self.__area = kwargs["area"]
        if "place" in kwargs: self.__place = kwargs["place"]
        if "number" in kwargs: self.__number = kwargs["number"]    
        

    @property
    def number( self ):
        return self.__number
    @number.setter  
    def number( self, value ):
        self.__number = value

    @property
    def area(self):
        return self.__area
    @area.setter
    def area( self, val ):
        if (val >= 20) and (val <= 1000):
            self.__area = val
        else:
            print( 'Ошибка: недопустимая площадь кабинета!' )
            #raise Exception('Ошибка: недопустимая площадь кабинета!')
        pass 

    
    def __str__(self):
        return (f"Number = {self.number}\n" + f"Area = {self.area}\n" + 
                f'Place = {self.__place}\n'  + f"Name is {self.__name}\n" + '-'*20)
    
r2 = Room( 16, 202, 48, "Конференц-зал" ) 
r2 = Room( name = "Конференц-зал", area = 48, number = 202, place=16 ) 
print(r2)

