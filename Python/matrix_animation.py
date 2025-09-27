# matrix_animation.py
# Upward Matrix-style digital rain with readable title

import pygame
import random
import pandas as pd

# -------------------------------
# 1️⃣ Load CSV/Excel
# -------------------------------
file_path = r"C:\Users\jaime\OneDrive\Desktop\Personal Projects\global_cybersecurity_threats.csv"

if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

df.columns = df.columns.str.strip().str.replace(' ', '_')

chars = df['Number_of_Affected_Users'].astype(str).tolist()
matrix_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
chars.extend(matrix_chars)

# -------------------------------
# 2️⃣ Pygame Setup
# -------------------------------
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cybersecurity Matrix Digital Rain")
clock = pygame.time.Clock()

# -------------------------------
# 3️⃣ Colors & Font
# -------------------------------
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LEAD_GREEN = (180, 255, 180)
font_size = 24
font = pygame.font.SysFont("Consolas", font_size)
title_font = pygame.font.SysFont("Consolas", 32, bold=True)

# -------------------------------
# 4️⃣ Columns & Drops (upwards)
# -------------------------------
columns = int(width / font_size)
drops = [random.randint(0, height // font_size) for _ in range(columns)]
speeds = [random.uniform(0.5, 1.5) for _ in range(columns)]  # slower speeds

# -------------------------------
# 5️⃣ Animation Loop
# -------------------------------
running = True
while running:
    s = pygame.Surface((width, height))
    s.set_alpha(50)
    s.fill(BLACK)
    screen.blit(s, (0, 0))

    # Title at top
    title_render = title_font.render("Cybersecurity Matrix", True, GREEN)
    title_rect = title_render.get_rect(center=(width // 2, 30))  # 30 pixels from top
    screen.blit(title_render, title_rect)

    for i in range(columns):
        char = random.choice(chars)
        color = LEAD_GREEN if random.random() > 0.85 else GREEN
        char_render = font.render(char, True, color)
        screen.blit(char_render, (i * font_size, drops[i] * font_size))

        # Move upward
        drops[i] -= speeds[i]
        if drops[i] * font_size < 0 or random.random() > 0.98:
            drops[i] = height // font_size

    pygame.display.flip()
    clock.tick(30)  # adjust FPS if you want even slower

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
