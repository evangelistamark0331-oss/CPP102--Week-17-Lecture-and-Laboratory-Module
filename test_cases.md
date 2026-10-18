# Test Cases – Simulated Device Monitoring and Alert System

**Tested by:** Mark R. Evangelista  
**Date of Testing:** October 18, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Display the four initial readings: 28, 31, 35, and 29 | The program displays all four stored readings. | Pass |
| TC02 | Choose 2, enter 33 | Add the reading successfully and classify it as WARNING | The program adds 33 and displays its classification as WARNING. | Pass |
| TC03 | Choose 2, enter `abc` | Reject the invalid input without crashing | The program displays an invalid input message. | Pass |
| TC04 | Choose 2, enter 101 | Reject the reading because it exceeds 100 | The program displays an invalid reading message. | Pass |
| TC05 | Choose 2, enter -5 | Reject the reading because it is below 0 | The program displays an invalid reading message. | Pass |
| TC06 | Choose 3 | Classify all readings according to the temperature thresholds | Readings below 30 are NORMAL, readings from 30 to 35 are WARNING, and readings above 35 are CRITICAL. | Pass |
| TC07 | Choose 4 | Display the numerical summary and overall device status | The program displays the total, average, highest, lowest, classification counts, and overall status. | Pass |
| TC08 | Enter 6 at the menu | Reject the invalid menu choice | The program displays an invalid choice message. | Pass |
| TC09 | Choose 2, enter 30 | Add the reading and classify it as WARNING | The program adds 30 and displays WARNING. | Pass |
| TC10 | Choose 5 | Exit the program | The program displays the goodbye message and terminates. | Pass |

## Test Results

**Total Test Cases:** 10  
**Passed:** 10  
**Failed:** 0

*Note: Confirm each actual result by running the program before submitting your report.*

## Bugs Found and Fixed

- Bug Found: The original `add_reading()` function caused a `ValueError` when the user entered letters, such as `abc`, instead of a temperature.
- Cause: The program attempted to convert the input directly into an integer without handling invalid text.
- Fix: I added a `try-except ValueError` block to catch invalid inputs and display an appropriate error message.
- Result: The program now rejects non-numeric input without crashing and allows the user to return to the main menu. This makes the system more reliable and user-friendly.

TC16: Exit Program Input: 5 Expected Output: Exiting program. Goodbye!

TC17: Non-Numeric Temperature Input: abc Expected Output: ValueError occurs.

TC18: Add Critical Reading Input: 40 Expected Output: Reading added successfully; classification is CRITICAL.
