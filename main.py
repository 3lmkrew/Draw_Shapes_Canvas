# Author: Mason Hernandez (@ 3lmkrew)
# Date: July 18, 2022

from canvas import Canvas
from shapes import Square, Rectengle

# Canvas size inputs
canvas_width = int(input("Enter canvas width:"))
canvas_height = int(input("Enter canvas height:"))

# Canvas background color input
while True:
    canvas_color = input("Enter canvas color (white or black):")
    if canvas_color.lower() == "black" or canvas_color.lower() == "white":
        break
    else:
        print(f"\nPlease try again, chose either black or white. You entered: {canvas_color}")
        continue

# Canvas color selection based on input
color_dic = {"black": [0, 0, 0], "white": [255, 255, 255]}
my_canvas = Canvas(width=canvas_width, height=canvas_height, color=color_dic[canvas_color.lower()])  # Create the canvas

# keep count of square and rectangle objects.
square_count = 0
rectangle_count = 0

while True:
    shape_input = input("What would you like to draw? (Square or Rectangle) Enter quite to quite.")

    # if user selects square object
    if shape_input.lower() == "square":
        square_count += 1
        # square inputs
        square_x = int(input("Enter X placement coordinate of the Square:"))
        square_y = int(input("Enter Y placement coordinate of the Square:"))
        square_side = int(input("Enter the side length of the Square?"))
        # square colors
        red = int(input(f"How much red should the {shape_input.capitalize()} have? (0 to 255)"))
        green = int(input(f"How much green should the {shape_input.capitalize()} have? (0 to 255)"))
        blue = int(input(f"How much blue should the {shape_input.capitalize()} have? (0 to 255)"))
        # creates square based on inputs
        square_one = Square(x=square_x, y=square_y, side=square_side, color=[red, green, blue])
        # draws square onto canvas
        square_one.draw(my_canvas)

    # if user selects rectangle object.
    elif shape_input.lower() == "rectangle":
        rectangle_count += 1
        # rectangle inputs
        rec_x = int(input("Enter X placement coordinate of the Rectangle:"))
        rec_y = int(input("Enter Y placement coordinate of the Rectangle:"))
        rec_with = int(input("Enter the width of the Rectangle:"))
        rec_height = int(input("Enter the height of the Rectangle:"))
        # rectangle colors
        red = int(input(f"How much red should the {shape_input.capitalize()} have? (0 to 255)"))
        green = int(input(f"How much green should the {shape_input.capitalize()} have? (0 to 255)"))
        blue = int(input(f"How much blue should the {shape_input.capitalize()} have? (0 to 255)"))
        # creates rectangle based on inputs
        rectangle_1 = Rectengle(x=rec_x, y=rec_y, width=rec_with, height=rec_height,
                                color=[red, green, blue])  # Create a green rectangle
        # draws rectangle onto canvas
        rectangle_1.draw(my_canvas)

    # if user wants to Quite.
    elif shape_input.lower() == "quite":
        break

    # if user inputs non of the 3 options or has misspelling.
    else:
        print(f"You entered {shape_input}, make sure you type either Square, Rectangle or Quite")
        print("Let's try this again!\n")
        continue


# file path saved location
file_path = "canvas.png"
my_canvas.make(file_path)  # pass save method with path location as arguments

# Completed message
print(f"\n\nYour Canvas has been completed and saved under {file_path}")
print(f"You made {str(square_count)} squares and {str(rectangle_count)} rectangles ")
