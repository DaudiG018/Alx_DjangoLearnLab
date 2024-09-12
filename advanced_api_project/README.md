# Advanced API Project

## API Endpoints

- **List Books**: `GET /api/books/`
  - Retrieve a list of all books.
- **Retrieve a Book**: `GET /api/books/<id>/`
  - Retrieve details of a specific book.
- **Create a Book**: `POST /api/books/`
  - Create a new book (authentication required).
- **Update a Book**: `PUT /api/books/<id>/`
  - Update details of a specific book (authentication required).
- **Delete a Book**: `DELETE /api/books/<id>/`
  - Delete a specific book (authentication required).

## Permissions

- List and Retrieve endpoints are accessible without authentication.
- Create, Update, and Delete endpoints require authentication.
