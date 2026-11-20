print("LOG FILE READER")
file = open("log.txt", "w")
file.write("INFO: Program started\n")
file.write("WARNING: Low memory\n")
file.write("ERROR: File not found\n")
file.write("INFO: Program completed\n")
file.close()
file = open("log.txt", "r")
print("\nLOG FILE CONTENTS")

for line in file:
    print(line, end="")
file.close()