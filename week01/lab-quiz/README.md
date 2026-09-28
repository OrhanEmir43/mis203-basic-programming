When enter an empty name the code takes just "" and goes bottom line.
To make the program more robust, add input validation to ensure the user does not leave the name blank and enters valid numbers for mathematical operations.
Testing & Recent Updates:
-Test Performed:** Tested the user prompt by submitting an empty string (pressing Enter without typing a name) to observe program behavior.
-Changes Made:** Updated `input()` handling to validate user inputs, preventing empty string submissions and ensuring proper data conversion before processing.
git commit -m "feat: validate empty name inputs and integer conversions"
