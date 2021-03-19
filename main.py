import pygame

# Initialise the pygame module
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!!!")
WHITE = (255,255,255)
BLACK = (0,0,0)

# Button Variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH-(RADIUS*2+GAP)*13)/2)
starty = 400

for i in range(26):
  x = startx + GAP*2 + ((RADIUS*2 + GAP)* (i%13))
  y = starty + ((i//13)* (GAP+RADIUS*2))
  letters.append([x,y])

# Load images
images = []
for i in range(7):
  image = pygame.image.load("hangman"+str(i)+ ".png")
  images.append(image)

# Game variables
hangman_stats = 0

def draw():
   # Update and refresh the display

  win.fill(WHITE)

  # Draw Buttons
  for letter in letters:
    x,y = letter
    pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3 )

  win.blit(images[hangman_stats], (100,50))
  pygame.display.update()



# Setup game loop 
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
  clock.tick(FPS)

  draw()

  for event in pygame.event.get():

    # Check for the quit button
    if event.type == pygame.QUIT:
      run = False

    # Check for the mouse button
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      print(pos)

pygame.quit()