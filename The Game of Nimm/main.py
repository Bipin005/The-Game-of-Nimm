def main():
    stones = 20
    current_player = 1  # Start with Player 1

    while stones > 0:
        print(f"There are {stones} stones left.")
        
        remove = int(input(f"Player {current_player} would you like to remove 1 or 2 stones? "))
        while remove not in [1, 2] or remove > stones:
            remove = int(input("Please enter 1 or 2: "))
        
        stones -= remove

        if stones == 0:
            winner = 2 if current_player == 1 else 1
            print(f"\nPlayer {winner} wins!")
            break

        current_player = 2 if current_player == 1 else 1
        print()

if __name__ == '__main__':
    main()