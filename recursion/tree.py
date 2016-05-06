import turtle
import random


def rand_angle():
    return random.randrange(15, 46)


def tree(t, branch_len):
    if branch_len > 5:

        if branch_len <= 15:
            t.color('green')

        t.pensize(branch_len / 10)
        t.forward(branch_len)

        right_angle = rand_angle()
        t.right(right_angle)

        tree(t, branch_len - random.randrange(5, 16))
        left_angle = rand_angle()
        t.left(right_angle + left_angle)
        tree(t, branch_len - random.randrange(5, 16))
        t.right(left_angle)

        t.backward(branch_len)
        t.color('black')


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("black")
    t.pensize(0.6)
    tree(t, 90)
    my_win.exitonclick()

main()
