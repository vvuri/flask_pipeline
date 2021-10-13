# Simple API server
# vvuri, 2021

from app.hello import app

def print_hi(name):
    print(f'Hi, {name}!')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')
    app.run()
