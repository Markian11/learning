import pygame

# Initialize pygame and create the game window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Angry Birds")

# Load the bird and pig sprites
bird_image = pygame.image.load("bird.png")
pig_image = pygame.image.load("pig.png")

# Create rectangles for the bird and pig sprites
bird_rect = bird_image.get_rect()
pig_rect = pig_image.get_rect()

# Position the pig in the middle of the screen
pig_rect.x = 350
pig_rect.y = 250

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the bird using the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bird_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        bird_rect.x += 5
    if keys[pygame.K_UP]:
        bird_rect.y -= 5
    if keys[pygame.K_DOWN]:
        bird_rect.y += 5
    
    # Check for collision between the bird and pig
    if bird_rect.colliderect(pig_rect):
        print("Hit the pig!")
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Draw the bird and pig sprites
    screen.blit(bird_image, bird_rect)
    screen.blit(pig_image, pig_rect)
    
    pygame.display.flip()
    
# Quit pygame
pygame.quit()
