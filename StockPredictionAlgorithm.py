def calculate_stock_price():
    print("Stock Price Prediction Model")
    
    P0 = float(input("Enter the initial stock price (P0): "))
    
    n = int(input("How many variables do you want to include? "))
    
    total_sum = 0
    variables = []
    totalWeight = 1
    # Collection loop
    for i in range(n):
        print(f"\nVariable {i+1}:")
        
        name = input(f"Enter variable name: ")
        while True:
            print(f"Total weight must add up to 1.")
            print(f"Weight available: {totalWeight}")
            
            weight = float(input(f"Enter weight for {name}: "))
            
            if weight > 1:
                print("Error: weight cannot be greater than 1.")
            elif weight > totalWeight:
                print("Error: exceeds remaining weight.")
            else:
                break
        print("Value EX: 1.2 = 20% increase")
        value = float(input(f"Enter value for {name}: "))
        
        contribution = weight * value
        total_sum += contribution
        
        variables.append((name, weight, value, contribution))
    
    Pf = P0 * total_sum
    
    print("--- Calculation Breakdown ---")
    for var in variables:
        print(f"{var[0]}: weight={var[1]}, value={var[2]}, contribution={var[3]}")
    
    print(f"Predicted Stock Price (Pf) = {Pf}")
    
    return Pf
calculate_stock_price()