# Pokécards - Pokémon Trading Card Collection Builder

## Description

Pokécards is a web application built with Django, Python, and JavaScript. It allows users to build and manage their Pokémon trading card collections online.

## Features

- User registration and authentication system.
- Browse and search Pokémon trading cards from a comprehensive database.
- Add cards to your collection and manage your collection.
- User-friendly interface for an enjoyable user experience.

## Installation

1. Clone the repository:

```
git clone https://github.com/Endeyr/pokecards.git

```

2. Change into the project directory:

```
cd pokecards
```

3. Create a virtual environment:

Install python3 and python3 venv if you haven't already

```
python3 -m venv env
```

1. Activate the virtual environment:

```
source env/bin/activate
```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Set up secrets:

Follow this guide https://github.com/kakulukia/django-secrets

7. Add api key:

Sign up at https://dev.pokemontcg.io/
Add api key to secrets.py created in step 6

8. Set up the database:

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

1. Seed the database:

```
python3 manage.py seed
```

10. Setup tailwind:

```
python3 manage.py tailwind install
```

10. Run tailwind:

```
python3 manage.py tailwind start
```

10. Run the development server:

```
python3 manage.py runserver
```

11. Access the application by visiting http://localhost:8000 in your web browser.

## Usage

- Register a new account or log in with an existing account.
- Explore the collection of Pokémon trading cards.
- Add cards to your collection and manage your collection.
- Create a user bio.

## Contributing

I am not planning on updating or maintaining this project. If you would like to contribute please fork the repository.

## License

This project is licensed under the MIT License.

## Acknowledgements

This application uses data from the Pokémon TCG API. (Link to the API documentation)
Special thanks to the Django, Python, and TailwindCSS communities for their excellent frameworks and libraries.
Inspired by https://pokemontcg.guru/

## Project

This project is a web application capstone for the CS50's Web Programming course. It is for educational purposes only.
This project is not a social media or e-commerce site but built to utilize an api, explore and create databases, be mobile-responsive, and utilize django for the back-end and javascript for the front-end.

## Distinctiveness and Complexity

## File Explanations

These are the important files for the project and their usage:

# management/commands/seed.py

How the user seeds the data to the project. In this file I formatted the api data then saved it to my models.py file. This allowed me to quickly access the database as users search for specific cards. An alternative approach could be using javascript to access the api at each user request but from my research, that process doesn't scale well with larger user bases as you quickly hit the api limit on the free tier. I could improve this process by properly deserializing some of the data before I save it to the database but I was having trouble working with that particular code and process so I opted for a more blunt approach of saving the more complex data into a text area then parsing through that string in the views before passing it to my template.

# templates/main

The main html for this project. These files handle the front end for searching, creating collections, viewing user profile, navigation, and the base index. I created a html file for each page of functionality and decided to use tailwind to style my components as I wanted a mobile first design pattern. Tailwind ended up being the best choice since it is by design mobile first.

# templates/users

The user html for this project. These files handle the front end for user registration and login functionality. I utilized django's builtin user creation and authentication then created these files as the font end. Again I used tailwind along with django's form model.

# forms.py

# models.py

# urls.py

# views.py

# my_secrets/definitions.py

# my_secrets/secrets.py

# static/main.js

# theme/static_src/tailwind.config.js

# users/forms.py

# users/urls.py

# users/views.py

# requirements.txt

## Additional Information
