from random import randrange, choice
from turtle import *
from freegames import square, vector
import time

colors = ['blue', 'green', 'yellow', 'purple', 'orange']

snake_color = choice(colors)
food_color = choice([c for c in colors if c != snake_color])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(point):
    """Return True if head inside boundaries."""
    return -200 < point.x < 190 and -200 < point.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

def move_food():
    """Move the food randomly within boundaries."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    rand_direction = directions[randrange(4)]

    new_food_pos = food + rand_direction
    if inside(new_food_pos):
        food.move(rand_direction)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
time.sleep(3)
move()
done()
