import webbrowser

x = "Playlist is updated every so often.\n"

while True:

    choice = input("[1] Happy\n[2] Depressing Russian\n[3] Depressing Non-Russian\n[4] Motivational Metal\n\n")

    if choice == 1:                     # Happy
        print("Work in progress.\n")
    elif choice == 2:                   # Sad Russian
        webbrowser.open('https://www.youtube.com/watch?v=W0bxjjPMU-Y&list=PLqA1TPFVNT1anGGR7iOq6fQavFD8lxLhI&index=1')
        print(x)
    elif choice == 3:                   # Sad Non-Russian
        print("Work in progress.\n")
    elif choice == 4:                   # Motivational Metal
        webbrowser.open('https://www.youtube.com/watch?v=RYsQqaAxDtw&list=PLqA1TPFVNT1atGT8CdR1Gcn6IVYEWSz2p&index=1')
        print(x)
    elif choice == 1488:                # You know what this is
        webbrowser.open('https://www.youtube.com/watch?v=r-NiDsRNr0I&list=PLqA1TPFVNT1Zj6a4okk86FzlwDNHCycrJ&index=2')
        print(x)
    else:
        print("The number you put in does not exist. Please try again.\n")
