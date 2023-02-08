import sys

def power_table(n):

    # Ensure n is a positive integer
    if not isinstance(n, int) or n < 1:
        print("Error: Please provide a positive integer as input.")
        return

    # Find maximum number of digits in n^2, n^3 and n^4
    max_width = max(len(str(n**2)), len(str(n**3)), len(str(n**4))) + 2

    # Print header
    for i in range(4):
        print(f'i^{i+1}'.ljust(max_width,' '),end='')
    print()

    # Print separator
    print("-" * (max_width) * 4)

    # Print table
    for i in range(n): # row
        for j in range(4): # column
            if j == 0:
                print(i+1,end = ' ')
            else:
                print(f'{(i+1)**(j+1):{max_width}}',end='')
                # print(f'{((i+1)*(j+1))**j}',end = ' ')    # .ljust(max_width + 2), end="")
        print()
    


# Check if input argument has been provided
if len(sys.argv) < 2:
    print("Error: Please provide a positive number as input.")
else:
    n = int(sys.argv[1])
    power_table(n)



