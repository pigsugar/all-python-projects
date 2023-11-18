class parent():
    def __init__(self):
        print("this is a parent class")
        
    def menu(dish):
        if dish == "burger":
            print("you can add the following toppings")
            print("more cheese | add jalapeno")
        elif dish == "iced_americano":
            print("you can add the following toppings")
            print("chocolate | caramel")
        else:
            print("please enter vallid dish")
            
    def final_amount(dish, add_ons):
        if dish=="burger" and add_ons == "cheese":
            print("the final amount is 2590 dollars")
        elif dish=="burger" and add_ons =="jalapeno":
            print("the total price is 0.009 dollars")
        elif dish=="iced_americano" and add_ons=="chocolate":
            print("the final amount is unavailable cause we dont have chocolate in stock")
        elif dish=="iced_americano" and add_ons=="chocolate":
            print("caramel is very delicious so im keeping it you can have the iced americano with no caramel. 7.99 dollars")
            
class child1(parent):
    def __init__(self,dish):
        self.new_dish= dish
    def getmenu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
        
child1_object=child1("burger")
child1_object.getmenu()

child2_object=child2("burger","cheese")
child2_object.get_final_amount()
        
       
        
        