# Password-Strength-Checker-Tool
The Password Strength Checker Tool evaluates the strength of a password based on its length, composition, and complexity. It helps users create strong passwords that are harder to guess.

Features
1. Evaluates passwords based on:
- Length.
- Inclusion of uppercase, lowercase, numbers, and special characters.

2. Provides a simple GUI to input passwords and display their strength.

Password Strength Categories
- Weak (too short): Passwords shorter than 6 characters.
- Weak: Contains only one type of character (e.g., only letters).
- Medium: Contains two types of characters (e.g., letters and numbers).
- Strong: Contains three types of characters.
- Very Strong: Contains all four types (uppercase, lowercase, numbers, special characters).

Installation
1. Install Python 3.9 or later.
2. Install wxPython:
   
   pip install wxPython

Usage
1. Run the script:

   python password_checker.py

2. Enter a password into the input field.
3. Click the "Check Strength" button.
4. View the strength evaluation below the button.

Example Output
1. Password: 12345
   Strength: Weak (too short)

2. Password: password
   Strength: Weak

3. Password: Password123
   Strength: Strong

4. Password: P@ssw0rd!
   Strength: Very Strong


Known Issues
- Passwords are evaluated only based on their composition, not on their context or dictionary words (e.g., password123 is rated "Strong" despite being insecure).

Future Improvements
- Add dictionary-based checks to detect common insecure passwords.
- Provide suggestions for improving password strength.

This tool is a simple yet effective way to help users create stronger passwords. Let me know if you'd like further customization!
  
