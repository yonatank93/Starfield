import pygame
import numpy as np
import time, copy

# from Starfield import Star
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
        self.star_color = (255, 255, 255) #To draw stars
        self.space_color = (0, 0, 0) #To delete stars
        self.tail_color = (255, 255, 255, 50) #To draw tails
        
        # Stars data
        self.x = np.random.randint(0, self.width, nstars)
        self.y = np.random.randint(0, self.height, nstars)
        self.z = np.random.randint(0, int(self.width/2), nstars)
        
        # Set px, py, pz to zeros
        self.px = np.zeros(nstars).astype(int)
        self.py = np.zeros(nstars).astype(int)
        self.pz = np.zeros(nstars).astype(int)
        
        # Set previous px, py, pz to zeros
        self.ppx = np.zeros(nstars).astype(int)
        self.ppy = np.zeros(nstars).astype(int)
        self.ppz = np.zeros(nstars).astype(int)
        
    def draw_stars(self):
        # Delete previous positions
        pr = (self.pz/(int(self.width/2)) * 4).astype(int)
        for xx, yy, rr in zip(self.px, self.py, pr):
            pygame.draw.circle(self.space, self.space_color, (xx, yy), rr)

        # Draw current positions
        r = (self.z/(int(self.width/2)) * 4).astype(int)
        for xx, yy, rr in zip(self.x, self.y, r):
            pygame.draw.circle(self.space, self.star_color, (xx, yy), rr)
            
    def draw_tail(self):
        # Delete previous tail
        pr = (self.pz/(int(self.width/2)) * 4).astype(int)
        for x0, y0, x1, y1, rr in zip(self.ppx, self.ppy, self.px, self.py, pr):
            pygame.draw.line(self.space, self.space_color, (x0, y0), (x1, y1), rr)

        # Draw current tail
        r = (self.z/(int(self.width/2)) * 4).astype(int)
        for x0, y0, x1, y1, rr in zip(self.px, self.py, self.x, self.y, r):
            if 0<x1<self.width and 0<y1<self.height:
                pygame.draw.line(self.space, self.tail_color, (x0, y0), (x1, y1), rr)
        
    def update(self):
        """ Stars move radially outward from the center.
        So we need to shift the coord (0, 0) to the center.
        """
        # Save previous previous data
        self.ppx = copy.copy(self.px)
        self.ppy = copy.copy(self.py)
        self.ppz = copy.copy(self.pz)
        
        # Save previous data
        self.px = copy.copy(self.x)
        self.py = copy.copy(self.y)
        self.pz = copy.copy(self.z)
        
        # Update stars' positions
        angle = self.get_angle(self.x-self.width/2, self.y-self.height/2)
        self.x = np.round(self.x + self.speed*np.cos(angle)).astype(int)
        self.y = np.round(self.y + self.speed*np.sin(angle)).astype(int)
        self.z += self.speed
            
    def show(self):
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
        
    def run(self, duration:float=60, show_tail=False):
        start = time.perf_counter()
        tdiff = 0
        while tdiff<duration:
            if show_tail:
                self.draw_tail()

            self.replace_stars()
            self.draw_stars()
            self.update()
            self.show()
            tdiff = time.perf_counter() - start
            
if __name__=="__main__":
    mystars = Star(800, 800, 50, 30)
    mystars.run()
