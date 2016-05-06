import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
    def __init__(self, maze_file_name):
        columns_in_maze = 0
        self.maze_list = []

        maze_file = open(maze_file_name, 'r')

        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = col

                col += 1

            rows_in_maze += 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)

        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze

        self.x_translate = -columns_in_maze / 2
        self.y_translate = rows_in_maze / 2

        turtle.setup(width=600, height=600)
        turtle.setworldcoordinates(
            -(columns_in_maze - 1) / 2 - 0.5,
            -(rows_in_maze - 1) / 2 - 0.5,
            (columns_in_maze - 1) / 2 + 0.5,
            (rows_in_maze - 1) / 2 + 0.5
        )
        turtle.title('Maze')
        self.t = turtle.Turtle()
        self.t.speed('fastest')

    def draw_maze(self):
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate, -y + self.y_translate, 'tan')
        self.t.color('black', 'blue')

    def draw_centered_box(self, x, y, color):
        turtle.tracer(0)
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        turtle.update()
        turtle.tracer(1)

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_breadcrumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.drop_breadcrumb(color)

    def is_exit(self, row, col):
        return row == 0 or row == self.rows_in_maze - 1 or \
               col == 0 or col == self.columns_in_maze - 1

    def __getitem__(self, index):
        return self.maze_list[index]


def search_from(maze, start_row, start_column):
    maze.update_position(start_row, start_column)

    if maze[start_row][start_column] == OBSTACLE:
        return False
    if maze[start_row][start_column] == TRIED or maze[start_row][start_column] == DEAD_END:
        return False
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True

    maze.update_position(start_row, start_column, TRIED)

    found = \
        search_from(maze, start_row, start_column + 1) or \
        search_from(maze, start_row + 1, start_column) or \
        search_from(maze, start_row - 1, start_column) or \
        search_from(maze, start_row, start_column - 1)

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)

    return found

my_maze = Maze('map.txt')
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)
search_from(my_maze, my_maze.start_row, my_maze.start_col)

# turtle.setup(width=600, height=600)
# turtle.title('Maze')
# turtle.setworldcoordinates(0, 600, 600,0)
# t = turtle.Turtle()
# t.up()
# t.goto(0,0)
