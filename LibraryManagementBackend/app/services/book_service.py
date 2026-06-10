from app.models.book import Book

def add_book(db, book_data):
    book = Book(
        title=book_data.title,
        author=book_data.author,
        quantity=book_data.quantity,
        available=book_data.quantity
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book