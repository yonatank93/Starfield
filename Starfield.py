import pygame
import numpy as np
import time, copy

class Star:
       
    def __init__(self, width:int, height:int, nstars:int, speed:float):
        """
        x goes from 0-width
        y goes from 0-width
        z goes from 0-width/2, it encodes depth data
        r goes from 0-16, it tells the size of circle from z value
        """
        self.width = width
        self.height = height
        self.nstars = nstars
        self.speed = speed
        
        # Create space
        pygame.init()
        self.space = pygame.display.set_mode((width, height))
        
        # Color data
        self.white = (255, 255, 255) #To draw stars
        self.black = (0, 0, 0) #To delete stars
        
        # Stars data
        self.x = np.random.randint(0, self.width, nstars)
        self.y = np.random.randint(0, self.height, nstars)
        self.z = np.random.randint(0, int(self.width/2), nstars)
        
        # Set px, py, pz to zeros
        self.px = np.zeros(nstars).astype(int)
        self.py = np.zeros(nstars).astype(int)
        self.pz = np.zeros(nstars).astype(int)
        
    def draw_stars(self):
        # Delete previous positions
        pr = (self.pz/(int(self.width/2)) * 4).astype(int)
        for xx, yy, rr in zip(self.px, self.py, pr):
            pygame.draw.circle(self.space, self.black, (xx, yy), rr)

        # Draw current positions
        r = (self.z/(int(self.width/2)) * 4).astype(int)
        for xx, yy, rr in zip(self.x, self.y, r):
            pygame.draw.circle(self.space, self.white, (xx, yy), rr)
        
    def update(self):
        """ Stars move radially outward from the center.
        So we need to shift the coord (0, 0) to the center.
        """
        # Save previous data
        self.px = copy.copy(self.x)
        self.py = copy.copy(self.y)
        self.pz = copy.copy(self.z)
        
        # Update stars' positions
        angle = self.get_angle(self.x-self.width/2, self.y-self.height/2)
        self.x = (self.x + self.speed*np.cos(angle)).astype(int)
        self.y = (self.y + self.speed*np.sin(angle)).astype(int)
        self.z += self.speed
        
        self.replace_stars()
            
    def show(self):
        time.sleep(1/self.speed)
        pygame.display.update()
        
    @staticmethod
    def get_angle(xsh, ysh):
        return np.angle(xsh+ysh*1j)
    
    def replace_stars(self):        
        # Get stars out of frame
        idxx1 = np.where(self.x<=0)[0]
        idxx2 = np.where(self.x>=self.width)[0]
        idxy1 = np.where(self.y<=0)[0]
        idxy2 = np.where(self.y>=self.height)[0]
        idx = np.unique(np.concatenate((idxx1, idxx2, idxy1, idxy2)))
                
        self.x[idx] = np.random.randint(0, self.width, len(idx))
        self.y[idx] = np.random.randint(0, self.height, len(idx))
        self.z[idx] = np.random.randint(0, int(self.width/2), len(idx))
        
    def run(self, duration:float=60):
        start = time.perf_counter()
        tdiff = 0
        while tdiff<duration:
            mystars.draw_stars()
            mystars.show()
            mystars.update()
            tdiff = time.perf_counter() - start
            
if __name__=="__main__":
    mystars = Star(1920, 1080, 50, 30)
    mystars.run()
