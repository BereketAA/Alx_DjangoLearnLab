# Blog Post Management

This module adds CRUD functionality to the Django blog project. Authenticated users can create, update, and delete posts. All users can view posts.

## Features
- List all posts
- View individual posts
- Create new posts (authenticated users only)
- Edit or delete posts (authors only)

## URLs
- `/` - List all posts
- `/post/<int:pk>/` - View a post
- `/post/new/` - Create a post
- `/post/<int:pk>/edit/` - Edit a post
- `/post/<int:pk>/delete/` - Delete a post

## Security
- Login required for creating posts.
- Authorization checks for editing and deleting posts.