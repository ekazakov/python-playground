import turtle


def draw_triangle(t, points, color="black"):
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()


def mid_point(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(t, points, level=7):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange', 'tan', 'cyan']
    draw_triangle(t, points, colormap[level])

    if level > 0:
        sierpinski(t,
                   (points[0], mid_point(points[0], points[1]), mid_point(points[0], points[2])),
                   level - 1)
        sierpinski(t,
                   (points[1], mid_point(points[1], points[0]), mid_point(points[1], points[2])),
                   level - 1)
        sierpinski(t,
                   (points[2], mid_point(points[2], points[1]), mid_point(points[2], points[0])),
                   level - 1)


def main():
    turtle.setup(width=1920, height=1080)
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_win = turtle.Screen()
    # my_turtle._tracer(0,0)

    points = ((-600, -500), (0, 400), (600, -500))

    # draw_triangle(my_turtle, points)
    sierpinski(my_turtle, points)
    my_win.exitonclick()


main()
