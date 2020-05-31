import webbrowser
while True:

    choice = int(input("[1] Happy\n[2] Depressing Russian\n[3] Depressing Non-Russian\n[4] Motivational Metal\n"))

    if choice == 1:                     # Happy
        print("Work in progress.")
        input("\n")
    elif choice == 2:                   # Sad Russian
        webbrowser.open('https://www.youtube.com/watch?v=W0bxjjPMU-Y&list=PLqA1TPFVNT1anGGR7iOq6fQavFD8lxLhI&index=1')
        print("Playlist is updated every so often.")
        input("\n")
    elif choice == 3:                   # Sad Non-Russian
        print("Work in progress.")
        input("\n")
    elif choice == 4:                   # Motivational Metal
        print("Work in progress.")
        input("\n")
    else:
        input("The number you put in does not exist. Please try again. ")
