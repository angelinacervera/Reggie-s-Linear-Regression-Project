"""
Reggie's Linear Regression Project
Author: Angelina Cervera
"""

def get_y(m, b, x):
    return m * x + b

def calculate_error(m, b, point):
    x_point, y_point = point[0], point[1]
    y_predicted = get_y(m, b, x_point)
    return abs(y_predicted - y_point)

def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error

# --- Optimization ---
possible_ms = [m * 0.1 for m in range(-100, 101)]
possible_bs = [b * 0.1 for b in range(-200, 201)]
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def find_best_fit(ms, bs, data):
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

if __name__ == "__main__":
    m_final, b_final, error_final = find_best_fit(possible_ms, possible_bs, datapoints)
    
    print("--- Linear Regression Results ---")
    print(f"Best Slope (m):     {m_final:.2f}")
    print(f"Best Intercept (b): {b_final:.2f}")
    print(f"Minimum Error:      {error_final:.2f}")
    
    prediction = get_y(m_final, b_final, 6)
    print(f"\nPrediction: A 6cm ball is expected to bounce {prediction:.1f} meters.")
