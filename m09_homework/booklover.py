import pandas as pd

class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    
    def add_book(self, book_name, rating):
        new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
        if book_name in self.book_list.book_name.unique():
            return ('this book is already in the list')
        else:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        overthree = self.book_list[self.book_list['book_rating'] > 3]
        return overthree
    

if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Emma", 2)
    test_object.has_read("War of the Worlds")
    test_object.num_books_read()
    test_object.fav_books()