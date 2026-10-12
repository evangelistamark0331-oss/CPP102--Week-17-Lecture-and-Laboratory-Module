TEST CASES: SIMULATED DEVICE MONITORING SYSTEM

TC01: View Readings Input: 1 Expected Output: Displays all readings.

TC02: Add Valid Reading Input: 25 Expected Output: Reading added successfully.

TC03: Add Minimum Value Input: 0 Expected Output: Reading added successfully.

TC04: Add Maximum Value Input: 100 Expected Output: Reading added successfully.

TC05: Invalid Low Value Input: -1 Expected Output: Invalid reading message.

TC06: Invalid High Value Input: 101 Expected Output: Invalid reading message.

TC07: Classify Normal Input: 28 Expected Output: NORMAL.

TC08: Classify Warning Input: 30 Expected Output: WARNING.

TC09: Classify Critical Input: 36 Expected Output: CRITICAL.

TC10: Generate Summary Input: [28, 31, 35, 29] Expected Output: Average: 30.75°C; Overall status: WARNING.

TC11: Empty Readings Input: [] Expected Output: No readings available.

TC12: All Normal Readings Input: [20, 25, 29] Expected Output: Overall status: NORMAL.

TC13: All Warning Readings Input: [30, 32, 35] Expected Output: Overall status: WARNING.

TC14: All Critical Readings Input: [36, 40, 50] Expected Output: Overall status: CRITICAL.

TC15: Invalid Menu Choice Input: 6 Expected Output: Invalid choice! Please select 1 to 5.

TC16: Exit Program Input: 5 Expected Output: Exiting program. Goodbye!

TC17: Non-Numeric Temperature Input: abc Expected Output: ValueError occurs.

TC18: Add Critical Reading Input: 40 Expected Output: Reading added successfully; classification is CRITICAL.
