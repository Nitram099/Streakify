🎯 Streakify App
Streakify is a beautifully simple streak-tracking desktop application built with Python and Tkinter. Track your daily routines, maintain streaks, and organize your habits into meaningful categories like Health, Productivity, and more. Keep your progress front and center with an intuitive, modern interface.



🚀 Features
📝 Add Routines: Create and manage routines with customizable times.
🏆 Streak Tracking: Stay consistent and track your daily progress with streak counters.
📅 Temporary Routines: Set up routines for a fixed duration (e.g., 30-day challenges).
🔖 Categories: Organize routines by categories (Health, Productivity, etc.).
💾 Persistent Data: Routines and logs are saved for future sessions.
📊 Logs: Keep a detailed activity log of every completed task.



📦 Installation
Prerequisites
Python 3.x installed on your system.
Tkinter (comes pre-installed with Python).
Steps:
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Streakify.git
Navigate to the project directory:

bash
Copy code
cd Streakify
Install necessary Python packages (Tkinter comes pre-installed in most Python distributions):

bash
Copy code
pip install tk
Run the application:

bash
Copy code
python main.py


🛠️ Usage
1. Adding a Routine
Click the Add Routine button to create a new routine.
Enter the routine name, time, and select or type a category.
Decide if it’s a temporary routine and set an end date if applicable.
2. Completing a Routine
When a routine is due, click the Complete button to mark it as finished.
Your streak counter will update automatically.
3. Organizing by Categories
Assign routines to categories (Health, Productivity, etc.) for better organization.
4. Logging Activity
Each activity is logged automatically with a timestamp, so you can track progress over time.


📂 File Structure
bash
Copy code
Streakify/
│
├── routines.json          # Stores all routine data.
├── activity_log.txt       # Log of user activity.
├── main.py                # Main application code.
├── README.md              # You're reading it!
Routine Data (routines.json)
Routines are stored in JSON format with fields such as:

time: Routine time (e.g., "07:00").
streak: Current streak count.
last_completed: The last date the routine was completed.
category: Routine category (e.g., Health, Productivity).
temporary: Whether the routine is temporary.
end_date: Expiration date for temporary routines.
Example:

json
Copy code
{
    "Morning Exercise": {
        "time": "07:00",
        "streak": 3,
        "last_completed": "2023-08-30",
        "category": "Health",
        "temporary": false,
        "end_date": null
    }
}


📝 Example Log (activity_log.txt)
plaintext
Copy code
2023-08-30 07:05: Added routine: Morning Exercise, Category: Health
2023-08-31 07:01: Completed routine: Morning Exercise
🌟 Future Features
🔔 Notifications: Get reminders when routines are due.
📈 Progress Charts: Visualize streak data with charts and graphs.
📊 Stats Dashboard: Detailed insights into routine performance.
☁️ Cloud Sync: Sync your streak data across devices.
🤝 Contributing

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
