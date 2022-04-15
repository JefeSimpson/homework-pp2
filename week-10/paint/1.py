import pygame

def main():
    #initializing pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    

    prevX = 0
    prevY = 0

    screen.fill((0, 0, 0))
    
    isMouseDown = False
    while True:
        
        pressed = pygame.key.get_pressed()
        #just in term prevs don't be zero
        currentX = prevX
        currentY = prevY
        #event has logic, when u click and hold the left mouse button draging, afterwads let it and we remember stop with end pos 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    isMouseDown = False


            if event.type == pygame.MOUSEMOTION:
                currentX = event.pos[0]
                currentY = event.pos[1]
        #here we draw, when we click and hold the left button of the mouse        
        if isMouseDown: 
            pygame.draw.line(screen, (200, 200, 200), (prevX, prevY), (currentX, currentY))

        #to make sure last position become prevs
        prevX = currentX
        prevY = currentY

        pygame.display.flip()
        clock.tick(60)

main()