# Definire una classe Book che abbia come attributi di istanza title e category.
class Book:
    total_book = 0
    categories = set()
    
    def __init__(self,title,category):
        self.title = title
        self.category = category
        Book.total_book += 1
        Book.add_category(category)

    @staticmethod
    def add_category(category,categories):
        if category not in categories:
            Book.add(category)
            return categories
        else:
            return f"Categoria {categories} presente"
    
    @staticmethod
    def get_total_book(self):
        return Book.total_book
    
    
libro = Book("io","horror")
libro1 = Book("loro","horror")
libro2 = Book("ajeje","comico")
print(Book.get_total_book())



    
