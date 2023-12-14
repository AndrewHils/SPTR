import numpy as np

def northwest_corner_method(supply, demand, costs):
    rows, cols = len(supply), len(demand)
    allocations = np.zeros((rows, cols))

    i, j = 0, 0

    while i < rows and j < cols:
        quantity = min(supply[i], demand[j])
        allocations[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity

        if supply[i] == 0:
            i += 1

        if demand[j] == 0:
            j += 1

    return allocations, np.sum(allocations * costs)

def main():
    supply = [200, 450, 250]
    demand = [100, 125, 325, 250, 100]
    costs = np.array([
        [5, 8, 7, 10, 3],
        [4, 2, 2, 5, 6],
        [7, 3, 5, 9, 2]
    ])

    allocations, total_cost = northwest_corner_method(supply, demand, costs)
    print("Allocations:")
    print(allocations)
    print(f"\nTotal Cost: {total_cost}")

if __name__ == '__main__':
    main()
