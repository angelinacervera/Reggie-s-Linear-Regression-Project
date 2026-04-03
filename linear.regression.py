"""
Reggie's Linear Regression Project
Author: Angelina Cervera
Objective: Determine the line of best fit for bouncy ball data.
"""

def get_y(m, b, x):
    """Calculates the y-value for a given slope, intercept, and x-coordinate."""
    return m * x + b

def calculate_error(m, b, point):
    """Calculates the absolute distance between a data point and a specific line."""
    x_point, y_point = point[0], point[1]
    y_predicted = get_y(m, b, x_point)
    return abs(y_predicted - y_point)

def calculate_all_error(m, b, points):
    """Returns the cumulative error for a line across an entire dataset."""
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error

# --- Optimization Setup ---

# Task 8 & 9: Generate possible slopes and intercepts using list comprehensions
possible_ms = [m * 0.1 for m in range(-100, 101)]
possible_bs = [b * 0.1 for b in range(-200, 201)]

# Task 5: Experimental Data
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def find_best_fit(ms, bs, data):
    """Iterates through all possible lines to find the one with the smallest error."""
    smallest_error = float("inf")
    best_m = 0
    best_b = 0

    for m in ms:
        for b in bs:
            current_error = calculate_all_error(m, b, data)
            if current_error < smallest_error:
                smallest_error = current_error
                best_m = m
                best_b = b
                
    return best_m, best_b, smallest_error

# --- Execution ---

if __name__ == "__main__":
    # Perform the optimization
    m_final, b_final, error_final = find_best_fit(possible_ms, possible_bs, datapoints)
    
    # Task 12: Display Model Results
    print("--- Linear Regression Results ---")
    print(f"Best Slope (m):     {m_final:.2f}")
    print(f"Best Intercept (b): {b_final:.2f}")
    print(f"Minimum Error:      {error_final:.2f}")
    
    # Task 13: Prediction for a 6cm bouncy ball
    prediction = get_y(m_final, b_final, 6)
    print(f"\nPrediction: A 6cm ball is expected to bounce {prediction:.1f} meters.")