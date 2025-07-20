from relationship_app.models import Author, Book, Library, Librarian

# Create an Author if not exists
author, created = Author.objects.get_or_create(name="George Orwell")

# Create Books if not exist
book1, _ = Book.objects.get_or_create(title="1984", author=author)
book2, _ = Book.objects.get_or_create(title="Animal Farm", author=author)

# Create a Library and add the books
library, _ = Library.objects.get_or_create(name="Central Library")
library.books.set([book1, book2])  # This clears and sets books

# Create a Librarian for the library
librarian, _ = Librarian.objects.get_or_create(name="Mr. Smith", library=library)

# --- Queries & Output ---
print("Books by George Orwell:")
for book in Book.objects.filter(author=author):
    print(f"- {book.title}")

print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print(f"- {book.title}")

print(f"\nLibrarian for {library.name}: {librarian.name}")
