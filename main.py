import pygame
import math
import random

# Initialise the pygame module
pygame.init()
WIDTH, HEIGHT = 800, 500  # Dimension of the Game Screen
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!!!")

# Colors Used 
WHITE = (255,255,255)
BLACK = (0,0,0)

# Button Variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH-(RADIUS*2+GAP)*13)/2) # start x position
starty = 400 # start y position
A = 65

for i in range(26):
  # Creating coordinates for the letters
  x = startx + GAP*2 + ((RADIUS*2 + GAP)* (i%13))
  y = starty + ((i//13)* (GAP+RADIUS*2))
  letters.append([x,y, chr(A+i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 60)

# Loading the images
images = []
for i in range(7):
  image = pygame.image.load("hangman"+str(i)+ ".png")
  images.append(image)

# Game variables
hangman_stats = 0
words = ["CODING","GITHUB","REPLIT", "PYTHON", "HANGMAN","COMPUTER", "KEYBOARD", "MOBILE", "DEVELOPER"]
word = random.choice(words)
guessed = []

# Draw Function
def draw():
   # Update and refresh the display
  win.fill(WHITE)

  # Draw Title
  text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
  win.blit(text, (WIDTH/2- text.get_width()/2, 20))

  # Draw Word Spaces
  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word += "_ "

  # Draw Word Update
  text = WORD_FONT.render(display_word, 1 , BLACK)
  win.blit(text,(400,200))

  # Draw Buttons
  for letter in letters:
    x, y, ltr, visible = letter
    if visible:
      pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3 )
      text = LETTER_FONT.render(ltr, 1 , BLACK)
      win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

  win.blit(images[hangman_stats], (100,100))
  pygame.display.update()

# Display Messsage Function
def display_message(message):
  pygame.time.delay(1000) # Time Delay before the result
  win.fill(WHITE)
  text = WORD_FONT.render(message, 1, BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2,HEIGHT/2 - text.get_height()/2)) # Position of the result
  pygame.display.update()
  pygame.time.delay(3000) # Time Delay after the result


# Game Loop Setup 
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
  clock.tick(FPS) # Clock Speed/ Refresh Rate

  for event in pygame.event.get():

    # Check for the quit button
    if event.type == pygame.QUIT:
      run = False

    # Check for the mouse button
    if event.type == pygame.MOUSEBUTTONDOWN:
      m_x,m_y = pygame.mouse.get_pos()
      for letter in letters:
        x,y,ltr, visible = letter
        dis = math.sqrt((x-m_x)**2+(y-m_y)**2)
        # Check if the button is clicked inside the radius
        if dis < RADIUS:
          letter[3] = False
          guessed.append(ltr)
          # Update the hangman picture
          if ltr not in word:
            hangman_stats += 1

    # Draw the updated screen
    draw()
  
  # Check for the results
  won = True
  for letter in word:
    if letter not in guessed:
      won = False
      break
  
  # Criteria for Win
  if won:
    display_message("YOU WON!")

  # Criteria for Lost
  if hangman_stats == 6:
    display_message("YOU LOST!")
    break

pygame.quit()