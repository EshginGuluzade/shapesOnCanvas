from canvas import Canvas
from shapes import Rectangle, Square

print("Hi! Let's draw squares and rectangles!")
canvas_width = int(input("Enter the width of canvas: "))
canvas_height = int(input("Enter the height of canvas: "))
canvas_color_red = int(input("Enter the value of red color for canvas: "))
canvas_color_green = int(input("Enter the value of green color for canvas: "))
canvas_color_blue = int(input("Enter the value of blue color for canvas: "))
canvas = Canvas(width=canvas_width, height=canvas_height, color=[canvas_color_red, canvas_color_green,
                                                                 canvas_color_blue])

while True:
    shape = input("What do you want to draw: 'rectangle' or 'square'? Write 'quit' to quit. ")

    if shape == "rectangle":
        rectangle_x = int(input("Enter the x coordinate of rectangle: "))
        rectangle_y = int(input("Enter the y coordinate of rectangle: "))
        rectangle_width = int(input("Enter the width of rectangle: "))
        rectangle_height = int(input("Enter the height of rectangle: "))
        rectangle_color_red = int(input("Enter the value of red color for rectangle: "))
        rectangle_color_green = int(input("Enter the value of green color for rectangle: "))
        rectangle_color_blue = int(input("Enter the value of blue color for rectangle: "))
        rectangle = Rectangle(x=rectangle_x, y=rectangle_y, width=rectangle_width, height=rectangle_height,
                              color=[rectangle_color_red, rectangle_color_green, rectangle_color_blue])
        rectangle.draw(canvas)

    if shape == "square":
        square_x = int(input("Enter the x coordinate of square: "))
        square_y = int(input("Enter the y coordinate of square: "))
        square_side = int(input("Enter the side of square: "))
        square_color_red = int(input("Enter the value of red color for square: "))
        square_color_green = int(input("Enter the value of green color for square: "))
        square_color_blue = int(input("Enter the value of blue color for square: "))
        square = Square(x=square_x, y=square_y, side=square_side, color=[square_color_red, square_color_green,
                                                                         square_color_blue])
        square.draw(canvas)

    if shape == "quit":
        break

canvas.make()
