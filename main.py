# Simple API server
# vvuri, 2021
from app.dao import create_database, app
from config import DevConfig


def print_start():
    print('Run server on Flask')


if __name__ == '__main__':
    print_start()
    create_database()
    app.config.from_object(DevConfig)
    app.run()
