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



# Comment System for Blog Posts

This module adds a comment system to the Django blog project. Users can leave comments on blog posts, fostering community engagement.

## Features
- Add comments to blog posts.
- Edit or delete comments (authors only).
- Display all comments under each post.

## URLs
- `/post/<int:post_id>/comment/new/` - Add a new comment.
- `/comment/<int:pk>/edit/` - Edit a comment.
- `/comment/<int:pk>/delete/` - Delete a comment.

## Security
- Login required for commenting.
- Authorization checks for editing and deleting comments.