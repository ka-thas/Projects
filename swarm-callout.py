"""
Multi-Agent Task Allocation Simulation

Simulates a swarm of autonomous agents collaborating to solve spatially distributed tasks.
Each task requires multiple agents (Tc) to be within range (Tr) simultaneously to complete.
Agents communicate within radius (Rd) and coordinate to efficiently allocate themselves to tasks.

Study how communication radius affects task completion efficiency in swarm robotics.
"""

import pygame
import numpy as np
import random
import math

# Initialize Pygame
pygame.init()

# Parameters (copied from capacity.py)
num_agents = 20
num_tasks = 3
area_size = 800  # Reduced for better screen fit
Rv = 2  # Reduced speed for better visualization
Tr = 50  # task radius
Tc = 2  # capacity
Rd = 100  # communication radius

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)

class Task:
    def __init__(self):
        self.pos = np.array([random.uniform(Tr, area_size - Tr), 
                            random.uniform(Tr, area_size - Tr)])
        self.agents_in_range = set()
    
    def is_solved(self):
        return len(self.agents_in_range) >= Tc

    def regenerate(self):
        self.agents_in_range.clear()
        self.pos = np.array([random.uniform(Tr, area_size - Tr), 
                            random.uniform(Tr, area_size - Tr)])

    def draw(self, screen):
        # Draw task radius circle
        color = LIGHT_GREEN if self.is_solved() else LIGHT_BLUE
        pygame.draw.circle(screen, color, (int(self.pos[0]), int(self.pos[1])), Tr, 2)
        
        # Draw task center
        center_color = GREEN if self.is_solved() else BLUE
        pygame.draw.circle(screen, center_color, (int(self.pos[0]), int(self.pos[1])), 8)
        
        # Draw agent count
        font = pygame.font.Font(None, 24)
        text = font.render(f"{len(self.agents_in_range)}/{Tc}", True, BLACK)
        screen.blit(text, (int(self.pos[0]) - 15, int(self.pos[1]) - 30))

class Agent:
    def __init__(self):
        self.pos = np.array([random.uniform(0, area_size), random.uniform(0, area_size)])
        self.angle = random.random() * 2 * math.pi
        self.speed = Rv
        self.locked = False

    def move(self, tasks, agents):
        # Clear previous task associations
        for task in tasks:
            if self in task.agents_in_range:
                task.agents_in_range.discard(self)
        
        # Check if agent is within any task radius
        for task in tasks:
            if math.dist(self.pos, task.pos) < Tr:
                self.locked = True
                task.agents_in_range.add(self)
                return

        self.locked = False

        # Communication behavior - move towards locked agents
        for agent in agents:
            if agent != self and agent.locked and math.dist(self.pos, agent.pos) < Rd:
                self.angle = math.atan2(agent.pos[1] - self.pos[1], agent.pos[0] - self.pos[0])
                break

        # Move
        self.pos += self.speed * np.array([math.cos(self.angle), math.sin(self.angle)])

        # Boundary handling
        if self.pos[0] < 0 or self.pos[0] > area_size or self.pos[1] < 0 or self.pos[1] > area_size:
            self.angle = random.random() * 2 * math.pi
            self.pos = np.clip(self.pos, 0, area_size)

    def draw(self, screen, agents):
        # Draw communication radius for unlocked agents
        if not self.locked:
            pygame.draw.circle(screen, GRAY, (int(self.pos[0]), int(self.pos[1])), Rd, 1)
        
        # Draw agent
        color = RED if self.locked else YELLOW
        pygame.draw.circle(screen, color, (int(self.pos[0]), int(self.pos[1])), 6)
        
        # Draw direction indicator
        end_pos = self.pos + 15 * np.array([math.cos(self.angle), math.sin(self.angle)])
        pygame.draw.line(screen, BLACK, self.pos, end_pos, 2)

def main():
    # Setup display
    screen = pygame.display.set_mode((area_size + 200, area_size + 100))
    pygame.display.set_caption("Agent-Task Simulation")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    
    # Initialize agents and tasks
    agents = [Agent() for _ in range(num_agents)]
    tasks = [Task() for _ in range(num_tasks)]
    
    solved_count = 0
    iteration = 0
    running = True
    paused = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    # Reset simulation
                    agents = [Agent() for _ in range(num_agents)]
                    tasks = [Task() for _ in range(num_tasks)]
                    solved_count = 0
                    iteration = 0
        
        if not paused:
            # Update simulation
            for agent in agents:
                agent.move(tasks, agents)
            
            # Check for solved tasks
            for task in tasks:
                if task.is_solved():
                    solved_count += 1
                    task.regenerate()
            
            iteration += 1
        
        # Draw everything
        screen.fill(WHITE)
        
        # Draw tasks first (so they appear behind agents)
        for task in tasks:
            task.draw(screen)
        
        # Draw agents
        for agent in agents:
            agent.draw(screen, agents)
        
        # Draw statistics
        stats_y = area_size + 10
        text1 = font.render(f"Iteration: {iteration}", True, BLACK)
        text2 = font.render(f"Tasks Solved: {solved_count}", True, BLACK)
        text3 = font.render(f"Agents: {num_agents}, Tasks: {num_tasks}, Capacity: {Tc}", True, BLACK)
        text4 = font.render("SPACE: Pause/Resume, R: Reset", True, BLACK)
        
        screen.blit(text1, (10, stats_y))
        screen.blit(text2, (200, stats_y))
        screen.blit(text3, (10, stats_y + 30))
        screen.blit(text4, (10, stats_y + 60))
        
        if paused:
            pause_text = font.render("PAUSED", True, RED)
            screen.blit(pause_text, (area_size - 100, stats_y))
        
        # Draw legend
        legend_x = area_size + 10
        legend_items = [
            ("Yellow: Free Agent", YELLOW),
            ("Red: Locked Agent", RED),
            ("Blue: Active Task", BLUE),
            ("Green: Solved Task", GREEN),
            ("Gray: Comm. Radius", GRAY)
        ]
        
        for i, (text, color) in enumerate(legend_items):
            y_pos = 10 + i * 25
            pygame.draw.circle(screen, color, (legend_x, y_pos + 10), 8)
            legend_text = pygame.font.Font(None, 20).render(text, True, BLACK)
            screen.blit(legend_text, (legend_x + 20, y_pos))
        
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()