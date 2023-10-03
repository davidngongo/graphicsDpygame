# import pygame
# import sys

# #initialize pygame
# pygame.init()
# #pygame.quit()

# #set the width and the height of the screen

# width = 640
# height = 480

# # create the screen

# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Lab1: computer graphics")

# #set the background color (RGB)

# background_color = (255, 255, 255)

# #set th color (RGB) for the line

# line_color = (0, 0, 0)

# #set the starting and the ending point of the line

# start_pos = (100, 100)
# end_pos = (500, 400)

# #set the line thickness

# line_thickness = 3

# # Create a clock object to control the frame rate


# #Game loop

# while True:
#     #we clear the screen with the background color
#     screen.fill(background_color)
    
#     #Draw the line on the screen
    
#     pygame.draw.line(screen, line_color, start_pos, )
    
#     #update the screen
    
#     pygame.display.flip()
    
#     #Event Handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()




import pygame
import sys

# Initialize pygame
pygame.init()

# Set the width and the height of the screen
width = 640
height = 480

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lab1: computer graphics")

# Set the background color (RGB)
background_color = (255, 255, 255)

# Set the color (RGB) for the line
line_color = (0, 0, 0)

# Set the starting and the ending point of the line
start_pos = (100, 100)
end_pos = (500, 400)

# Set the line thickness
line_thickness = 3

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Clear the screen with the background color
    screen.fill(background_color)

    # Draw the line on the screen
    pygame.draw.line(screen, line_color, start_pos, end_pos, line_thickness)

    # Update the screen
    pygame.display.flip()

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Set running to False to exit the loop

    # Control the frame rate
    clock.tick(60)  # You can adjust the frame rate (e.g., 60 frames per second)

# Quit pygame and exit the program
pygame.quit()
sys.exit()
