import random

grid = []
grid_size = int(input("Enter the grid size: "))
number_of_ships = int(input("Enter the number of ships at battle: "))
ships_positions = []
positions_gussed = []


def grid_maker():
    for k in range(grid_size): #makeing a list of list
        grid.append([])
    for k in range(len(grid)): # making a list with grid_size and inserting * in to it
        for i in range(grid_size):
            grid[k].append('*')


def random_coordinates(): #create a pair of random integers between the 0 and the grid_size
    x_axis= random.randint(0,grid_size)
    y_axis= random.randint(0,grid_size)
    return x_axis, y_axis


def ship_location_plotter(): #create unique set of coordinates for the ships
    i = 0
    for k in range(grid_size):
        ships_positions.append(random_coordinates())

    while i <= len(ships_positions):
        for j in range(0,grid_size,-1):
            while ships_positions[i][0] == ships_positions[j][0] and ships_positions[i][1] == ships_positions[j][1]:
                ships_positions[j][0] = random.randint(0,grid_size)
                ships_positions[j][1] = random.randint(0,grid_size)
        i = i+1

    for k in range(len(ships_positions)):
        grid[ships_positions[k][0]-1][ships_positions[k][1]-1] = "S" #if one exludes the minus 1 from the index it doesnt work proply

    for k in grid:
        print(k)

def inputs():
    x = int(input(f"Please enter a X coordinate for attack: "))
    y = int(input(f"Please enter a Y coordinate for attack: "))
    return x,y


def positions_guessing(): #keep a record of what coordinates has been gussed before, if coordinate alright gussed ask for new ones.
    for i in ships_positions:
        input1 = inputs()
        for k in positions_gussed:
            print("printing from second loop: ")
            if k == input1: #parse through ships_positions
                input1 = inputs()
        positions_gussed.append(input1)
        print(positions_gussed)
        for u in ships_positions:
            print("printing from thrid loop: ")
            print("value of input1 is: ")
            print(input1)
            if (u[0],u[1]) == input1:
                grid[input1[0]-1][input1[1]-1] = "D"
                print("printing from test case: ")
        for j in grid:
            print(j)


def main():
    grid_maker()
    ship_location_plotter()
    positions_guessing()

main()
