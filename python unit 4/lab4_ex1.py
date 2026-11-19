file = open("student.txt", "w")

file.write("Name: Kishore Kumar R\n")
file.write("Course: B.Tech AIML\n")
file.write("College: Jain University\n")

file.close()
print("Data written successfully")

file = open("student.txt", "r")
print("\nFile Contents:")
print(file.read())

file.close()
file = open("student.txt", "a")

file.write("Semester: 3\n")

file.close()

print("Data appended successfully")
file = open("student.txt", "r")
print("\nUpdated File Contents:")
print(file.read())

file.close()