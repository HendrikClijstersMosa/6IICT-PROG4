import pygame
from particle import *

class Storm:
    # Create storm
    def __init__(self, n_particles, max_speed, width, height):
        self.width = width
        self.height = height
        self.particles = self.setup(n_particles, max_speed)

    # Simulation loop
    def loop(self):
        running = True
        while running:
            interval = self.clock.tick(120)
            running = self.handle_events()
            self.update_particles(interval) # Handles updating and resetting of particles
            self.update_screen()
        pygame.quit()

    # Handles button presses and clicks, can be expanded upon
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    # Method to fill list with different particle types
    def setup(self,n_particles, max_speed):
        pygame.init()
        pygame.display.set_caption("Fire Storm Simulation")
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        
        list = []
        for key, value in n_particles.items():
            for _ in range(value):
                list.append(key(max_speed))
        return list

    # Update elements in list of storm
    def update_particles(self, interval):
        for particle in self.particles:
            particle.update(interval)
            particle.reset()

    # Fill the screen with all different particles
    def update_screen(self):
        self.screen.fill((0,0,0))
        for particle in self.particles:
            x_co, y_co = particle.pos_x*self.width/2 + self.width/2, particle.pos_y*self.height/2 + self.height/2
            pygame.draw.circle(self.screen, particle.color, [x_co,y_co], 10)
        pygame.display.update()

# Executes on running of file  
if __name__ == '__main__':
    """ Use for testing base implementation and version 2 """
    storm = Storm({Particle:20}, 0.001, 600, 600)

    """ Use for testing version 3 """
    # storm = Storm({Boring:20}, 0.001, 600, 600)

    """ Use for testing version 4 - change number of particles as you please """
    # storm = Storm({Boring:0, Bouncing:20}, 0.001, 600, 600)

    """ Use for testing version 5 - change number of particles as you please """
    # storm = Storm({Boring:0, Bouncing:0, Spinning: 20}, 0.001, 600, 600)
    
    """ Use for testing version 6 - change number of particles as you please """
    # storm = Storm({Boring:20, Bouncing:20, Spinning:20, Gravitational:20}, 0.001, 600, 600)
    
    storm.loop()


    


