- **Name:** Orhan Emir Dağtaş
- **Student Number:** 2504109029
- **Department:** MIS
- **Course Name:** MIS 203 - Basic Programming

## AI Tool Note

**AI Tool Used:** Claude

**Prompt Used:** "Write a Python program that asks the user for their name, department, age, and career goal, then prints a formatted student profile."

**What did you change?** I added a blank line before the profile output for readability, and renamed variables to match the assignment's exact field names.



week02:


AI Tool: Claude

Prompt: i cant see a difference except students+ = 1 i fix this btw but the other one is invisible can u finBd the other mistake

What i changed: I changed 2 lines of code one of is students+= 1 i forgot write this and the other one is elif/else/if must be written with tab spaces

Break: the q word is break the code



week03:


AI Tool: Gemini

Prompt : Write me these codes that my teacher gave me; explain me strip, 2.f and try commands.

Changes: I changed the  age scales.

Tests: 1. Input: Name="MehmetHan", Age=5 (Boundary age < 6), Day="weekend", Student="no" -> Result: "MehmetHan: 0.00 TRY (Free)"
  2. Input: Name="Kadir", Age=65 (Boundary age >= 65), Day="weekday", Student="no" -> Result: "Kadir: 100.00 TRY (Senior)"
  3. Input: Name="Emir", Age=26, Day="weekday", Student="yes" -> Result: "Emir: 200.00 TRY (Standard)"
  
  Why does the order of the rules matter: The order of rules matters because if a broader rule (like Student) comes before a more specific or higher-discount rule (like Child), a 10-year-old student would get the smaller Student discount (30%) instead of the correct Child discount (40%). The system stops evaluation at the first matching rule.
