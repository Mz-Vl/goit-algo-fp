import random
from collections import Counter

outcomes = Counter()


def monte_carlo_simulation(num_trials):
    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        outcomes[total] += 1

    probabilities = {key: value / num_trials * 100 for key, value in outcomes.items()}
    return probabilities


def print_probabilities(probabilities):
    print("Sum |\tProbability %")
    print("--------------------------------")
    for total, probability in sorted(probabilities.items()):
        probability_str = f"{probability:.2f}%".ljust(9)
        print(f"{total}\t{probability_str} ({outcomes[total]:,}/{num_trials:,})")


# Number of simulation iterations
num_trials = 100000

# Run the simulation
probabilities = monte_carlo_simulation(num_trials)

# Results
print_probabilities(probabilities)
