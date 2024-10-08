# API Endpoints

## Books

### List Books
- **Endpoint:** `/books/`
- **Methods:** `GET`, `POST`
- **Permissions:** Open to all (no authentication required)

### Retrieve, Update, Delete Book
- **Endpoint:** `/books/<int:pk>/`
- **Methods:** `GET`, `PUT/PATCH`, `DELETE`
- **Permissions:** Authenticated users only

## Customizations
- **CreateView**: Allows adding new books, customized to save data with potential preprocessing.
- **UpdateView**: Custom update logic can be added.
- **Permissions**: `ListView` is open to all users; `DetailView` requires authentication.

# API Endpoints

## Books

### Filtering
- **Endpoint:** `/books/`
- **Query Parameters:** `title`, `author`, `publication_year`
- **Example:** `/books/?title=Harry Potter&author=Rowling`

### Searching
- **Endpoint:** `/books/`
- **Query Parameters:** `search`
- **Example:** `/books/?search=Adventure`

### Ordering
- **Endpoint:** `/books/`
- **Query Parameters:** `ordering`
- **Example:** `/books/?ordering=-publication_year` (descending order)

## Customizations
- **Filtering:** Allows filtering by title, author, and publication year.
- **Searching:** Searches across title and author fields.
- **Ordering:** Sorts by title or publication year (ascending or descending).

# API Testing

## Testing Strategy

- **CRUD Operations**: Ensure that Create, Retrieve, Update, and Delete operations for the Book model work correctly.
- **Advanced Query Features**: Validate filtering, searching, and ordering functionalities.
- **Permissions**: Verify that authentication and permissions are correctly enforced.

## Running Tests

1. Ensure the Django test server is set up.
2. Run tests with the following command:
   ```bash
   python manage.py test api
