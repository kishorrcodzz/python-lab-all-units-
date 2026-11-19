import json

logs = []

n = int(input("Enter number of log entries: "))
for i in range(n):
    message = input("Enter log message: ")
    status = input("Enter status (INFO/ERROR/WARNING): ")

    log = {
        "message": message,
        "status": status
    }

    logs.append(log)
with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

print("\nLog data saved successfully")

with open("logs.json", "r") as file:
    data = json.load(file)

print("\nLog Report:")

for log in data:
    print("Message:", log["message"])
    print("Status:", log["status"])
    print("----------------")