 #LABARATORY EXERCISE 17
 #Simulated Device Monitoring And Alert System


reading= [28, 31, 35, 29]

def classify_reading(temp):
    if temp < 30:
        return "NORMAL"
    elif temp <= 35:
        return "WARNING"
    else:
        return "CRITICAL"
    
def view_readings():
    print("Current readings")
    print("----------------")
    for i, temp in enumerate(reading, start=1):
        print(f"Reading {i}: {temp} C")
        
def add_reading():
    temp = int(input("Enter temperature (0-100):"))
    if 0<= temp <= 100:
        reading.append(temp)
        print("Reading added successfully.")
    else:
        print("Invalid Reading! Enter a number from 0 to 100.")
    
def classify_readings():
    print("READING CLASSIFICATION")
    print("----------------------")
    
    for i, temp in enumerate(reading, start=1):
        status = classify_reading(temp)
        print(f"Reading {i}: {temp} C- {status}")
        
def generate_summary():
    total = len(reading)
    
    if total == 0:
        print("No readings available")
        return
    
    average = sum(reading) / total
    highest = max(reading)
    lowest = min(reading)
    
    normal = 0
    warning = 0
    critical = 0
    
    for temp in reading:
        status = classify_reading(temp)
        
        if status == "NORMAL":
            normal += 1
        elif status == "WARNING":
            warning += 1
        else:
            critical += 1
        
        
    if critical > 0:
        overall_status = "CRITICAL"
    elif warning > 0:
        overall_status = "WARNING"
    else:
        overall_status = "NORMAL"
    
    print("DEVICE MONITORING SUMMARY")
    print("-------------------------")
    print("Total readings:", total)
    print(f"Average temperature: {average:.2f} C")
    print("Highest temperature:", highest, "C")
    print("Lowest temperature:", lowest, "C")
    print("Normal readings:", normal)
    print("Warning readings:", warning)
    print("Critical readings:", critical)
    print("Overall device status:", overall_status)
    
def main():
    while True:
        print("SIMULATED DEVICE MONITORING SYSTEM")
        print("----------------------------------")
        print("[1] View readings")
        print("[2] Add Readings")
        print("[3] Classify Readings")
        print("[4] Generate summary")
        print("[5] Exit")
        
        choice = input("Enter choice:")
        
        if choice =="1":
            view_readings()
        elif choice =="2":
            add_reading()
        elif choice =="3":
            classify_readings()
        elif choice == "4":
            generate_summary()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1 to 5.")
            
main()