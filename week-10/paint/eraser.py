from keyword import iskeyword
import pygame

def main():
    #initializing
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    #giving base pos
    prevX = 0
    prevY = 0

    screen.fill((0, 0, 0))
    
    #bools to use in keys
    isKeyEPressed = False
    isMouseDown = False
    while True:
        
        pressed = pygame.key.get_pressed()
        #giving pos, so the base not be on the origin
        currentX = prevX
        currentY = prevY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            #logic of pressing e to erase and d to draw    
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_e: 
                    isKeyEPressed = True
                if event.key == pygame.K_d: 
                    isKeyEPressed = False

            #Again logic if we click, we draw by the bools, and otherwise don't draw

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    isMouseDown = False


            if event.type == pygame.MOUSEMOTION:
                
                currentX = event.pos[0]
                currentY = event.pos[1]

        #first in case to draw in black(erase in other words)        
        if isKeyEPressed and isMouseDown: 
            pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY))
        #draw func
        if isMouseDown and not isKeyEPressed: 
            pygame.draw.line(screen, (200, 200, 200), (prevX, prevY), (currentX, currentY))

        prevX = currentX
        prevY = currentY

        pygame.display.flip()
        clock.tick(60)

main()