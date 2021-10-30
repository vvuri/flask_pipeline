# Simple API server
# vvuri, 2021
from app.dao import create_database, app


def print_start():
    print('Run server on Flask')


if __name__ == '__main__':
    print_start()
    create_database()
    app.run(debug=True)
