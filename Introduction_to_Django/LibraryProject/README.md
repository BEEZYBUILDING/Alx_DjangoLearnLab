# Create a new Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Expected output:
# The object is successfully saved to the database.
# You can confirm by running:
# Book.objects.get(title="1984")
# Output: <Book: 1984>

