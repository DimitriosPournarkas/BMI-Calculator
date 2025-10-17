# BMI Calculator & Calorie Goal Tracker

A comprehensive BMI (Body Mass Index) calculator with calorie tracking and visual weight range analysis. This desktop application helps users monitor their health metrics and plan their fitness goals.

## Features

- 📊 **BMI Calculation**: Calculate current and goal BMI based on height and weight
- 🎯 **Calorie Goal Tracking**: Get personalized daily calorie recommendations
- 📈 **Visual Weight Chart**: Dynamic chart showing healthy weight ranges by age
- 👥 **Gender-Specific Analysis**: Adjusted BMI categories for male and female users
- 🏃 **Activity Level Integration**: Calculates TDEE based on 5 activity levels
- ⏱️ **Goal Timeline**: Estimates time needed to reach your target weight
- 🎨 **User-Friendly Interface**: Clean, modern GUI with side-by-side layout

## Screenshots

![BMI Calculator Interface](screenshot.png)
*Main interface showing input fields and dynamic weight chart*

## Installation

### Requirements

- Python 3.7 or higher
- tkinter (usually comes with Python)
- matplotlib
- numpy

## Usage

1. **Enter Personal Information**:
   - Age (years)
   - Height (cm)
   - Current Weight (kg)
   - Goal Weight (kg)
   - Select Gender (Male/Female)

2. **Select Activity Level**:
   - Sedentary (office job, little exercise)
   - Light (exercise 1-3 days/week)
   - Moderate (exercise 3-5 days/week)
   - Active (exercise 6-7 days/week)
   - Very Active (intense daily exercise)

3. **Click Calculate** to see:
   - Current BMI and category
   - Goal BMI
   - BMR (Basal Metabolic Rate)
   - TDEE (Total Daily Energy Expenditure)
   - Recommended daily calorie goal
   - Estimated time to reach goal weight
   - Your position on the weight chart

## BMI Categories

### Male
- Underweight: BMI < 18.5
- Normal Weight: BMI 18.5 - 25
- Overweight: BMI 25 - 30
- Obese Class I: BMI 30 - 35
- Obese Class II/III: BMI > 35

### Female
- Underweight: BMI < 18.5
- Normal Weight: BMI 18.5 - 24
- Overweight: BMI 24 - 29
- Obese Class I: BMI 29 - 34
- Obese Class II/III: BMI > 34

## Calculations

- **BMI**: weight (kg) / height² (m)
- **BMR** (Harris-Benedict Formula):
  - Male: 88.362 + (13.397 × weight) + (4.799 × height) - (5.677 × age)
  - Female: 447.593 + (9.247 × weight) + (3.098 × height) - (4.330 × age)
- **TDEE**: BMR × Activity Level Multiplier
- **Calorie Goal**: 
  - Weight loss: TDEE - 500 kcal
  - Weight gain: TDEE + 300 kcal
  - Maintenance: TDEE



## License

This project is licensed under the MIT License - see the [LICENSE](License) file for details.

## Acknowledgments

- BMI categories based on WHO standards
- Harris-Benedict Formula for BMR calculation
- Activity level multipliers from fitness research



---

⭐ If you find this project helpful, please consider giving it a star!
