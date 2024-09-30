import tkinter as tk  # Importing Tkinter for GUI
from tkinter import messagebox, simpledialog  # Importing messagebox and simpledialog for user interactions
from tkinter import ttk  # Importing ttk for themed widgets
from datetime import datetime, date  # Importing datetime to manage time and dates
import json  # Importing JSON for data storage
import os  # Importing os for file management

# Constants for file paths and routine categories
ROUTINES_FILE = "routines.json"  # File to save routines data
LOG_FILE = "activity_log.txt"  # File to log user activities
CATEGORIES = ["Health", "Productivity", "Exercise", "Learning", "Other"]  # Routine categories

# Function to load routines from a JSON file
def load_routines():
    if os.path.exists(ROUTINES_FILE):  # Check if routines file exists
        try:
            with open(ROUTINES_FILE, "r") as file:  # Open the file in read mode
                return json.load(file)  # Load and return the JSON data
        except json.JSONDecodeError:  # Handle file decoding errors
            return {}  # Return an empty dictionary if error occurs
    return {}  # If file doesn't exist, return an empty dictionary

# Function to save routines to the JSON file
def save_routines(routines):
    with open(ROUTINES_FILE, "w") as file:  # Open the file in write mode
        json.dump(routines, file)  # Save the routines as JSON

# Function to log activities to a text file
def log_activity(activity):
    with open(LOG_FILE, "a") as file:  # Open the log file in append mode
        file.write(f"{datetime.now()}: {activity}\n")  # Log the activity with a timestamp

# Main application class for Streakify
class StreakifyApp:
    def __init__(self, root):
        self.root = root  # Main application window
        self.root.title("Streakify")  # Set window title

        # Set the theme for the app
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use 'clam' for a modern appearance

        # Configure styles for the widgets
        self.style.configure('TButton', font=('Helvetica', 10), padding=10, color='#AD4CB8')
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TFrame', background='#73FAE8')

        # Load routines from the JSON file
        self.routines = load_routines()

        # Create UI widgets
        self.create_widgets()

        # Update the display to show the routines
        self.update_routines_display()

    # Method to create the UI components
    def create_widgets(self):
        # Button to add a new routine
        self.add_routine_button = ttk.Button(self.root, text="Add Routine", command=self.add_routine)
        self.add_routine_button.pack(pady=10)  # Add padding around the button

        # Frame to display the list of routines
        self.routines_frame = ttk.Frame(self.root, padding="10")
        self.routines_frame.pack(pady=10, fill=tk.BOTH, expand=True)  # Make the frame expand with the window

    # Method to add a new routine
    def add_routine(self):
        routine_name = simpledialog.askstring("Routine", "Enter the routine:")  # Ask user for routine name
        if not routine_name:
            return  # If no name entered, exit the method

        routine_time_str = simpledialog.askstring("Time", "Enter the time (HH:MM):")  # Ask for the routine time
        try:
            routine_time = datetime.strptime(routine_time_str, "%H:%M").time()  # Parse the time string
        except ValueError:
            messagebox.showerror("Invalid time", "Please enter a valid time in HH:MM format.")  # Show error for invalid time
            return

        # Ask user to select a category or type their own
        category = simpledialog.askstring("Category", f"Enter a category (e.g., {', '.join(CATEGORIES)}):")
        if not category:
            category = "Other"  # Default category if not entered

        # Ask if the routine is temporary
        is_temporary = messagebox.askyesno("Routine Type", "Is this a temporary routine?")
        end_date_str = None
        if is_temporary:
            end_date_str = simpledialog.askstring("End Date", "Enter the end date (YYYY-MM-DD):")  # Ask for end date if temporary
            try:
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()  # Parse the end date string
                if end_date < date.today():
                    messagebox.showerror("Invalid date", "End date must be in the future.")  # Error if date is in the past
                    return
            except ValueError:
                messagebox.showerror("Invalid date", "Please enter a valid date in YYYY-MM-DD format.")  # Error for invalid date
                return

        # Add the new routine to the routines dictionary
        self.routines[routine_name] = {
            "time": routine_time_str,  # Time of the routine
            "streak": 0,  # Initial streak is 0
            "last_completed": None,  # Last completed date is None
            "category": category,  # Category of the routine
            "temporary": is_temporary,  # Whether the routine is temporary
            "end_date": end_date_str  # End date if temporary
        }

        # Save routines and log the addition of the new routine
        save_routines(self.routines)
        log_activity(f"Added routine: {routine_name}, Category: {category} at {routine_time_str}, Temporary: {is_temporary}, End Date: {end_date_str}")

        # Update the routines display
        self.update_routines_display()

    # Method to update the routines display in the app
    def update_routines_display(self):
        for widget in self.routines_frame.winfo_children():  # Remove existing widgets
            widget.destroy()

        # Loop through all routines and display them
        for routine, details in self.routines.items():
            if details['temporary'] and details['end_date']:  # Check if routine is temporary and has an end date
                end_date = datetime.strptime(details['end_date'], "%Y-%m-%d").date()
                if date.today() > end_date:  # If end date has passed, delete the routine
                    del self.routines[routine]
                    continue

            # Get the category of the routine
            category = details.get('category', 'Other')  # Default category is 'Other' if not provided

            # Create a frame for each routine
            frame = ttk.Frame(self.routines_frame)
            frame.pack(fill=tk.X, pady=5)

            # Label for the routine name and time
            routine_label = ttk.Label(frame, text=f"{routine} - {category} - Time: {details['time']}", style='White.TLabel')
            routine_label.pack(side=tk.LEFT, padx=5)

            # Label for the streak count
            streak_label = ttk.Label(frame, text=f"🔥 Streak: {details['streak']}", style='White.TLabel')
            streak_label.pack(side=tk.LEFT, padx=5)

            # Check if the routine is already completed for today
            now = datetime.now().time()
            routine_time = datetime.strptime(details['time'], "%H:%M").time()
            if details['last_completed'] == datetime.now().date().isoformat() or now > routine_time:
                # Disable the complete button if the routine is already completed or it's past the routine time
                complete_button = ttk.Button(frame, text="Complete", state=tk.DISABLED)
            else:
                # Create a complete button to mark the routine as done
                complete_button = ttk.Button(frame, text="Complete", command=lambda r=routine: self.complete_routine(r))
            complete_button.pack(side=tk.RIGHT, padx=5)

        # Save updated routines
        save_routines(self.routines)

    # Method to mark a routine as complete
    def complete_routine(self, routine):
        now = datetime.now()
        self.routines[routine]['last_completed'] = now.date().isoformat()  # Update last completed date
        self.routines[routine]['streak'] += 1  # Increment streak count
        save_routines(self.routines)  # Save updated routines
        log_activity(f"Completed routine: {routine}")  # Log the completion of the routine
        self.update_routines_display()  # Update the display

# Main entry point to run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = StreakifyApp(root)  # Instantiate the app
    root.mainloop()  # Start the Tkinter event loop
