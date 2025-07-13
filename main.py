import canvas
import shapes

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color code and prompt for color:
colors={'white':(255,255,255),'black':(0,0,0)}
user_color = input("Enter canvas color (black or white): ")
canvas = canvas.Canvas(width=canvas_width, height=canvas_height,color=colors[user_color])

while True:
    user_shape = input("What would you like to draw? Enter quit to quit. ")
    if user_shape.lower() == 'square':
        square_x = int(input("Enter square x: "))
        square_y = int(input("Enter square y: "))
        square_side= int(input("Enter square size: "))
        square_R = int(input("Enter how much red should the square have?"))
        square_G= int(input("Enter how much green should the square have?"))
        square_B = int(input("Enter how much green should the square have?"))

        squ = shapes.Square(square_x,square_y,square_side,color=(square_R,square_G,square_B))
        squ.draw(canvas)
    elif user_shape == 'rectangle':
        rect_x = int(input("Enter rectangle x: "))
        rect_y = int(input("Enter rectangle y: "))
        rect_width = int(input("Enter width size: "))
        rect_height = int(input("Enter height size: "))
        rect_R = int(input("Enter how much red should the rectangle have?"))
        rect_G = int(input("Enter how much green should the rectangle have?"))
        rect_B = int(input("Enter how much green should the rectangle have?"))
        rect = shapes.Rectangle(x=rect_x,y=rect_y,width=rect_width,height=rect_height,color=(rect_R,rect_G,rect_B))
        rect.draw(canvas)

    elif user_shape == 'quit':
        break

canvas.make("canvas.png")