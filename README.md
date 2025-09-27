Matrix Cybersecurity Analysis
Overview

This project analyzes global cybersecurity threats using a dataset from Kaggle. The goal is to extract meaningful insights from the data using SQL and Python, visualize trends, and present them in a creative, Matrix-style animation. It combines data analytics with engaging visualization to make the findings both informative and visually appealing.

Project Goals

Analyze cybersecurity incidents across industries, attack types, and affected users.

Identify trends in incident resolution times, financial losses, and vulnerabilities.

Visualize key insights through charts and a Matrix-style digital rain animation.

Repository Structure
├── data/                 # Original CSV dataset
├── scripts/              # Python scripts for analysis and visualization
│   ├── cybersecurity_analytics.py  # SQL + Python workflow & plots
│   └── matrix_animation.py         # Matrix-style animation using data
├── results/              # Generated plots and outputs
└── README.md             # Project overview and instructions

Workflow

Data Preparation

Dataset downloaded from Kaggle.

Cleaned and preprocessed using pandas (columns standardized, missing values handled).

SQL Analysis

Connected to a local SQL Server using pyodbc.

Ran queries to answer questions such as:

Total incidents per year

Average resolution time by attack type

Top 5 industries with the highest financial loss

Correlation of affected users vs. financial loss

Vulnerability types and defense mechanisms

Python Visualization

Converted SQL results into Pandas DataFrames.

Generated visualizations using matplotlib and seaborn.

Charts include line plots, bar plots, scatter plots, and grouped bar plots.

Matrix-style Animation

Used pygame to create a digital rain effect.

Animated Number_of_Affected_Users from the dataset along with alphanumeric characters.

Title “Cybersecurity Matrix” displayed at the top for context.

How to Run

Clone the repository:

git clone https://github.com/yourusername/matrix-cybersecurity.git


Install required packages:

pip install pandas matplotlib seaborn pyodbc pygame


Update file paths in cybersecurity_analytics.py and matrix_animation.py as needed.

Run scripts:

python cybersecurity_analytics.py   # Generates plots from SQL queries
python matrix_animation.py          # Launches Matrix-style animation

Key Learnings

Hands-on experience integrating SQL queries with Python for data analysis.

Learned to visualize data effectively using multiple chart types.

Explored creative ways to present data through animations.

Developed a full end-to-end workflow: data → analysis → visualization → interactive presentation.

Notes

All scripts and outputs are included in a single commit for simplicity.
