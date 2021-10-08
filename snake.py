from turtle import Turtle




class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.snake_shape = self.snake_body()

    def snake_body(self):
        snake_segments = []
        positions = [0, -20, -40]
        for seg in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(positions[seg], 0)
            snake_segments.append(segment)
        return snake_segments

    def snake_animation(self):
        for seg in range(len(self.snake_shape) -1, 0, -1):
            snake_seg = self.snake_shape[seg - 1]
            new_x = snake_seg.xcor()
            new_y = snake_seg.ycor()
            snake_seg.goto(new_x, new_y)
        self.snake_shape[0].forward(20)







