from play import play

def main():
    print("Welcome to Checkers!")
    print("Select player types:")
    print("1. User vs. User")
    print("2. User vs. Maraion")
    print("3. Maraion vs. Maraion")
    
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        print("Starting User vs. User game...")
        play(red_player="user", black_player="user")

    elif choice == "2":
        print("Starting User vs. Maraion game...")
        maraion_depth = int(input("Enter Maraion depth (e.g., 4 or 6): ").strip())
        play(red_player="user", black_player="maraion", black_maraion_depth=maraion_depth)

    elif choice == "3":
        print("Starting Maraion vs. Maraion game...")
        red_maraion_depth = int(input("Enter RED Maraion depth (e.g., 4 or 6): ").strip())
        black_maraion_depth = int(input("Enter BLACK Maraion depth (e.g., 4 or 6): ").strip())
        play(red_player="maraion", black_player="maraion", red_maraion_depth=red_maraion_depth, black_maraion_depth=black_maraion_depth)

    else:
        print("Invalid choice. Exiting...")



main()