from os import system
from keyboard import is_pressed


def __init__():
    pass


pip = r"pip install --upgrade --target=D:\pythonProject2\DivisionByZero\modules "
while not is_pressed("esc"):
    system(pip + input(pip))
