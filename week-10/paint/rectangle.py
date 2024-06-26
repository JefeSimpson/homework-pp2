import pygame

def main():
    #initializing moment
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    baseLayer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    
    #base poses, so not on the origin, then giving pos when we move using mouse
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            #here we give positions when we click 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]
            #here we end the process
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))

            #here we showing current pos in case when we let the button to remember it
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
        
 
        #draw func
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
             screen.blit(baseLayer, (0, 0))
             r = calculateRect(prevX, prevY, currentX, currentY)
             pygame.draw.rect(screen, (255,255, 255),pygame.Rect(r), 1)
        
        pygame.display.flip()
        clock.tick(60)
        
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

main()
