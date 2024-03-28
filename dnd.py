from random import *

def roll_die(sides : int, advantage : bool = False) -> int:
    """Simulates a DnD dice roll given the sides and whether the player has advantage"""
    die_to_roll : int = 2 if advantage else 1
    die_rolled : list = []

    for i in range (0, die_to_roll):
        die_rolled.append(randint(1, sides))

    # Player does not have advantage, meaning they roll only one die
    if die_to_roll == 1:
        return die_rolled[0]
    
    # Player has advantage, meaning they roll two dice
    else:
        return max(die_rolled)
    
def get_starting_stats() -> int:
    """Simulates getting a starting base stat for a dnd character"""
    dice : list = []
    starting_stat : int = 0

    for i in range(0, 4):
        dice.append(roll_die(6))
    dice.remove(min(dice))
    starting_stat = sum(dice)

    return starting_stat


if __name__ == '__main__':
    print(roll_die(6))
    print(roll_die(8, True))
    print(roll_die(20))

    sides : str = ''
    while sides.casefold() != 'quit':
        sides = input('Enter the amount of sides to roll or type \'quit\' to quit: ')
        if sides == 'quit':
            break
        advantage : str = input('Would you like to roll with advantage? (y/n): ')
        while advantage.casefold() != 'y' and advantage.casefold() != 'n':
            print("Invalid input.")
            advantage : str = input('Would you like to roll with advantage? (y/n): ')
        print(roll_die(int(sides), advantage='y'))
        
    print(get_starting_stats())