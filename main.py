import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainbow Fireworks Show")

# Colors
BLACK = (0, 0, 0)
COLORS = [
    (255, 0, 0),    # Red
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (75, 0, 130),   # Indigo
    (238, 130, 238) # Violet
]

# Firework class
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(COLORS)
        self.particles = []
        self.exploded = False
        self.radius = 0

    def explode(self):
        for _ in range(100):  # Create 100 particles
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 5)
            self.particles.append([self.x, self.y, math.cos(angle) * speed, math.sin(angle) * speed])
        self.exploded = True

    def update(self):
        if not self.exploded:
            self.y -= 5  # Move firework upwards
            if self.y <= random.randint(100, 300):  # Random explosion height
                self.explode()
        else:
            for particle in self.particles:
                particle[0] += particle[2]  # Update x position
                particle[1] += particle[3]  # Update y position
                particle[3] += 0.1  # Gravity effect

    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)
        else:
            for particle in self.particles:
                pygame.draw.circle(screen, self.color, (int(particle[0]), int(particle[1])), 2)

# Main loop
fireworks = []
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            fireworks.append(Firework(x, y))

    for firework in fireworks:
        firework.update()
        firework.draw()

    # Remove off-screen fireworks
    fireworks = [f for f in fireworks if not (f.exploded and all(p[1] > HEIGHT for p in f.particles))]

    pygame.display.update()
    clock.tick(30)

pygame.quit()
