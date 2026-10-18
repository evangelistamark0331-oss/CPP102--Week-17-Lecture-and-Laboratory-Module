# Simulated Device Monitoring and Alert System

Student Name: Mark R. Evangelista  
Student Number: 2601305
Section: 1CPE-A

 Project Description

This program simulates a device monitoring system that checks and classifies temperature readings. It allows users to view current readings, add new temperatures, classify each reading as NORMAL, WARNING, or CRITICAL, and generate a summary of the device's condition. The program also calculates the average, highest, and lowest temperatures and displays the overall device status.

 Features

- View all stored temperature readings.
- Add a new temperature reading from 0 to 100.
- Classify readings as NORMAL, WARNING, or CRITICAL.
- Generate a summary showing the total, average, highest, and lowest temperatures.
- Count the number of NORMAL, WARNING, and CRITICAL readings.
- Determine the overall device status based on the stored readings.
- Reject invalid menu choices and temperature values outside the accepted range.

 Requirements

- Python 3
- No external packages required.

 How to Run

1. Save the code in a file named `device_monitor.py`.
2. Open a terminal inside the Week17 folder.
3. Run the following command:

   `python device_monitor.py`

   On macOS or Linux, use `python3 device_monitor.py`.

 Sample Output

The following output is based on the initial readings in the program: 28, 31, 35, and 29.

```text
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View readings
[2] Add Readings
[3] Classify Readings
[4] Generate summary
[5] Exit
Enter choice:3

READING CLASSIFICATION
----------------------
Reading 1: 28 C- NORMAL
Reading 2: 31 C- WARNING
Reading 3: 35 C- WARNING
Reading 4: 29 C- NORMAL
```

Sample Summary

```text
DEVICE MONITORING SUMMARY
-------------------------
Total readings: 4
Average temperature: 30.75 C
Highest temperature: 35 C
Lowest temperature: 28 C
Normal readings: 2
Warning readings: 2
Critical readings: 0
Overall device status: WARNING
```

 Test Cases

I prepared 10 test cases to check the main functions of the program, including viewing readings, adding valid temperatures, classifying readings, generating a summary, and handling invalid inputs.

Passed: (Fill in after testing)  
Failed: (Fill in after testing)

The full test details will be saved in `test_cases.md`.

 Known Limitations

The program uses simulated temperature readings instead of an actual temperature sensor. The readings are stored only in a Python list, so newly added values are lost when the program closes. The temperature classifications use fixed thresholds: below 30°C is NORMAL, 30–35°C is WARNING, and above 35°C is CRITICAL. The program can also encounter an error if the user enters letters or decimal values instead of whole numbers when adding a reading.

 Reflection

The hardest part of this activity was creating the functions that classify the temperature readings and generate the device monitoring summary. I learned how to use functions, loops, lists, conditional statements, and basic calculations in Python. I also learned how the program determines the overall status by checking whether any readings are classified as CRITICAL or WARNING. One improvement I would make is adding better input validation to prevent errors when users enter letters or decimal numbers. In the future, I would also like to save the readings in a file and connect the system to an actual temperature sensor.
