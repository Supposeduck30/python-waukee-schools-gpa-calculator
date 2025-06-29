# GPA Calculator for WCSD

## A fully functional easy to use GPA calculator written in python that calculates weighted cumulative GPA for the Waukee Community School District

This project was built with no external libraries at all. This GPA calculator will:
- Ask you how many classes you have taken 
- Ask you how many AP classes you have taken
- Ask you your letter grade in every class
- Calculate your cumulative weighted gpa as it would be in the WCSD district 

## 🕓 Version History
### 1.0.0 
- Terminal based
- Input for AP classes and input for classes
- Input for percentage grade of however many classes were inputted

### 1.1.0 
- Input for grade changed to letter grades instead of percentages to account for rounding
- Changed code format to be shorter and more efficient 

## 💻 How to run this project
1. Ensure python is installed on your device (You can verify this by running the command "python --version" in your terminal/command prompt")

2. Download the script
- If you have git installed, run
```
  git clone https://github.com/Supposeduck30/GPACalculatorForWCSD.git
  ```
- Or, you can click the green code button and press download zip, then extract it

3. Inside of the directory, find the file named GPACalculator.py

4. Open your terminal/command prompt, and execute
```
   python GPACalculator.py
  ```
6. ALTERNATIVE - If you don't want to run the script locally, you can paste the code into an online python compiler (https://www.programiz.com/python-programming/online-compiler/)

#### THE CODE IS IN THE .py FILE INSIDE OF THE FOLDER


## 🔧 How to tweak this project for your own uses 
1. Fork the repository
   
2. Clone the fork
   
3. Make your changes to the code
   
4. Commit and push your changes to the fork
   
5. OPTIONAL - Create a pull request if you want the main repository to change the code with what you changed 

## 🧮 How it works 
- The code just runs the same function (the function that returns the gpa value from a letter grade) the same number times you have classes (which is inputted by the user)
- It then adds the result of that function to total GPA
- The number of AP classes * .5 is also added into the total
- That total then gets divided by the total number of classes

## ![image](https://github.com/user-attachments/assets/4b876f8e-069a-48ac-a344-44da6317453a)

## Output
```
How many classes have you taken? 8
How many of those were AP? 1
Enter the letter grade for class 1: A+
Enter the letter grade for class 2: a+
Enter the letter grade for class 3: a+
Enter the letter grade for class 4: a+
Enter the letter grade for class 5: a+
Enter the letter grade for class 6: a+
Enter the letter grade for class 7: a
Enter the letter grade for class 8: a
Your GPA is: 4.31
```
## ⚠️ Known Issues 
- The result after calculating the GPA is rounded up to 3 decimal 
- How WCSD works is that if a class is 2 semesters (9th) or 2 terms (10-12th), it calculates it as 2 seperate classes, so input accordingly 



## ⚖️ LICENSE
### MIT LICENSE
