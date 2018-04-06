# Soshiki
A kanban project for the web course of the HE-ARC

## Local installation

Download the requirements with : ```pip install -r requirements.txt```

Make a copy of .env.example with the name `.env` and fill it with your config.

To generate a secret key : ```python manage.py generate_secret_key ```

And replace the default secret key in the .env file with the generated one that is located in the `secretkey.txt` file.

If you change the models, you can generate the corresponding migrations with : ```python manage.py makemigrations```

Then migrate them with : ```python manage.py migrate ```

Then load the fixtures with : ```python manage.py loaddata tables```

## Deployment

[See this Wiki page](https://github.com/HE-Arc/Soshiki/wiki/Deployment).
