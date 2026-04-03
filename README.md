# Reggie's Linear Regression Analysis

## Project Overview
This project implements a machine learning foundation—Linear Regression—from scratch using Python. The objective was to analyze experimental data regarding bouncy ball widths and their corresponding bounce heights to identify a line of best fit. This model allows for data-driven predictions of bounce heights for ball sizes not included in the original dataset.

## Technical Implementation
Unlike standard data analysis that relies on external libraries, this project focuses on the core logic of predictive modeling:
* **Error Calculation:** Developed functions to determine the precision of a model by calculating the distance between data points and the regression line.
* **Optimization:** Implemented a grid-search approach using nested loops to iterate through thousands of potential slopes and intercepts.
* **List Comprehensions:** Leveraged advanced Python syntax to generate precise ranges of floating-point values for model testing.

## Results and Findings
The optimization process identified the following parameters for the line of best fit:
* **Optimal Slope (m):** 0.4
* **Optimal Intercept (b):** 1.6
* **Model Accuracy:** The minimum total error achieved was 5.0.

### Predictive Analysis
Based on the final model, a ball with a width of **6cm** is predicted to have a bounce height of **4.0 meters**.

## Tools Used
* Python 3
* Visual Studio Code
* Git/GitHub for version control
