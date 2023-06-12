#Get all permutations for brute force
def get_strings(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def bruteforce(values,weights,capacity):
    n=len(values)

    # Generate all possible bit strings of length n
    bit_strings = get_strings(n)

    max_profit = 0

    for k in bit_strings:

        # Calculate the profit and weight for the current bit string
        profit = sum([int(k[i]) * values[i] for i in range(n)])
        weight = sum([int(k[i]) * weights[i] for i in range(n)])

        if weight <= capacity and profit > max_profit:
            max_profit = profit
    
    return max_profit

def fracbruteforce(values, weights, capacity):
    n = len(values)
    bit_strings = get_strings(n)

    max_profit = 0

    for k in bit_strings:
       
        profit = 0
        weight = 0

        for i in range(n):

            #Check if the bit is 1
            if k[i] == '1':
                # Add the entire item if weight allows
                if weights[i] <= capacity - weight:
                    profit += values[i]
                    weight += weights[i]
                else:
                    # Add a fraction of the item to fill the remaining capacity
                    fraction = (capacity - weight) / weights[i]
                    profit += fraction * values[i]
                    weight = capacity
                    break

        if profit > max_profit:
            max_profit = profit
           
    return max_profit


def fracgreedy(values, weights, capacity):

    items = [(value, weight) for value, weight in zip(values, weights)]
    items.sort(key=lambda x: x[0] / x[1], reverse=True)  # Sort items based on value-to-weight ratio

    total_value = 0
    remaining_capacity = capacity

    for value, weight in items:
        if weight <= remaining_capacity:
            # Add the entire item to the knapsack
            total_value += value
            remaining_capacity -= weight
        else:
            # Add a fraction of the item to the knapsack
            fraction = remaining_capacity / weight
            total_value += fraction * value
            break  # No more items can be added

    return total_value