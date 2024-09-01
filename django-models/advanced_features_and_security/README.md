#All about the
# Permissions and Groups Setup

## Permissions
The `Article` model includes the following custom permissions:
- `can_view`: Allows viewing articles.
- `can_create`: Allows creating new articles.
- `can_edit`: Allows editing existing articles.
- `can_delete`: Allows deleting articles.

## Groups
- **Editors**: Assigned `can_edit` and `can_create` permissions.
- **Viewers**: Assigned `can_view` permission.
- **Admins**: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Usage
Use the `@permission_required` decorator to enforce permissions in views. Ensure that users are assigned to the appropriate groups to match their access level.
