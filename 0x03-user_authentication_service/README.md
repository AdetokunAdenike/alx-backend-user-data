0x03. User authentication service

This project implements a user authentication service using Flask and SQLAlchemy.

## User Model
- **Table Name**: `users`
- **Attributes**:
  - `id`: Primary key, integer.
  - `email`: Non-nullable string, unique.
  - `hashed_password`: Non-nullable string.
  - `session_id`: Nullable string for tracking sessions.
  - `reset_token`: Nullable string for password reset functionality.
