import json
print("JSON LOG FILE ANALYZER")
logs = [
    {"level": "INFO", "message": "Program started"},
    {"level": "ERROR", "message": "File not found"},
    {"level": "WARNING", "message": "Low memory"},
    {"level": "ERROR", "message": "Connection failed"},
    {"level": "INFO", "message": "Program completed"}
]
file = open("logs.json", "w")
json.dump(logs, file, indent=4)
file.close()
file = open("logs.json", "r")
data = json.load(file)
file.close()
info = 0
warning = 0
error = 0
print("\nLOG DETAILS")
for log in data:
    print(log["level"], ":", log["message"])
    if log["level"] == "INFO":
        info += 1
    elif log["level"] == "WARNING":
        warning += 1
    elif log["level"] == "ERROR":
        error += 1
print("\nLOG SUMMARY")
print("INFO:", info)
print("WARNING:", warning)
print("ERROR:", error)
print("Total Logs:", len(data))