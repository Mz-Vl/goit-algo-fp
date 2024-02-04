# goit-algo-fp

### t1_data_structures.py
Data Structures, Sorting, and Linked List Operations

### t2_pythagorean_tree.py
Recursion. Creation of the "Pythagoras tree" fractal using recursion

### t3_dijkstra_algorithm.py
Trees, Dijkstra's algorithm

### t4_pyramid_visualization.py
Visualization of the pyramid

### t5_binary_tree_visualization.py
Binary tree traversal visualization

### t6_greedy_dynamic_prog.py
Greedy algorithms and dynamic programming

### t7_monte_carlo.py
Using the Monte Carlo method
### Table of probabilities of sums when throwing two dice
```
Sum	Probability
2	2.78% (1/36)
3	5.56% (2/36)
4	8.33% (3/36)
5	11.11% (4/36)
6	13.89% (5/36)
7	16.67% (6/36)
8	13.89% (5/36)
9	11.11% (4/36)
10	8.33% (3/36)
11	5.56% (2/36)
12	2.78% (1/36)
```

The results obtained by the Monte Carlo method with the analytical values:

For the sum of 2, the analytical probability is 2.78%, with Monte Carlo - 2.71%. The results are very close.

For the sum of 3, the analytical probability is 5.56%, Monte Carlo - 5.57%. Almost ideal match.

For all other sums (4-12), the Monte Carlo and analytical results are also very close.

So, the results obtained by the statistical simulation Monte Carlo method correlate well with the analytical probability values for this problem.

The Monte Carlo method allows to get a good approximation to the exact analytical solution for a sufficiently large number of simulations (100,000 in this case). This confirms the effectiveness of this method for statistical modeling of complex systems.

Therefore, the simulation results and analytical calculations are consistent, so the Monte Carlo method is applied correctly.

### Result:
```
Sum |   Probability %
--------------------------------
2	2.71%     (2,712/100,000)
3	5.57%     (5,567/100,000)
4	8.33%     (8,335/100,000)
5	10.96%    (10,963/100,000)
6	13.94%    (13,936/100,000)
7	16.59%    (16,590/100,000)
8	13.97%    (13,966/100,000)
9	11.12%    (11,124/100,000)
10	8.37%     (8,365/100,000)
11	5.63%     (5,634/100,000)
12	2.81%     (2,808/100,000)```