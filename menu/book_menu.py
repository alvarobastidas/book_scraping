class Menu:
    def __init__(self, all_content):
        self.all_content = all_content

    @property
    def by_rating(self):
        #number_rating = float(input('Enter the number of star from 1 to 5: '))
        return [a for a in self.all_content if a.rating == 3]

    @property
    def by_price(self):
        #min_price = float(input('Enter the min price: '))
        #max_price = float(input('Enter the max price: '))
        return [a for a in self.all_content if 10 <= a.price[0] <= 20]

    @property
    def best_books(self):
        return sorted(self.all_content, key = lambda x: x.rating * -1)[:10]

    @property
    def cheapest_books(self):
        return sorted(self.all_content, key=lambda x: x.price)[:10]

    @property
    def all_books(self):
        return self.all_content
