from Functions import *






print("-----Auxilliary fonction test-----")
print ("nombre de disque: ",nb_disk)
print ("test towers_initialisation: ",towers_initialisation())
print ("test is_valid_move (0->2): ",is_valid_move(towers_initialisation(), 0, 2))
print("test move_disk: ",move_disk(towers_initialisation(), 0, 2))
print("test is_finished [[3, 2, 1], [], []] : ",is_finished([[3, 2, 1], [], []]))
print("test is_finished [[], [], [1]] : ",is_finished([[], [], [1]]))
print("\n")

print("-----Terminal display fonction test-----")
print("test display_towers_terminal0: ") ; display_towers_terminal0(towers_initialisation())
towers_test_terminal1 = [[3, 2, 1], [1], [1,2]] ; print("test display_towers_terminal1 : ") ; display_towers_terminal1(towers_test_terminal1)


print("\n-----Automatic resolution test-----")
towers = towers_initialisation() 
print("test tower_of_hanoi_recursive: ") ; tower_of_hanoi_recursive(nb_disk, towers) 
print("test tower_of_hanoi_iterative: ") ; tower_of_hanoi_iterative(towers)


print("\n\n-----Game loop test-----")

print("test game_loop recursive: ") ; game_loop(1)
nb_move = 0 # we reset the number of moves as the other test will increment it
print("test game_loop iterative: ") ; game_loop(2)

#print("test game_loop classic: ") ; game_loop(0,0)  # uncomment to test the most generic terminal version for the classic game
nb_move = 0 ; print("test game_loop classic: ") ; game_loop(0,1)  # uncomment to test the more advance terminal version for the classic game


print ("\n\n-----Test Scores-----")

print("nombre de move: ",nb_move)