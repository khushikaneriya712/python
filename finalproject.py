import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class FitnessTracker:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.data = pd.read_csv(file_name)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=[
                "Date", "Activity Type", "Duration (Minutes)", "Calories Burned"
            ])

    
    def log_activity(self, date, activity_type, duration, calories):
        if duration <= 0 or calories <= 0:
            print("Invalid input! Duration and calories must be positive.")
            return

        new_entry = {
            "Date": date,
            "Activity Type": activity_type,
            "Duration (Minutes)": duration,
            "Calories Burned": calories
        }

        self.data = pd.concat([self.data, pd.DataFrame([new_entry])], ignore_index=True)
        print("Activity added successfully!")

    
    def calculate_metrics(self):
        total_calories = self.data["Calories Burned"].sum()
        avg_duration = self.data["Duration (Minutes)"].mean()
        activity_count = self.data["Activity Type"].value_counts()

        print("\n--- Fitness Metrics ---")
        print("Total Calories Burned:", total_calories)
        print("Average Duration:", round(avg_duration, 2))
        print("\nActivity Frequency:\n", activity_count)

    
    def filter_activities(self, activity_type=None):
        if activity_type:
            filtered = self.data[self.data["Activity Type"] == activity_type]
        else:
            filtered = self.data

        print("\nFiltered Data:\n", filtered)
        return filtered

    
    def generate_report(self):
        print("\n--- Full Report ---")
        print(self.data.describe())


    def save_data(self):
        self.data.to_csv(self.file_name, index=False)
        print("Data saved to CSV!")

    
    def visualize(self):
        
        activity_sum = self.data.groupby("Activity Type")["Duration (Minutes)"].sum()
        activity_sum.plot(kind='bar', title="Time Spent per Activity")
        plt.ylabel("Minutes")
        plt.show()

        
        daily_calories = self.data.groupby("Date")["Calories Burned"].sum()
        daily_calories.plot(kind='line', marker='o', title="Calories Burned Over Time")
        plt.ylabel("Calories")
        plt.xticks(rotation=45)
        plt.show()

        
        activity_count = self.data["Activity Type"].value_counts()
        activity_count.plot(kind='pie', autopct='%1.1f%%', title="Activity Distribution")
        plt.ylabel("")
        plt.show()

    
        corr = self.data[["Duration (Minutes)", "Calories Burned"]].corr()
        plt.imshow(corr, cmap='coolwarm')
        plt.colorbar()
        plt.xticks([0,1], corr.columns)
        plt.yticks([0,1], corr.columns)
        plt.title("Correlation Heatmap")
        plt.show()


tracker = FitnessTracker("fitness_activities.csv")

while True:
    print("\n1. Add Activity")
    print("2. View Metrics")
    print("3. Filter Activity")
    print("4. Generate Report")
    print("5. Visualize Data")
    print("6. Save & Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        date = input("Enter Date (YYYY-MM-DD): ")
        activity = input("Enter Activity Type: ")
        duration = int(input("Enter Duration (minutes): "))
        calories = int(input("Enter Calories: "))
        tracker.log_activity(date, activity, duration, calories)

    elif choice == '2':
        tracker.calculate_metrics()

    elif choice == '3':
        activity = input("Enter activity type to filter: ")
        tracker.filter_activities(activity)

    elif choice == '4':
        tracker.generate_report()

    elif choice == '5':
        tracker.visualize()

    elif choice == '6':
        tracker.save_data()
        break

    else:
        print("Invalid choice!")