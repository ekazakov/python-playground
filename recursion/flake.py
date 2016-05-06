import turtle


def flake(t, length, level):
    if level == 0:
        return

    t.left(60)
    t.forward(length / 3)
    flake(t, length / 3, level - 1)

    t.forward(length / 3)

    t.right(120)
    t.forward(length / 3)

    flake(t, length / 3, level - 1)

    t.forward(length / 3)
    t.left(60)


def flake_base(t, length, level=7):
    t.left(60)
    t.forward(length / 3)

    flake(t, length / 3, level - 1)

    t.forward(length / 3)
    t.right(120)
    t.forward(length / 3)

    flake(t, length / 3, level - 1)

    # t.left(60)
    t.forward(length / 3)
    t.right(120)
    t.forward(length / 3)
    #
    flake(t, length / 3, level - 1)
    #
    # t.left(60)
    t.forward(length / 3)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_turtle.up()
    my_turtle.goto(-350, -150)
    my_turtle.down()
    flake_base(my_turtle, 600)
    my_win.exitonclick()

# main()