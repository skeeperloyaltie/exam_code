
class Person:
    def __init__(self, year):
        self.__id = id(self)
        self.__first = None
        self.__last = None
        self.__year = year
        
    
    def __str__(self):
        return "ID: " + str(self.__id) + ", First Name: " + self.__first + ", Last Name: " + self.__last + ", Birth Year: " + str(self.__year)
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.__id == other.__id and self.__first == other.__first and self.__last == other.__last and self.__year == other.__year
        else:
            return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def get_id(self):
        return self.__id
    
    def get_first_name(self):
        return self.__first
    
    def get_last_name(self):
        return self.__last
    
    def get_birth_year(self):
        return self.__year
    
    def set_birth_year(self, year):
        self.__year = year
    
    def set_first_name(self, fname):
        self.__first = fname
    
    def set_last_name(self, lname):
        self.__last = lname
    
    def validateName(self, name):
        if name.find(":") == -1:
            return False
        else:
            return True
    
    def set_name(self, name):
        if self.validateName(name):
            self.set_first_name(name.split(":")[0])
            self.set_last_name(name.split(":")[1])
        else:
            print("Invalid name")
    
    @staticmethod
    def get_id_count():
        return Person.__id_count


    
class BirthRegistration(Person):
    def __init__(self, year):
        super().__init__(year)
        self.__id = id(self)
        self.__first = None
        self.__last = None
        self.__year = year
        
    def __str__(self):
        return "ID: " + str(self.__id) + ", First Name: " + self.__first + ", Last Name: " + self.__last + ", Birth Year: " + str(self.__year)
    
    def __eq__(self, other):
        if isinstance(other, BirthRegistration):
            return self.__id == other.__id and self.__first == other.__first and self.__last == other.__last and self.__year == other.__year
        else:
            return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def get_id(self):
        return self.__id
    
    def get_first_name(self):
        return self.__first
    
    def get_last_name(self):
        return self.__last
    
    def get_birth_year(self):
        return self.__year
    
    def set_birth_year(self, year):
        self.__year = year
    
    def set_first_name(self, fname):
        self.__first = fname
    
    def set_last_name(self, lname):
        self.__last = lname
    
    def validateName(self, name):
        if name.find(":") == -1:
            return False
        else:
            return True
    
    def set_name(self, name):
        if self.validateName(name):
            self.set_first_name(name.split(":")[0])
            self.set_last_name(name.split(":")[1])
        else:
            print("Invalid name")
    
    @staticmethod
    def get_id_count():
        return Person.__id_count
    
        
    
def main():
    p1 = Person(2000)
    p1.set_name("John:Doe")
    p2 = Person(2000)
    p2.set_name("John:Doe")
  
    
    
    print(p1)
    print(p2)
   



if __name__ == "__main__":
    main()

    
     
