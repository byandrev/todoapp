# ToDo App

## Installation

### Clone the repo

```bash
git clone git@github.com:byandrev/todoapp.git # with SSH

or

git clone https://github.com/byandrev/todoapp.git # with HTTPS
```

### Create Virtual Env

```bash
python -m venv venv
source ./venv/bin/activate # in Linux
.\venv\Scripts\activate # in Windows
```

### Install the dependencies

```bash
pip install -r requirements/dev.txt
```

### Run the Server

```bash
make run

or

python manage.py runserver
```

## Linters

```bash
make lint

or

python -m  flake8 .
```

## Format

```bash
make format

or

python -m  black .
```

## Contributors

* Andres Parra - [byandrev](https://github.com/byandrev)
* Mauricio Di Donato - [MauricioDDS](https://github.com/MauricioDDS)
* Andersson Cardenas - [anderssonccg](https://github.com/anderssonccg)
