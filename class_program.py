class book():
    def __init__(self,book_author,book_name):
        self.book_author=book_author
        self.book_name=book_name

    def __str__(self):
        return f"book name is {self.book_name} and author is {self.book_author}"

b1=book("charlien","'love is sweet'")
print(b1)