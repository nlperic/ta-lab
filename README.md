# Introduction

[TA-lab](https://github.com/nlperic/ta-lab) is a tool to assign travel demand to network following the user equilibrium principle. It has the following components which enable it to do pathfinding and path flow updating

- 'shortest_path' and 'kspp_yen' implements Dijkstra algorithm for shortest path and Yen's algorithm for finding K-shortest path.
- 'graph' deals with the network structure, it is independent with the 'networkx' package
- 'line' gives a bi-section search method to determine the step size of line search
- 'assign' is the main operator to map OD demand to path flow. There are two options: MSA and Frank-Wolfe.

# Dependencies

This project is done purely in Python and depends on 'numpy' package for matrix operations.

# Version and updates

This project is finished in May, 2016. I won't update it in the future.

# Contact

If there were any questions regarding this project, please contact [geqian@outlook.com](mailto:geqian@outlook.com). For more information about the author, you may check [my website](https://nlperic.github.io/) for details.
