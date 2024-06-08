import tkinter as tk
import re

def assess_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_character_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Calculate strength score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_character_criteria])
    
    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_character_criteria:
        feedback.append("Password should include at least one special character.")
    
    return {
        "strength": strength,
        "feedback": feedback
    }

def check_password():
    password = entry.get()
    result = assess_password_strength(password)
    strength_label.config(text=f"Password Strength: {result['strength']}")
    feedback_text.delete("1.0", tk.END)
    for feedback in result['feedback']:
        feedback_text.insert(tk.END, f"- {feedback}\n")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")

# Add widgets
tk.Label(root, text="Enter Password:",foreground="blue").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_password,foreground="white",background="red")
check_button.grid(row=1, column=0, columnspan=2, pady=10)

strength_label = tk.Label(root, text="Password Strength: ",foreground="blue")
strength_label.grid(row=2, column=0, columnspan=2, pady=10)

feedback_text = tk.Text(root, height=5, width=50)
feedback_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
