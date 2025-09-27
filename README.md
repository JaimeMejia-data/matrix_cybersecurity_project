# Matrix Cybersecurity Data Analysis

## Overview
This project analyzes global cybersecurity threats using a dataset from Kaggle. SQL and Python were used to extract insights and visualize trends in attack types, financial losses, and vulnerabilities. Additionally, a Matrix-style digital rain animation was created as a creative way to display raw data from the dataset.

## Dataset
Source: https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024

Features include: Year, Attack Type, Target Industry, Number of Affected Users, Financial Loss, Incident Resolution Time, Vulnerability Types, Defense Mechanisms

Methods
Data Cleaning & Preprocessing: Python (pandas)

SQL Queries:
- Total incidents per year
- Average resolution time by attack type
- Top 5 industries by financial loss
- Average affected users vs financial loss
- Vulnerability types and defense mechanisms usage

Visualization: matplotlib & seaborn
Line plots, bar charts, scatter plots, grouped bar plots

Animation: pygame for Matrix-style digital rain using dataset characters

## Results

Key Insights:

- Trends in incident counts over the years
- Industries with the highest financial losses
- Attack types with longest resolution times
- Relationships between affected users and financial losses
- Most common vulnerabilities and defense mechanisms
- Visualizations and animation make patterns easy to understand and engaging

## How to Run
1. Clone the repo:
`git clone https://github.com/yourusername/matrix_cybersecurity_project.git cd matrix_cybersecurity_project`
2. Install dependencies:
`pip install -r requirements.txt`
3. Place the dataset file (global_cybersecurity_threats.csv) in the project folder.
4. Run the SQL + Python Analytics:
`python Cybersecurity_analytics.py`
5. Run the Matrix-style digital rain animation:
`python matrix_animation.py`


  
