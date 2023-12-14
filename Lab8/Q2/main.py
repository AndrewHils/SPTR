import numpy as np

def northwest_corner(supply, demand):
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

    return allocations


def transportation_potential(supply, demand, costs):
    num_supply = len(supply)
    num_demand = len(demand)

    u = np.zeros(num_supply)
    v = np.zeros(num_demand)

    initial_solution = northwest_corner(supply.copy(), demand.copy())

    modified_costs = np.copy(costs)

    for _ in range(num_supply + num_demand - 1):
        for i in range(num_supply):
            for j in range(num_demand):
                if initial_solution[i, j] > 0:
                    modified_costs[i, j] = costs[i, j] - u[i] - v[j]

        min_cost = np.min(modified_costs)
        min_indices = np.argwhere(modified_costs == min_cost)[0]

        u[min_indices[0]] += min_cost
        v[min_indices[1]] += min_cost

    final_solution = northwest_corner(supply.copy(), demand.copy())

    return final_solution, u, v


def main():
    supply = [350, 330, 270]
    demand = [210, 170, 220, 150, 200]
    costs = np.array([
        [3, 12, 9, 1, 7],
        [2, 4, 11, 2, 10],
        [7, 14, 12, 5, 8]
    ])

    optimal_solution, u_potential, v_potential = transportation_potential(supply, demand, costs)

    print("Optimal Transportation Plan:")
    print(optimal_solution)
    print("\nPotentials u:", u_potential)
    print("Potentials v:", v_potential)


if __name__ == '__main__':
    main()
