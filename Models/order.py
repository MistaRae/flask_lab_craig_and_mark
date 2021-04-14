class Order():
    
    def __init__ (self, customer_name, order_date, quantity, food_name):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.food_name = food_name
        self.items_ordered = []
    

    def add_food_to_items_ordered(self, item):
        self.items_ordered.append(item)