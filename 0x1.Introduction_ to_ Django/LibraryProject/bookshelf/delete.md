**Delete Operation**

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
from bookshelf.models import Book
