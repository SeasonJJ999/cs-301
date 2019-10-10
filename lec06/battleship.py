def draw_map(x,y,width,height,symbol):

    print(('.'*width+'\n')*y)
    print('.'*(x)+symbol+'.'*(width-x-1))
    print(('.'*width+'\n')*(height-y-1))

def is_hit(x,y):
    ship1_x = 5
    ship1_y = 4
    ship2_x = 8
    ship2_y = 8
    return (x == ship1_x and y == ship1_y) or (x == ship2_x and x == ship2_y)

def guess(width,weight):   
    x = int(input('Please input an integer between 0 and '+str(width-1)+':\n'))
    y = int(input('Please input an integer between 0 and '+str(height-1)+':\n'))
    hit = is_hit(x,y)
    print("Hit?" + str(hit))
    symbol = str(int(hit))
    draw_map(x,y,width,weight,symbol)
    
width = 10
height = 10
guess(width, height)








