# GPA Calculator for WCSD

## A fully functional easy to use GPA calculator written in python that calculates weighted cumulative GPA for the Waukee Community Schools District

This project was built with no external libraries at all. This GPA calculator will:
- Ask you how many classes you have taken 
- Ask you how many AP classes you have taken
- Ask you your percentage grade in every class
- Calculate your cumulative weighted gpa as it would be in the WCSD district 

## 💻 How to run this project
1. Ensure python is installed on your device (You can verify this by running the command "python --version" in your terminal/command prompt")

2. Download the script
- If you have git installed, run "git clone https://github.com/Supposeduck30/GPACalculatorForWCSD.git" in your command prompt/termimal"
- Or, you can click the green code button and press download zip, then extract it

3. Inside of the directory, find the file named GPACalculator.py

4. Open your terminal/command prompt, and execute "python GPACalculator.py"

5. ALTERNATIVE - If you don't want to run the script locally, you can paste the code into an online python compiler (https://www.programiz.com/python-programming/online-compiler/)

#### THE CODE IS IN THE .py FILE INSIDE OF THE FOLDER


## 🛠️ How to tweak this project for your own uses 
1. Fork the repository
   
2. Clone the fork
   
3. Make your changes to the code
   
4. Commit and push your changes to the fork
   
5. OPTIONAL - Create a pull request if you want the main repository to change the code with what you changed 

## How it works 
- The code just runs the same function (the function that returns the gpa value from a percentage) the same number times you have classes (which is inputted by the user)
- It then adds the result of that function to total GPA
- The number of AP classes * 5 is also added into the total
- That total then gets divided by the total number of classes

## ![image](https://github.com/user-attachments/assets/4b876f8e-069a-48ac-a344-44da6317453a)

## Screenshot
## ![image](https://github.com/user-attachments/assets/5c5dbeb1-081a-4180-99cf-4f35bec7eb23)



## Known Issues 
- The result after calculating the GPA is rounded up to 3 decimal places
- If negative numbers are input, the calculation won't work but it won't submit an error
- Entering a non number will result in an error
- If your teacher rounded your letter grade but kept your percentage the same, then just input the percentage of your new letter grade for accurate results
