# For this question, you are asked to write the StackTest class with the following functionality:
#     constructor(stack:Stack): The constructor will Initialize a protected variable stack with the input stack of Vehicle objects.
#     get_stack(): This method will return the stack of Vehicle objects.
#     compute_net_profit(year:Integer): This method will compute and return the net profit made from sales of all vehicles with a model year greater than the input year. For any vehicle sale, the sales profit (or loss) is the difference between its sales price and the dealer cost. The net profit is the sum of all such differences. You are required to use the original stack to compute the net profit. Your original stack should remain intact in the end i.e. it should have all the elements (Vehicle objects) in the same order as it had at the start of this method. You may remove some stack elements, process them, and then add them back to the original stack to maintain the original order. You are not allowed to use the copy module. However, you may use multiple stacks for the temporary storage of Vehicle objects.
#      Example:
#      Sales1: dealer_cost: 2000.10, sales_price: 3000.10, profit = 1000.00
#      Sales2: dealer_cost: 2500.12, sales_price: 2300.12, profit = -200.00
#      Sales3: dealer_cost: 1500.15, sales_price: 2000.15, profit = 500.00
#      net profit = 1000-200+500 = 1300
# You are required to use the given Stack class. The use of the deque module is prohibited. The Stack class has the following functionality:

#     pop_element() - removes and returns the top element of the stack.
#     push_element(input_element) - adds the input element to the stack.
#     top_element() - returns the top element of the stack without removing it.
#     stack_size():Integer - returns the number of elements in the stack.
#     print_stack(order:Integer) - print the stack elements from top-to-bottom if the order is 0, and from bottom-to-top if the order is 1.
# You do not need to write the Vehicle class. This class has already been created and imported for you. Vehicles have an ADT defined as:
# Vehicle ADT:
# Data:
#     year:Integer - An integer indicating the model year.
#     mileage:Integer - An integer indicating the vehicle mileage. 
#     dealer_cost:Float - A float indicating the dealer cost.
#     sales_price:Float - A float indicating the sales price.

# Operations:
#     constructor(year:Integer, mileage:Integer, dealer_cost:Float, sales_price:Float)
#     get_year():Integer Returns the model year
#     get_mileage():Integer Returns the vehicle's mileage
#     get_dealer_cost():Float Returns the dealer cost
#     get_sales_price():Float Returns the sales price
#     set_year(year:Integer): Sets the year to be the value in the first parameter
#     set_mileage(mileage:Integer): Sets the mileage to be the value in the first parameter
#     set_dealer_cost(dealer_cost:Float): Sets the dealer_cost to be the value in the first parameter
#     set_sales_price(sales_price:Float): Sets the sales_price to be the value in the first parameter
# The _str_ method represents the Vehicle object as a string.
# **Test cases also include a call to the CreateStack function. This function creates a stack of vehicle objects. You do not need to know about the details of this function.
# For example:
# Test 	Result
# sk = CreateStack("vehicles.csv")
# sobj = StackTest(sk)
# print(round(sobj.compute_net_profit(2015),2))
# 3111.75
# sk = CreateStack("vehicles.csv")
# sobj = StackTest(sk)
# sobj.get_stack().print_stack(0)
# Stack elements - from top to bottom:
# Year:2009, Mileage:346, CarCondition:Used, DealerCost:21654.12, SalesPrice:22654.24
# Year:2003, Mileage:232, CarCondition:Used, DealerCost:16729.76, SalesPrice:17292.72
# Year:2006, Mileage:567, CarCondition:Used, DealerCost:13432.14, SalesPrice:13698.43
# Year:2020, Mileage:342, CarCondition:Used, DealerCost:10000.12, SalesPrice:11010.43
# Year:2018, Mileage:57, CarCondition:Used, DealerCost:12200.12, SalesPrice:12652.29
# Year:2005, Mileage:5632, CarCondition:Used, DealerCost:12321.67, SalesPrice:12439.78
# Year:2003, Mileage:3232, CarCondition:Used, DealerCost:52132.23, SalesPrice:54130.67
# Year:2004, Mileage:56742, CarCondition:Used, DealerCost:12321.23, SalesPrice:13333.76
# Year:2016, Mileage:424, CarCondition:Used, DealerCost:18752.23, SalesPrice:18760.12
# Year:2018, Mileage:532, CarCondition:Used, DealerCost:23123.76, SalesPrice:23765.34
# Year:2013, Mileage:3242, CarCondition:Used, DealerCost:32120.54, SalesPrice:32232.12
# Year:2011, Mileage:2321, CarCondition:Used, DealerCost:10901.12, SalesPrice:12231.34
# Year:2010, Mileage:12, CarCondition:Used, DealerCost:32123.34, SalesPrice:33223.14
# Year:2000, Mileage:4, CarCondition:Used, DealerCost:19123.67, SalesPrice:19412.62
# Year:2008, Mileage:20, CarCondition:Used, DealerCost:10000.12, SalesPrice:12000.32
# Year:2001, Mileage:2000, CarCondition:Used, DealerCost:12652.23, SalesPrice:14232.23
# Year:2013, Mileage:500, CarCondition:Used, DealerCost:52321.56, SalesPrice:52124.12
# Year:2005, Mileage:200, CarCondition:Used, DealerCost:43231.12, SalesPrice:43120.12
# Year:2019, Mileage:0, CarCondition:New, DealerCost:32000.32, SalesPrice:33000.12
# Year:2015, Mileage:2000, CarCondition:Used, DealerCost:10323.23, SalesPrice:12324.45

import csv


class Vehicle:
    def __init__(self, year, mileage, dealer_cost, sales_price):
        self.year = year
        self.mileage = mileage
        self.dealer_cost = dealer_cost
        self.sales_price = sales_price

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def get_dealer_cost(self):
        return self.dealer_cost

    def get_sales_price(self):
        return self.sales_price

    def set_year(self, year):
        self.year = year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_dealer_cost(self, dealer_cost):
        self.dealer_cost = dealer_cost

    def set_sales_price(self, sales_price):
        self.sales_price = sales_price

    def __str__(self):
        return "Year: " + str(self.year) + ", Mileage: " + str(self.mileage) + ", CarCondition: Used, DealerCost: " + str(
            self.dealer_cost) + ", SalesPrice: " + str(self.sales_price)
        
class StackTest:
    def __init__(self, stack):
        self.stack = stack

    def compute_net_profit(self, year):
        profit = 0
        while self.stack.stack_size() > 0:
            vehicle = self.stack.pop_element()
            if vehicle.get_year() > year:
                profit += vehicle.get_sales_price() - vehicle.get_dealer_cost()
        return profit
    
    # get_stack(): This method will return the stack of Vehicle objects.
    def get_stack(self):
        return self.stack
    
class Stack:
    def __init__(self):
        self.stack = []

    def push_element(self, element):
        self.stack.append(element)

    def pop_element(self):
        return self.stack.pop()

    def stack_size(self):
        return len(self.stack)

    def print_stack(self, order):
        if order == 0:
            for i in range(len(self.stack)):
                print(self.stack[i])
        else:
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])
                
                
def CreateStack(file_name):
    stack = Stack()
    # Create the csv file 
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            vehicle = Vehicle(int(row[0]), int(row[1]), float(row[2]), float(row[3]))
            stack.push_element(vehicle)
    
    return stack


def main():
    sk = CreateStack("vehicles.csv")
    sobj = StackTest(sk)
    print(round(sobj.compute_net_profit(2015), 2))
    sk = CreateStack("vehicles.csv")
    sobj = StackTest(sk)
    sobj.get_stack().print_stack(0)
    sk = CreateStack("vehicles.csv")
    sobj = StackTest(sk)
    sobj.get_stack().print_stack(1)
    
if __name__ == "__main__":
    main()
   