# Simple API server
# vvuri, 2021

from app.api_route import app


def print_start():
    print('Run server on Flask')


if __name__ == '__main__':
    print_start()
    app.run()
