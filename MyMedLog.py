#Medication Log
patient_list = {1: "Surab", 2: "Vishal", 3: "Sindhu"}
log_list = {1: "Medication", 2: "Diet"}
#TO ADD NEW PATIENTS:
#patient_list.update({"4":"New_Patient"})

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Patient Name:")
    for key, value in patient_list.items():
        print("Press", key, "for", value, "\n", end="")
    patient_name = int(input())

    print("Selected Patient : ", patient_list[patient_name], "\n", end="")

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    op = int(input())

    if op == 1:
        for key, value in log_list.items():
            print("Press", key, "to log", value, "\n", end="")
        log_name = int(input())
        print("Selected : ", log_list[log_name])
        f = open(patient_list[patient_name] + "_" + log_list[log_name] + ".txt", "a")
        k = 'y'
        while (k != "n"):
            print("Enter", log_list[log_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()).replace(":", "-") + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op == 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        log_name = int(input())
        print(patient_list[patient_name], "-", log_list[log_name], "Report :", "\n", end="")
        f = open(patient_list[patient_name] + "_" + log_list[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")