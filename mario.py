#for _ in range(3):
#    print("#")

def main():
    #print_column(3)
    #print_row(4)
    print_square(3)

#def print_row(width):
 #   print("?" * width)

def print_square(size):
    for i in range(size):
        print("#" * size)

def print_row(width):
    print("#" * width)

#def print_column(height):
    #for _ in range(height):
        #print("#\n" * height, end="")


main()
