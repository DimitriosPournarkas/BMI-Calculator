import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class ActivityLevel(Enum):
    SEDENTARY = 1.2
    LIGHT = 1.375
    MODERATE = 1.55
    ACTIVE = 1.725
    VERY_ACTIVE = 1.9

class BMI_Category(Enum):
    UNDERWEIGHT = "Underweight"
    NORMAL = "Normal weight"
    OVERWEIGHT = "Overweight"
    OBESE_I = "Obese Class I"
    OBESE_II = "Obese Class II"
    OBESE_III = "Obese Class III"

class BMICalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator & Calorie Goal Tracker")
        self.root.geometry("1100x700")
        self.root.resizable(True, True)
        
        self.current_age = None
        self.current_weight = None
        self.current_height = None
        
        self.setup_styles()
        self.create_widgets() 

    def setup_styles(self):
        """Configure styles for the GUI"""
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10))
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Result.TLabel', font=('Arial', 11, 'bold'))

    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        main_container = ttk.Frame(self.root, padding="10")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # LEFT SIDE - Input and Results
        left_frame = ttk.Frame(main_container)
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Title
        title_label = ttk.Label(left_frame, text="BMI Calculator & Calorie Goal Tracker", 
                               style='Header.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))
        
        # Personal Information Section
        personal_frame = ttk.LabelFrame(left_frame, text="Personal Information", padding="10")
        personal_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Age
        ttk.Label(personal_frame, text="Age (years):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.age_entry = ttk.Entry(personal_frame, width=10)
        self.age_entry.grid(row=0, column=1, sticky=tk.W, pady=2)
        
        # Height
        ttk.Label(personal_frame, text="Height (cm):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.height_entry = ttk.Entry(personal_frame, width=10)
        self.height_entry.grid(row=1, column=1, sticky=tk.W, pady=2)
        
        # Current Weight
        ttk.Label(personal_frame, text="Current Weight (kg):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.weight_entry = ttk.Entry(personal_frame, width=10)
        self.weight_entry.grid(row=2, column=1, sticky=tk.W, pady=2)
        
        # Goal Weight
        ttk.Label(personal_frame, text="Goal Weight (kg):").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.goal_weight_entry = ttk.Entry(personal_frame, width=10)
        self.goal_weight_entry.grid(row=3, column=1, sticky=tk.W, pady=2)
        
        # Gender
        ttk.Label(personal_frame, text="Gender:").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.gender_var = tk.StringVar(value="male")
        ttk.Radiobutton(personal_frame, text="Male", variable=self.gender_var, value="male", 
                       command=self.on_gender_change).grid(row=4, column=1, sticky=tk.W)
        ttk.Radiobutton(personal_frame, text="Female", variable=self.gender_var, value="female",
                       command=self.on_gender_change).grid(row=4, column=2, sticky=tk.W)
        
        # Activity Level Section
        activity_frame = ttk.LabelFrame(left_frame, text="Activity Level", padding="10")
        activity_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.activity_var = tk.StringVar(value="sedentary")
        activities = [
            ("Sedentary (office job, little exercise)", "sedentary"),
            ("Light (exercise 1-3 days/week)", "light"),
            ("Moderate (exercise 3-5 days/week)", "moderate"),
            ("Active (exercise 6-7 days/week)", "active"),
            ("Very Active (intense daily exercise)", "very_active")
        ]
        
        for i, (text, value) in enumerate(activities):
            ttk.Radiobutton(activity_frame, text=text, variable=self.activity_var, 
                           value=value).grid(row=i, column=0, sticky=tk.W, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(left_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Calculate", command=self.calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_form).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
        # Results Section
        results_frame = ttk.LabelFrame(left_frame, text="Results", padding="10")
        results_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # BMI Results
        ttk.Label(results_frame, text="Current BMI:", style='Result.TLabel').grid(row=0, column=0, sticky=tk.W, pady=2)
        self.current_bmi_label = ttk.Label(results_frame, text="", style='Result.TLabel')
        self.current_bmi_label.grid(row=0, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(results_frame, text="BMI Category:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.bmi_category_label = ttk.Label(results_frame, text="")
        self.bmi_category_label.grid(row=1, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(results_frame, text="Goal BMI:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.goal_bmi_label = ttk.Label(results_frame, text="")
        self.goal_bmi_label.grid(row=2, column=1, sticky=tk.W, pady=2)
        
        # Calorie Results
        ttk.Label(results_frame, text="BMR (Basal Metabolic Rate):").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.bmr_label = ttk.Label(results_frame, text="")
        self.bmr_label.grid(row=3, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(results_frame, text="TDEE (Total Daily Energy):").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.tdee_label = ttk.Label(results_frame, text="")
        self.tdee_label.grid(row=4, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(results_frame, text="Daily Calorie Goal:", style='Result.TLabel').grid(row=5, column=0, sticky=tk.W, pady=2)
        self.calorie_goal_label = ttk.Label(results_frame, text="", style='Result.TLabel')
        self.calorie_goal_label.grid(row=5, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(results_frame, text="Time to Goal:").grid(row=6, column=0, sticky=tk.W, pady=2)
        self.time_goal_label = ttk.Label(results_frame, text="")
        self.time_goal_label.grid(row=6, column=1, sticky=tk.W, pady=2)
        
        # RIGHT SIDE - Chart
        chart_frame = ttk.LabelFrame(main_container, text="BMI Chart - Weight Ranges by Age", padding="10")
        chart_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create canvas for chart
        self.chart_canvas = tk.Canvas(chart_frame, width=550, height=600, bg='white', 
                                    highlightthickness=1, highlightbackground='black')
        self.chart_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=0)
        main_container.columnconfigure(1, weight=1)
        main_container.rowconfigure(0, weight=1)
        
        self.draw_bmi_chart()

    def draw_bmi_chart(self):
        """Draw BMI chart in the main window"""
        self.chart_canvas.delete("all")
        
        # Chart dimensions
        chart_width = 480
        chart_height = 520
        margin_left = 60
        margin_top = 40
        
        # Draw chart border
        self.chart_canvas.create_rectangle(margin_left, margin_top, 
                                         margin_left + chart_width, margin_top + chart_height, 
                                         outline='black', width=2)
        
        # Get current gender for display
        current_gender = self.gender_var.get()
        
        # BMI categories - leicht angepasst für Frauen
        if current_gender == "female":
            bmi_categories = [
                (0, 18.5, "Underweight", "#87CEEB"),
                (18.5, 24, "Normal Weight", "#90EE90"),  
                (24, 29, "Overweight", "#FFFF00"),
                (29, 34, "Obese I", "#FFA500"),
                (34, 100, "Obese II/III", "#FF0000")
            ]
        else:  # male
            bmi_categories = [
                (0, 18.5, "Underweight", "#87CEEB"),
                (18.5, 25, "Normal Weight", "#90EE90"),  
                (25, 30, "Overweight", "#FFFF00"),
                (30, 35, "Obese I", "#FFA500"),
                (35, 100, "Obese II/III", "#FF0000")
            ]
        
        # Draw weight ranges for sample ages
        ages_to_show = list(range(15, 81, 3))
        total_years = len(ages_to_show)
        bar_width = chart_width / total_years
        
        # Standard height falls keine Eingabe
        display_height = self.current_height if self.current_height else 1.7
        
        for i, age in enumerate(ages_to_show):
            x_pos = margin_left + (i * bar_width) + (bar_width / 2)
            
            # Draw age label on x-axis
            if age % 15 == 0:
                self.chart_canvas.create_text(x_pos, margin_top + chart_height + 15, 
                                            text=str(age), font=('Arial', 9))
            
            for min_bmi, max_bmi, label, color in bmi_categories:
                min_weight = min_bmi * (display_height ** 2)
                max_weight = max_bmi * (display_height ** 2)
                
                # Limit weight range
                min_weight = max(0, min(min_weight, 150))
                max_weight = max(0, min(max_weight, 150))
                
                if min_weight < max_weight:
                    y_min = margin_top + chart_height - (min_weight / 150) * chart_height
                    y_max = margin_top + chart_height - (max_weight / 150) * chart_height
                    
                    # Draw the weight range bar
                    self.chart_canvas.create_rectangle(
                        x_pos - bar_width/2, y_max,
                        x_pos + bar_width/2, y_min,
                        fill=color, outline=color, width=0
                    )
        
        # Draw Y-axis labels
        for weight in [0, 30, 60, 90, 120, 150]:
            y_pos = margin_top + chart_height - (weight / 150) * chart_height
            self.chart_canvas.create_text(margin_left - 10, y_pos, text=str(weight), 
                                        font=('Arial', 9), anchor='e')
            # Grid line
            self.chart_canvas.create_line(margin_left, y_pos, margin_left + chart_width, y_pos,
                                        fill='lightgray', dash=(2, 2))
        
        # Draw axes labels with gender info
        gender_text = "Male" if current_gender == "male" else "Female"
        self.chart_canvas.create_text(margin_left + chart_width/2, margin_top + chart_height + 35, 
                                    text=f"Age (years) - {gender_text}", font=('Arial', 10, 'bold'))
        self.chart_canvas.create_text(25, margin_top + chart_height/2, text="Weight (kg)", 
                                    font=('Arial', 10, 'bold'), angle=90)
        
        # Punkt zeichnen wenn Daten vorhanden
        if self.current_age and self.current_weight and self.current_height:
            current_age_index = (self.current_age - 15) // 3
            if 0 <= current_age_index < len(ages_to_show):
                current_x = margin_left + (current_age_index * bar_width) + (bar_width / 2)
                current_y = margin_top + chart_height - (self.current_weight / 150) * chart_height
                
                self.chart_canvas.create_oval(current_x - 6, current_y - 6, current_x + 6, current_y + 6, 
                                            fill='blue', outline='darkblue', width=3)
                self.chart_canvas.create_text(current_x, current_y - 15, text="You", 
                                            font=('Arial', 9, 'bold'), fill='blue')
        
        # Draw legend
        legend_x = margin_left + 10
        legend_y = margin_top + 10
        
        for i, (min_bmi, max_bmi, label, color) in enumerate(bmi_categories):
            y_pos = legend_y + i * 20
            self.chart_canvas.create_rectangle(legend_x, y_pos, legend_x + 15, y_pos + 15, 
                                            fill=color, outline='black')
            bmi_range = f"BMI {min_bmi}-{max_bmi if max_bmi < 100 else '40+'}"
            self.chart_canvas.create_text(legend_x + 20, y_pos + 7, text=f"{label} ({bmi_range})", 
                                        font=('Arial', 8), anchor='w')

    def calculate_bmi(self, weight, height):
        """Calculate BMI based on weight and height"""
        bmi = weight / (height ** 2)
        return round(bmi, 1)
    
    def get_bmi_category(self, bmi):
        """Determine BMI category based on WHO standards"""
        if bmi < 18.5:
            return BMI_Category.UNDERWEIGHT
        elif 18.5 <= bmi < 25:
            return BMI_Category.NORMAL
        elif 25 <= bmi < 30:
            return BMI_Category.OVERWEIGHT
        elif 30 <= bmi < 35:
            return BMI_Category.OBESE_I
        elif 35 <= bmi < 40:
            return BMI_Category.OBESE_II
        else:
            return BMI_Category.OBESE_III

    def calculate_bmr(self, weight, height_cm, age, gender):
        """Calculate Basal Metabolic Rate using Harris-Benedict formula"""
        if gender == "male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)
        return round(bmr)
    
    def get_activity_multiplier(self, activity_level):
        """Get activity multiplier based on selected level"""
        activity_map = {
            "sedentary": ActivityLevel.SEDENTARY,
            "light": ActivityLevel.LIGHT,
            "moderate": ActivityLevel.MODERATE,
            "active": ActivityLevel.ACTIVE,
            "very_active": ActivityLevel.VERY_ACTIVE
        }
        return activity_map[activity_level].value
    
    def calculate_calorie_goal(self, current_weight, goal_weight, tdee):
        """Calculate calorie goal and time to reach target weight"""
        weight_difference = goal_weight - current_weight
        calories_per_kg = 7000
        
        if weight_difference < 0:  # Weight loss
            calorie_goal = tdee - 500
            weeks_to_goal = abs(weight_difference) * calories_per_kg / (500 * 7)
        elif weight_difference > 0:  # Weight gain
            calorie_goal = tdee + 300
            weeks_to_goal = abs(weight_difference) * calories_per_kg / (300 * 7)
        else:  # Weight maintenance
            calorie_goal = tdee
            weeks_to_goal = 0
        
        return {
            'calorie_goal': round(calorie_goal),
            'weeks_to_goal': round(weeks_to_goal, 1),
            'weight_difference': weight_difference
        }
    
    def validate_input(self):
        """Validate all user inputs"""
        try:
            age = int(self.age_entry.get())
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            goal_weight = float(self.goal_weight_entry.get())
            
            if age <= 0 or height <= 0 or weight <= 0 or goal_weight <= 0:
                raise ValueError("Values must be positive")
                
            if height > 300:
                raise ValueError("Please enter height in centimeters")
                
            return True, (age, height, weight, goal_weight)
            
        except ValueError as e:
            return False, str(e)
    
    def calculate(self):
        """Main calculation function"""
        is_valid, result = self.validate_input()
        if not is_valid:
            messagebox.showerror("Input Error", f"Please check your input:\n{result}")
            return
        
        age, height_cm, weight, goal_weight = result
        height_m = height_cm / 100
        gender = self.gender_var.get()
        activity_level = self.activity_var.get()
        
        # Store for plotting
        self.current_age = age
        self.current_weight = weight
        self.current_height = height_m
        
        # Calculate BMI
        current_bmi = self.calculate_bmi(weight, height_m)
        bmi_category = self.get_bmi_category(current_bmi)
        goal_bmi = self.calculate_bmi(goal_weight, height_m)
        
        # Calculate BMR and TDEE
        bmr = self.calculate_bmr(weight, height_cm, age, gender)
        activity_multiplier = self.get_activity_multiplier(activity_level)
        tdee = round(bmr * activity_multiplier)
        
        # Calculate calorie goal
        calorie_data = self.calculate_calorie_goal(weight, goal_weight, tdee)
        
        # Update results labels
        self.current_bmi_label.config(text=f"{current_bmi}")
        self.bmi_category_label.config(text=f"{bmi_category.value}")
        self.goal_bmi_label.config(text=f"{goal_bmi}")
        self.bmr_label.config(text=f"{bmr} kcal/day")
        self.tdee_label.config(text=f"{tdee} kcal/day")
        self.calorie_goal_label.config(text=f"{calorie_data['calorie_goal']} kcal/day")
        
        # Set time to goal
        if calorie_data['weight_difference'] == 0:
            self.time_goal_label.config(text="Maintain current weight")
        elif calorie_data['weight_difference'] < 0:
            self.time_goal_label.config(text=f"{calorie_data['weeks_to_goal']} weeks to lose {abs(calorie_data['weight_difference']):.1f} kg")
        else:
            self.time_goal_label.config(text=f"{calorie_data['weeks_to_goal']} weeks to gain {calorie_data['weight_difference']:.1f} kg")
        
        self.draw_bmi_chart()

    def clear_form(self):
        """Clear all input fields and results"""
        self.age_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.goal_weight_entry.delete(0, tk.END)
        self.gender_var.set("male")
        self.activity_var.set("sedentary")
        
        self.current_age = None
        self.current_weight = None
        self.current_height = None
        
        self.current_bmi_label.config(text="")
        self.bmi_category_label.config(text="")
        self.goal_bmi_label.config(text="")
        self.bmr_label.config(text="")
        self.tdee_label.config(text="")
        self.calorie_goal_label.config(text="")
        self.time_goal_label.config(text="")
        
        self.draw_bmi_chart()
    
    def on_gender_change(self):
        """Called when gender selection changes"""
        self.draw_bmi_chart()

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = BMICalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()