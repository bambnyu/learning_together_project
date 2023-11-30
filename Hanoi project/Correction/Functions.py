#### global variables
nb_disk = int(input("Enter the number of disks: "))
move_list = []
limit_move = (2 ** nb_disk - 1) * 2
nb_move = 0




#### Auxilliary  functions

def towers_initialisation():
    '''
    Board initialisation
    I: none
    O: list of lists with number of disks disks on the first tower
    '''
    global nb_disk
    towers = [[], [], []] # we always have 3 towers so we can hardcode it as a list of of 3 lists
    # we fill the first tower (from the biggest to the smallest)
    for i in range(nb_disk, 0, -1): 
        towers[0].append(i)
    return towers



def is_valid_move(towers , source, destination):
    ''' 
    Verify if the move is valid
    I: the towers, the source tower and the destination tower of the move
    O: Bool, True if the move is valid, False otherwise
    '''
    # check if the towwer of destination is empty as we can move any disk to an empty tower
    
    if towers[destination] == [] and towers[source] != []:
        return True
    # check if the tower of source is empty as we can't move any disk from an empty tower
    if towers[source] == []:
        return False
    # check if the disk of source is bigger than the disk of destination as we can't move a bigger disk on a smaller one
    elif towers[source][-1] > towers[destination][-1]:
        return False
    if (source>2 or source<0) or (destination>2 or destination<0):
        return False
    else:
        return True
    
    
def move_disk(towers, source, destination):
    ''' 
    Move a disk from a tower to another if the move is valid else ask the user to enter a new move
    I: the towers, the source tower and the destination tower of the move
    O: the towers
    '''
    global nb_move
    while not is_valid_move(towers, source, destination): # we continue to ask the user to enter a move until he does enter a valid one
        print("Invalid move")
        source = int(input("Enter the source tower: "))
        destination = int(input("Enter the destination tower: "))
    disk = towers[source].pop() # we remove the disk from the source tower
    towers[destination].append(disk) # we add the disk to the destination tower
    
    nb_move += 1 # we increment the number of moves
    return towers


def is_finished(towers):
    ''' 
    check if the game is finished
    I: the towers
    O: Bool, True if the game is finished, False otherwise
    '''
    if towers[0] == [] and towers[1] == []: # if the first and the second tower are empty then the game is finished
        return True
    else:
        return False
    




#### Automatic resolution functions


##### Recursive resolution
def tower_of_hanoi_recursive(n, towers, source=0, auxiliary=1, destination=2):
    ''' 
    Resolve the game recursively
    I: the number of disks, the towers, the source tower, the auxiliary tower and the destination tower
    O: none
    '''
    if n == 1:
        # Move the top disk from the source tower to the destination tower
        move_disk(towers, source, destination)
        display_towers_terminal1(towers,)
    else:
        # Move n-1 disks from the source tower to the auxiliary tower using the destination tower
        tower_of_hanoi_recursive(n - 1, towers, source, destination, auxiliary)

        # Move the largest disk from the source tower to the destination tower
        move_disk(towers, source, destination)
        display_towers_terminal1(towers,)
        
        # Move the n-1 disks from the auxiliary tower to the destination tower using the source tower
        tower_of_hanoi_recursive(n - 1, towers, auxiliary, source, destination)




##### Iterative resolution
def tower_of_hanoi_iterative(towers):
    ''' 
    Resolve the Tower of Hanoi problem iteratively
    I: the towers
    O: none
    '''
    global nb_disk
    
    num_moves = 0 # number of moves
    total_moves = 2**nb_disk - 1 # total number of moves to solve the problem
    source, auxiliary, destination = 0, 1, 2 # towers indexes

    if nb_disk % 2 == 0: # if the number of disks is even then we swap the auxiliary and the destination towers
        auxiliary, destination = destination, auxiliary

    while num_moves < total_moves: # we continue to move the disks until the game is finished
        if num_moves % 3 == 0:
            check(towers, source, destination)
        elif num_moves % 3 == 1: 
            check(towers, source, auxiliary)
        else:
            check(towers, auxiliary, destination)
        num_moves += 1

def check(towers, source, destination):
    ''' 
    Verify if the source tower and the destination tower are empty or not and apply the move
    I: the towers, the source tower and the destination tower of the move
    O: none
    '''
    if not towers[source]: # if the source tower is empty then we move the disk from the destination tower to the source tower
        move_disk(towers, destination, source)
        display_towers_terminal1(towers)
    elif not towers[destination]: # if the destination tower is empty then we move the disk from the source tower to the destination tower  
        move_disk(towers, source, destination)
        display_towers_terminal1(towers)
    elif towers[source][-1] > towers[destination][-1]: # if the disk of the source tower is bigger than the disk of the destination tower then we move the disk from the destination tower to the source tower
        move_disk(towers, destination, source)
        display_towers_terminal1(towers)
    else: 
        move_disk(towers, source, destination)
        display_towers_terminal1(towers)







#### Terminal Display functions

def display_towers_terminal0(towers):
    ''' 
    Display the towers in the terminal (most generic version)
    I: the towers
    O: none
    '''
    for i in range(len(towers)):
        print(towers[i])
    print("")
    
    
def display_towers_terminal1(towers):
    ''' 
    Display the towers in the terminal (more advance version)
    I: the towers
    O: none
    '''
    global nb_disk
    for i in range(nb_disk):
        for j in range(len(towers)):
            print(" "*25, end=" ")
            if len(towers[j]) >= nb_disk - i:
                print(towers[j][nb_disk - i - 1],"  ", end=" ")
            else:
                print("    ", end=" ")
        
        print("")
    print("_"*180)





#### Game loop function

def game_loop(game_mode, graphic_mode = 1):
    '''
    Game loop
    I: Int graphic_mode    the graphic mode of the game (0 for the most generic terminal version, 1 for the more advance terminal version )
       Int game_mode       the game mode of the game (0 for the classic game, 1 for recursive demonstration, 2 for iterative demonstration)
    O: none
    '''
    global nb_disk, move_list
    towers = towers_initialisation()
    if game_mode == 0:
        print ("You have", limit_move, "moves to finish the game")
        while not is_finished(towers) and nb_move <= limit_move:
            if graphic_mode == 0:
                display_towers_terminal0(towers)
            else:
                display_towers_terminal1(towers)
                
            move = input("Enter the source tower and the destination tower (c to cancel the last move, q to quit game): ")
            if move == "q":
                break
            if  move == "c":
                if move_list != []:
                    moves = move_list.pop()
                    towers = move_disk(towers, moves[1], moves[0])
                else:
                    print("No move to cancel")
            else:
                source = int(move)
                destination = int(input("Enter the destination tower : "))
                move_list.append([source, destination])
                move_disk(towers, source, destination)
        
        if nb_move == limit_move:
            print("You have reached the limit of moves game finished, you lost!")
        else:
            print("Game finished, you won!")
        
    elif game_mode == 1:
        tower_of_hanoi_recursive(nb_disk, towers)
        print("Game finished")
    elif game_mode == 2:
        tower_of_hanoi_iterative(towers)
        print("Game finished")       