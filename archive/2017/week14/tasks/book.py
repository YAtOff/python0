"""
Представете си, че трябва да напишем програма за работа с книги.
Тя има следните операции:
- добавяне на книга
- разглеждане на всички книти
- търсене на книга по име, жанр или автор
- изтриване на книги

По какъв начин бихме представили книгите?
Книгите са много - следователно трябва да са в списък.
Каква информация ще имаме за всяка книга?
- Име
- Автор
- Година на публикуване
- Брой страници
- Жанр
- ... много други атрибути

Най-лесният начин е да запазим данните за всяка книга като речник.
"""


books = [
    {
        "title": "Python Tricks: A Buffet of Awesome Python Features",
        "author": "Dan Bader",
        "genre": "programming Python",
        "detail": {
            "publication_year": 2017,
            "isbn-13": 9781775093305,
            "language": "English",
            "pages": 302
        }
    },
    {
        "title": "Fluent Python: Clear, Concise, and Effective Programming",
        "author": "Luciano Ramalho",
        "genre": "programming Python",
        "detail": {
            "publication_year": 2015,
            "isbn-13": 9781491946008,
            "language": "English",
            "pages": 792
        }
    }
]


def list_books():
    """
    Принтира таблица от книги
    """
    pass


def find_book_by_title(title):
    """
    title - стойността на title
    Връща първата книга с заглавие `title` или None ако няма такава
    """
    pass


def find_book(by_what, value):
    """
    by_what - може да бъде title, author, genre
    value - стойността на title, author или genre
    Връща списък от намерени книги
    """
    pass
