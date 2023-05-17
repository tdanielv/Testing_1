class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Seller(User):
    def __init__(self, name):
        super().__init__(name, "seller")
        self.lots = []

    def create_lot(self, flower_type, shade, quantity, price):
        lot = Lot(flower_type, shade, quantity, price, self)
        self.lots.append(lot)
        return lot

    def visibility(self, lot):
        lot.visible = not lot.visible

class Buyer(User):
    def __init__(self, name):
        super().__init__(name, "buyer")

class Lot:
    def __init__(self, flower_type, shade, quantity, price, seller):
        self.flower_type = flower_type
        self.shade = shade
        self.quantity = quantity
        self.price = price
        self.seller = seller
        self.visible = False
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

class Transaction:
    def __init__(self, buyer, lot, quantity):
        self.buyer = buyer
        self.lot = lot
        self.quantity = quantity

class FlowerMarket:
    def __init__(self):
        self.users = []
        self.transactions = []

    def add_user(self, user):
        self.users.append(user)

    def create_transaction(self, buyer, lot, quantity):
        if buyer.role == "buyer" and lot.visible and quantity <= lot.quantity:
            transaction = Transaction(buyer, lot, quantity)
            self.transactions.append(transaction)
            lot.quantity -= quantity
            return transaction
        else:
            return None

    def get_sellers_with_buyers(self):
        sellers_with_buyers = []
        for user in self.users:
            if user.role == "seller":
                seller = user
                buyers = []
                total_sales = 0
                for transaction in self.transactions:
                    if transaction.lot.seller == seller:
                        buyers.append(transaction.buyer)
                        total_sales += transaction.lot.price * transaction.quantity
                sellers_with_buyers.append((seller, buyers, total_sales))
        return sellers_with_buyers

market = FlowerMarket()

seller1 = Seller("Ваня")
seller2 = Seller("Дима")
seller3 = Seller("Кузя")
seller4 = Seller("Мама")

buyer1 = Buyer("Лиза")
buyer2 = Buyer("Саша")
buyer3 = Buyer("Вася")
buyer4 = Buyer("Петя")
buyer5 = Buyer("Коля")

market.add_user(seller1)
market.add_user(seller2)
market.add_user(seller3)
market.add_user(seller4)

market.add_user(buyer1)
market.add_user(buyer2)
market.add_user(buyer3)
market.add_user(buyer4)
market.add_user(buyer5)

lot1 = seller1.create_lot("Алоэ", "Спелый", 201, 5)
lot2 = seller2.create_lot("Лилии", "Белые", 433, 10)
lot3 = seller3.create_lot("Ромашка", "Обыкновенная", 120, 1)
lot4 = seller4.create_lot("Тюльпан", "Белый", 200, 3)


seller1.visibility(lot1)
seller2.visibility(lot2)
seller3.visibility(lot3)
seller4.visibility(lot4)

transaction1 = market.create_transaction(buyer1, lot1, 50)
transaction2 = market.create_transaction(buyer2, lot2, 73)
transaction3 = market.create_transaction(buyer3, lot3, 12)
transaction4 = market.create_transaction(buyer4, lot4, 73)
transaction5 = market.create_transaction(buyer5, lot1, 143)
transaction6 = market.create_transaction(buyer1, lot2, 280)
transaction7 = market.create_transaction(buyer2, lot3, 73)

review1 = "Все супер!"
review2 = "Спсибо!"
review3 = "Отличные ребята!"
review4 = "Все хорошо!"
review5 = "Просто уау!"
review6 = "Спасли праздник!"
review7 = "Ееееее!"

lot1.add_review(review1)
lot2.add_review(review2)
lot3.add_review(review2)
lot4.add_review(review2)
lot1.add_review(review2)
lot2.add_review(review2)
lot3.add_review(review2)

sellers_with_buyers = market.get_sellers_with_buyers()

for seller, buyers, total_sales in sellers_with_buyers:
    print("Продавец:", seller.name)
    print("Покупатели:", [buyer.name for buyer in buyers])
    print("Общая сумма покупок:", total_sales)
