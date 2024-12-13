# Clone the repository
$ git clone <repository-url>
$ cd social_media_api

# Create a virtual environment
$ python -m venv venv

# Activate the virtual environment

$ source venv\Scripts\activate

# Apply Migrations
$ python manage.py makemigrations
$ python manage.py migrate

# Run the Server
python manage.py runserver



### API Endpoints

Endpoint: POST /api/accounts/register/

Request Body:

{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "securepassword"
}

Response:

{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}

### User Login (Optional Enhancement)

If login is implemented:
Endpoint: POST /api/token/

Request Body:

{
    "username": "testuser",
    "password": "securepassword"
}

Response:
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}