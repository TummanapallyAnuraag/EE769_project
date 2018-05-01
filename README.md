# EE769_project
Implementation of DB-SCAN Algorithm from scratch

# Execution
Please run the following command in terminal.
`python main.py`

```
Note: Double check that the branch which you are cloning or downloading is "master" branch
```
# What is DBSCAN Actually?
DBSCAN is not any scanner, though it seems so :P .

**DBSCAN - Density Based Spatial Clustering of Applications with Noise** is a data clustering algorithm proposed by Martin Ester, Hans-Peter Kriegel, Jörg Sander and Xiaowei Xu in 1996.


# Requirements
Following Python packages are required
* numpy
* pandas
* MinMaxScaler (form SciKit learn)
* pyplot from matplotlib
* Axes3D from mpl_toolkits.mplot3d

# About code
DBSCAN.py is the code for DBSCAN class and algorithm

main.py is the one to be run for simulation, csv file for input is in "data" folder

# References
* We have gone through the code from this [Repo](https://github.com/madhug-nadig/Machine-Learning-Algorithms-from-Scratch)

* The following [Wiki Page](https://en.wikipedia.org/wiki/DBSCAN) was helpful in understanding the Algorithm

* Slides from EE769 Lectures (2018)

# Data
We have implemented DBSCAN Algorithm from scratch, and tried to use this algorithm on a "GasEmissions" data of all sates in India

[Source: Research Gate]

# Future Work
We can also make a Web Page and have a live demo of DBSCAN Algorithm, `checkout to Python_Web branch` to check that, but it is still in development though... you are always welcome to collaborate, just get in contact with the authors.

# FAQs
* Did you know that `pip install --user numpy` will install numpy only for the current user
