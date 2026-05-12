import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class FitnessDataAnalyzer:
    def __init__(self):
        self.data = None
        self.current_plot = None

    def __del__(self):
        plt.close('all')

   
    def load_data(self, file_path):
        if file_path.endswith('.csv'):
            self.data = pd.read_csv(file_path, parse_dates=['Date'])
        elif file_path.endswith(('.xlsx', '.xls')):
            self.data = pd.read_excel(file_path, parse_dates=['Date'])
        else:
            raise ValueError("Unsupported file format. Use CSV or Excel.")
        print("Dataset loaded successfully!")

   
    def explore_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n== Explore Data ==")
            print("1. First 5 rows")
            print("2. Last 5 rows")
            print("3. Column names")
            print("4. Data types")
            print("5. Info")
            print("6. Back")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                print(self.data.head())
            elif choice == '2':
                print(self.data.tail())
            elif choice == '3':
                print(self.data.columns.tolist())
            elif choice == '4':
                print(self.data.dtypes)
            elif choice == '5':
                self.data.info()
            elif choice == '6':
                break
            else:
                print("Invalid choice.")

   
    def dataframe_operations(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n== DataFrame Operations ==")
            print("1. Calories Statistics")
            print("2. Duration Statistics")
            print("3. Activity-wise Summary")
            print("4. Back")

            choice = input("Enter choice: ").strip()

            if choice == '1':
                arr = self.data['Calories Burned'].to_numpy()
                print(f"Total Calories: {arr.sum()}")
                print(f"Average Calories: {arr.mean():.2f}")
                print(f"Min: {arr.min()} | Max: {arr.max()}")

            elif choice == '2':
                arr = self.data['Duration (Minutes)'].to_numpy()
                print(f"Total Duration: {arr.sum()} min")
                print(f"Average Duration: {arr.mean():.2f} min")

            elif choice == '3':
                print(
                    self.data.groupby('Activity Type')[
                        ['Duration (Minutes)', 'Calories Burned']
                    ].sum()
                )

            elif choice == '4':
                break
            else:
                print("Invalid choice.")

  
    def handle_missing_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n== Missing Data ==")
            print("1. Show missing values")
            print("2. Fill with mean")
            print("3. Drop rows")
            print("4. Back")

            choice = input("Enter choice: ").strip()

            if choice == '1':
                print(self.data.isnull().sum())

            elif choice == '2':
                num_cols = self.data.select_dtypes(include=np.number).columns
                self.data[num_cols] = self.data[num_cols].fillna(
                    self.data[num_cols].mean()
                )
                print("Filled missing values with mean.")

            elif choice == '3':
                self.data.dropna(inplace=True)
                print("Dropped missing rows.")

            elif choice == '4':
                break

            else:
                print("Invalid choice.")


    def generate_descriptive_statistics(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        print("\n== Descriptive Statistics ==")
        print(self.data.describe())

        print("\nActivity-wise Calories:")
        print(
            self.data.pivot_table(
                values='Calories Burned',
                index='Activity Type',
                aggfunc='sum'
            )
        )

   
    def visualize_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n== Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Back")

            choice = input("Enter choice: ").strip()

            if choice == '6':
                break

            fig, ax = plt.subplots(figsize=(10, 6))

            if choice == '1':
                self.data.groupby('Activity Type')['Calories Burned'].sum().plot(
                    kind='bar', ax=ax, color='skyblue'
                )
                ax.set_title("Calories by Activity")

            elif choice == '2':
                self.data.groupby('Date')['Calories Burned'].sum().plot(
                    ax=ax, marker='o', color='red'
                )
                ax.set_title("Calories Over Time")

            
            elif choice == '3':
                ax.scatter(
                    self.data['Duration (Minutes)'],
                    self.data['Calories Burned'],
                    color='green'
                )
                ax.set_xlabel("Duration")
                ax.set_ylabel("Calories")

            elif choice == '4':
                self.data.groupby('Activity Type')['Calories Burned'].sum().plot(
                    kind='pie', autopct='%1.1f%%', ax=ax
                )
                ax.set_ylabel("")
                ax.set_title("Activity Share")

            elif choice == '5':
                self.data['Duration (Minutes)'].plot(
                    kind='hist', bins=10, ax=ax, color='purple'
                )
                ax.set_title("Duration Distribution")

            else:
                print("Invalid choice.")
                plt.close()
                continue

            plt.tight_layout()
            self.current_plot = fig
            plt.show()

    
    def save_visualization(self):
        if self.current_plot is None:
            print("No plot available.")
            return

        fname = input("Enter file name: ")
        self.current_plot.savefig(fname)
        print("Saved successfully!")

   
    def run(self):
        while True:
            print("\n===== FITNESS DATA ANALYZER =====")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. DataFrame Operations")
            print("4. Missing Data Handling")
            print("5. Statistics")
            print("6. Visualization")
            print("7. Save Plot")
            print("8. Exit")

            choice = input("Enter choice: ").strip()

            if choice == '1':
                path = input("Enter CSV path: ")
                self.load_data(path)

            elif choice == '2':
                self.explore_data()

            elif choice == '3':
                self.dataframe_operations()

            elif choice == '4':
                self.handle_missing_data()

            elif choice == '5':
                self.generate_descriptive_statistics()

            elif choice == '6':
                self.visualize_data()

            elif choice == '7':
                self.save_visualization()

            elif choice == '8':
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")


if __name__ == '__main__':
    analyzer = FitnessDataAnalyzer()
    analyzer.run()