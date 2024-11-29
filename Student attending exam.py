medical_cause=input("did you have a medical cause yes or no: ")
attendace=int(input("enter student attendance: "))
if medical_cause=="yes":
    print("allowed")
else:
    if attendace>=75:
        print("you are allowed")
    else:
        print("you are not allowed")