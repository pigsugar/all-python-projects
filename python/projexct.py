class Allies:
    def __init__(self,book, price,maincharacter,author,published):
        self.book_name = book
        self.book_price = price
        self.book_maincharacter = maincharacter
        self.book_author = author
        self.book_published = published
        
    def add_book(self):
         print("book: "+self.book_name)
         print("price: "+str(self.book_price))
         print("maincharacter: "+self.book_maincharacter)
         print("author: "+self.book_author)
         print("published: "+self.book_published)


         
groundzero = Allies("groundzero", 11.99,"reshmina","alan gratz","february 2nd 2021")        
groundzero.add_book() 

allies = Allies("allies",11.99,"dee","alan gratz","october 3rd 2019")        
allies.add_book() 