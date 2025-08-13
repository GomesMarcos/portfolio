# Marcos Gomes' Custom Portfolio
made with Django

## Local development
### Install Dependencies
1. Create venv: `python -m venv venv`
2. Activate venv: `source venv/bin/activate`
3. Install dev dependencies: `pip install -U pip -r requirements-dev.txt`

### Run migrations
`./manage.py migrate`

## Install TailWind
```
curl -sLo static/css/tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
chmod +x static/css/tailwindcss
curl -sLo static/css/daisyui.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui.js
curl -sLo static/css/daisyui-theme.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui-theme.js
```

### TailWind Commands
```
# Start a watcher
./static/css/tailwindcss -i static/css/input.css -o static/css/output.css --watch

# Compile and minify your CSS for production
./static/css/tailwindcss -i static/css/input.css -o static/css/output.css --minify
```

## LiveReload Development
1. run `pip install -r requirements-dev.txt`
2. Set env var `DEBUG=True`
3. run `./manage.py livereload` before `runserver`
4. run `./manage.py runserver`

Now you can test your templates' changes without reloading page

## Running with Docker
Run in terminal `docker-compose up --build -d`, and them, access `http://127.0.0.1/` (without port)

### Running Docker Local
`docker-compose -f docker-local.yml up --build -d`


## Load Existent Data
1. Dump data from database into `data.json` file:
    - `./manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude sessions.session --exclude admin.logentry > data.json`  
    - PS: If you're using SQLITE db, use dump for it with:
    `./manage.py dumpdata --database=local --exclude auth.permission --exclude contenttypes --exclude sessions.session --exclude admin.logentry > data.json`
2. Load dumped data into default DB:
    - `./manage.py loaddata data.json`

3. In a Docker container, run:
    - `docker-compose exec web ./manage.py loaddata data.json`

### !Important
Remember to exclude superusers from your dumped data JSON file for security proposites.

## Keep the standards!!
This project is formatted by the [ruff.toml](ruff.toml) file.
Every big change run: `ruff format .` on root of the project and them `ruff check .`

## Add Certificate
run `docker-compose exec nginx certbot --nginx -d gomesmarcos.dev.br`
