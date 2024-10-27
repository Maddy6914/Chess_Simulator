# two player Chess in python with Pygame
#set up he var ,img &game loop


import pygame

pygame.init()

WIDTH = 1000

HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player  Chess!')
font = pygame.font.Font('freesansbold.ttf', 28)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps=60

#game var and img
white_pieces =['rook','knight','bishop','king','queen','bishop','knight','rook',
               'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

white_locations =[(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                  (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]


black_pieces =['rook','knight','bishop','king','queen','bishop','knight','rook',
               'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

black_locations =[(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                  (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

captured_pieces_white =[]
captured_pieces_black =[]
# 0-whites turn no selection: 1-whites turn piece selection:2-black turn no selection: 3-black turn piece selected
turn_step = 0
selection = 100
valid_moves =[]

#load in a game pieces images('king','queen','bishop','knight','rook','pawn') X 2

black_queen=pygame.image.load('img/black_queen.png')
black_queen=pygame.transform.scale(black_queen, (80,80))
black_queen_small=pygame.transform.scale(black_queen, (45,45))

black_king=pygame.image.load('img/black_king.png')
black_king=pygame.transform.scale(black_king, (80,80))
black_king_small=pygame.transform.scale(black_king, (45,45))

black_rook=pygame.image.load('img/black_rook.png')
black_rook=pygame.transform.scale(black_rook, (80,80))
black_rook_small=pygame.transform.scale(black_rook, (45,45))

black_bishop=pygame.image.load('img/black_bishop.png')
black_bishop=pygame.transform.scale(black_bishop, (80,80))
black_bishop_small=pygame.transform.scale(black_bishop, (45,45))

black_knight=pygame.image.load('img/black_knight.png')
black_knight=pygame.transform.scale(black_knight, (80,80))
black_knight_small=pygame.transform.scale(black_knight, (45,45))

black_pawn=pygame.image.load('img/black_pawn.png')
black_pawn=pygame.transform.scale(black_pawn, (65,65))
black_pawn_small=pygame.transform.scale(black_pawn, (45,45))
#-------------------white_pieces-----------------------------------
white_queen=pygame.image.load('img/white_queen.png')
white_queen=pygame.transform.scale(white_queen, (80,80))
white_queen_small=pygame.transform.scale(white_queen, (45,45))

white_king=pygame.image.load('img/white_king.png')
white_king=pygame.transform.scale(white_king, (80,80))
white_king_small=pygame.transform.scale(white_king, (45,45))

white_rook=pygame.image.load('img/white_rook.png')
white_rook=pygame.transform.scale(white_rook, (80,80))
white_rook_small=pygame.transform.scale(white_rook, (45,45))

white_bishop=pygame.image.load('img/white_bishop.png')
white_bishop=pygame.transform.scale(white_bishop, (80,80))
white_bishop_small=pygame.transform.scale(white_bishop, (45,45))

white_knight=pygame.image.load('img/white_knight.png')
white_knight=pygame.transform.scale(white_knight, (80,80))
white_knight_small=pygame.transform.scale(white_knight, (45,45))

white_pawn=pygame.image.load('img/white_pawn.png')
white_pawn=pygame.transform.scale(white_pawn, (65,65))
white_pawn_small=pygame.transform.scale(white_pawn, (45,45))

#list of pieces
white_images =[white_queen, white_king, white_bishop, white_knight, white_rook, white_pawn]
small_white_images =[white_queen_small, white_king_small, white_bishop_small, white_knight_small, white_rook_small, white_pawn_small]

black_images =[black_queen, black_king, black_bishop, black_knight, black_rook, black_pawn]
small_black_images =[black_queen_small, black_king_small, black_bishop_small, black_knight_small, black_rook_small, black_pawn_small]

pieces_list =['queen', 'king', 'bishop', 'knight', 'rook', 'pawn']

#check variables // flashing counter






#draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'dark grey', [600 - (column*200), (row * 100), 100, 100])
        else:
            pygame.draw.rect(screen, 'dark grey', [700 - (column*200), (row * 100), 100, 100])
        pygame.draw.rect(screen, 'gold', [0,800, WIDTH, 100])
        pygame.draw.rect(screen, 'red' ,[0,800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold' ,[800,0, 200, HEIGHT])
        pygame.draw.rect(screen, 'red' ,[800,0, 200, HEIGHT], 5)
        status_text=['White: Select a Piece to Move !','White: Select a Destionation!',
                     'Black: Select a Piece to Move !','Black: Select a Destionation!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))  
        for i in range (9):
            pygame.draw.line(screen, "black", (0, 100 * i),(800, 100 * i), 2) 
            pygame.draw.line(screen, "black", (100 * i, 0),(100 * i, 800), 2)    


#draw piecies onto a board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = pieces_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn' :
         screen.blit(white_pawn, (white_locations[i][0] * 100 + 22 , white_locations[i][1] *100 + 30))
        else :
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10 , white_locations[i][1] *100 + 10))
        
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen,'green', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 100 ,100], 2)

    for i in range(len(black_pieces)):
        index = pieces_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn' :
         screen.blit(black_pawn, (black_locations[i][0] * 100 + 22 , black_locations[i][1] * 100 + 30))
        else :
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10 , black_locations[i][1] *100 + 10))
       
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen,'green', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100 ,100], 2)




#function to check  all piecies valid options on the board
def check_options(pieces,locations,turn):
    moves_list =[]
    all_moves_list=[]
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location , turn)
        elif piece == 'rook':
            moves_list =check_rook(location , turn)
        elif piece == 'knight':
            moves_list =check_knight(location , turn)
        elif piece == 'bishop':
            moves_list =check_bishop(location , turn)
        elif piece == 'queen':
            moves_list =check_queen(location , turn)
        elif piece == 'king':
            moves_list =check_king(location , turn)
        all_moves_list.append(moves_list)
        
    return all_moves_list


#Check Rook moves
def check_rook(position,color):
    



#Check Knight moves
def check_knight(position,color):
    pass



#Check bishop moves
def check_bishop(position,color):
    pass



#Check Queen moves
def check_queen(position,color):
    pass



#Check King moves
def check_king(position,color):
    pass




# Check valid pawn moves
def check_pawn(position, color):
    moves_list=[]
    if color == 'white':
        if (position[0], position[1]+ 1) not in white_locations and  \
            (position[0], position[1]+1) not in black_locations and position[1] < 7:
                moves_list.append((position[0],position[1]+ 1))      
        if (position[0], position[1]+ 2) not in white_locations and  \
            (position[0], position[1]+2) not in black_locations and position[1] == 1:
                moves_list.append((position[0],position[1]+ 2))              
        if(position[0]+1, position[1]+1) in black_locations :
            moves_list.append((position[0]+1, position[1]+1))       
        if(position[0]-1, position[1]+1) in black_locations :
            moves_list.append((position[0]-1, position[1]+1))
    else:
        if (position[0], position[1]- 1) not in white_locations and  \
            (position[0], position[1]-1) not in black_locations and position[1] > 0 :
                moves_list.append((position[0],position[1]- 1))
        if (position[0], position[1]- 2) not in white_locations and  \
            (position[0], position[1]-2) not in black_locations and position[1] == 6:
                moves_list.append((position[0],position[1]- 2))     
        if(position[0]+1, position[1]-1) in white_locations :
            moves_list.append((position[0]+1, position[1]-1))    
        if(position[0]-1, position[1]-1) in white_locations :
            moves_list.append((position[0]-1, position[1]-1))
    return moves_list
            
            
            
#Check for valid moves for the selected pieces
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options            
            
                    
#Draw valid moves on the screen 
def draw_valid(moves):
    if turn_step < 2:
        color='green'
    else:
        color='green'
    for i in range((len(moves))):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50,moves[i][1] * 100 + 50),10)
        


#main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')

run = True

while run:
    timer.tick(fps)
    screen.fill('YELLOW')
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves= check_valid_moves()
        draw_valid(valid_moves)
    
    
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 :
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <=1:
                if click_coords in white_locations :
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step=1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step=2
                    selection = 100
                    valid_moves=[]
                
            if turn_step > 1:
                 if click_coords in black_locations :
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step=3
                 if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step=0
                    selection =100
                    valid_moves=[]
                
                
    pygame.display.flip()
pygame.quit()