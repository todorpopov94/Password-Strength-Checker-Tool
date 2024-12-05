import wx
import re


# Function to check the strength of a password
def check_password_strength(password):
    """
    Evaluates the strength of a password based on length and character composition.
    Returns the strength as a string.
    """
    if len(password) < 6:
        return "Weak (too short)"
    strength = 0
    # Check for various character types
    if re.search(r"[a-z]", password):  # Lowercase letters
        strength += 1
    if re.search(r"[A-Z]", password):  # Uppercase letters
        strength += 1
    if re.search(r"[0-9]", password):  # Numbers
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Special characters
        strength += 1

    # Return strength evaluation
    if strength == 1:
        return "Weak"
    elif strength == 2:
        return "Medium"
    elif strength == 3:
        return "Strong"
    elif strength == 4:
        return "Very Strong"
    else:
        return "Weak"


# Main GUI Application Class
class PasswordStrengthCheckerApp(wx.Frame):
    def __init__(self, parent, title):
        """
        Initializes the GUI for the Password Strength Checker.
        """
        super(PasswordStrengthCheckerApp, self).__init__(
            parent, title=title, size=(400, 250)
        )

        # Create a panel for the GUI
        panel = wx.Panel(self)

        # Add a title label
        title_label = wx.StaticText(
            panel,
            label="Password Strength Checker",
            pos=(100, 20),
            style=wx.ALIGN_CENTER,
        )
        font = wx.Font(
            14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD
        )
        title_label.SetFont(font)

        # Input field for password
        wx.StaticText(panel, label="Enter Password:", pos=(20, 80))
        self.password_input = wx.TextCtrl(
            panel, pos=(150, 75), size=(200, 25), style=wx.TE_PASSWORD
        )

        # Button to check password strength
        self.check_button = wx.Button(panel, label="Check Strength", pos=(150, 120))
        self.check_button.Bind(wx.EVT_BUTTON, self.on_check_strength)

        # Output field for displaying strength
        wx.StaticText(panel, label="Strength:", pos=(20, 170))
        self.result_label = wx.StaticText(panel, label="", pos=(150, 170))

        # Center the window
        self.Centre()

    def on_check_strength(self, event):
        """
        Event handler for the 'Check Strength' button.
        Retrieves the entered password and displays the strength evaluation.
        """
        password = self.password_input.GetValue()
        strength = check_password_strength(password)
        self.result_label.SetLabel(strength)


# Main entry point of the application
if __name__ == "__main__":
    app = wx.App(False)
    frame = PasswordStrengthCheckerApp(None, "Password Strength Checker")
    frame.Show()
    app.MainLoop()
