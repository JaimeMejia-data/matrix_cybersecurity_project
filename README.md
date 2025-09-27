Matrix Cybersecurity Analysis
Overview

This project analyzes global cybersecurity threats using a dataset from Kaggle. The goal is to extract meaningful insights from the data using SQL and Python, visualize trends, and present them in a creative, Matrix-style animation. It combines data analytics with engaging visualization to make the findings both informative and visually appealing.

Project Goals

Analyze cybersecurity incidents across industries, attack types, and affected users.

Identify trends in incident resolution times, financial losses, and vulnerabilities.

Visualize key insights through charts and a Matrix-style digital rain animation.

Repository Structure

data/ – Original CSV dataset

scripts/ – Python scripts for analysis and visualization

cybersecurity_analytics.py – SQL + Python workflow & plots

matrix_animation.py – Matrix-style animation using data

results/ – Generated plots and outputs

README.md – Project overview and instructions

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
