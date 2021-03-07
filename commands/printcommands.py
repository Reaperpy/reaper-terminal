def printcmd():
    print_string = input("Please enter a string that you want to print. ")
    print(print_string)
def writecmd():
    write_string = input("Please enter a string that you want to write to a text file. ")
    write_name = input("Please enter a name for your text file. ")
    write_file = open(f"{write_name}.txt")
    write = write_file.write(write_string)
    write_file.close()
