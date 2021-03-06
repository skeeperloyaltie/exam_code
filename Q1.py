

class Cake:
    def __init__(self, flavour, layers):
        self.__flavour = flavour
        self.__layers = layers

    def set_flavour(self, flavour):
        self.__flavour = flavour

    def set_layers(self, layers):
        self.__layers = layers

    def get_flavour(self):
        return self.__flavour

    def get_layers(self):
        return self.__layers

    def __str__(self):
        return "Flavour: " + self.__flavour + ", Layers: " + str(self.__layers)

    def __eq__(self, other):
        if isinstance(other, Cake):
            return self.__flavour == other.__flavour and self.__layers == other.__layers
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
    

def main():
    cake1 = Cake("Black Forest", 2)
    cake2 = Cake("Black Forest", 2)
    cake3 = Cake("Chocolate", 2)
    cake4 = Cake("Chocolate", 3)
    cake5 = Cake("Chocolate", 3)
    
    print(cake1)
    print(cake2)
    print(cake3)
    print(cake4)
    print(cake5)

if __name__ == "__main__":
    main()
    


