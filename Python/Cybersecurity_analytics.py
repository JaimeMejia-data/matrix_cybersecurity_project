# Cybersecurity_analytics.py
# Full workflow: SQL queries -> pandas -> visualizations using pyodbc

import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1️⃣ SQL Server Connection
# -------------------------------
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-PACA0KO\\SQLEXPRESS01;"  
    "DATABASE=global_cybersecurity_threats;" 
    "Trusted_Connection=yes;"
)

# -------------------------------
# 2️⃣ Define SQL Queries
# -------------------------------
queries = {
    "IncidentsPerYear": """
        SELECT Year, COUNT(*) AS Total_Incidents
        FROM dbo.global_cybersecurity_threats
        GROUP BY Year
        ORDER BY Year;
    """,
    "ResolutionTime": """
        SELECT Attack_Type, AVG(Incident_Resolution_Time_in_Hours) AS Avg_Resolution_Time
        FROM dbo.global_cybersecurity_threats
        GROUP BY Attack_Type
        ORDER BY Avg_Resolution_Time;
    """,
    "TopIndustries": """
        SELECT TOP 5 Target_Industry, SUM(Financial_Loss_in_Million) AS Total_Financial_Loss
        FROM dbo.global_cybersecurity_threats
        GROUP BY Target_Industry
        ORDER BY Total_Financial_Loss DESC;
    """,
    "AvgAffectedVsLoss": """
        SELECT Attack_Type,
               AVG(Number_of_Affected_Users) AS Avg_Affected_Users,
               AVG(Financial_Loss_in_Million) AS Avg_Financial_Loss
        FROM dbo.global_cybersecurity_threats
        GROUP BY Attack_Type
        ORDER BY Avg_Financial_Loss DESC;
    """,
    "VulnerabilityDefense": """
        SELECT Security_Vulnerability_Type, Defense_Mechanism_Used, COUNT(*) AS Usage_Count
        FROM dbo.global_cybersecurity_threats
        GROUP BY Security_Vulnerability_Type, Defense_Mechanism_Used
        ORDER BY Usage_Count DESC;
    """
}

# -------------------------------
# 3️⃣ Run Queries and Load into Pandas
# -------------------------------
dfs = {}
for name, query in queries.items():
    try:
        dfs[name] = pd.read_sql(query, conn)
        print(f"{name} loaded successfully")
    except Exception as e:
        print(f"Error loading {name}: {e}")

# -------------------------------
# 4️⃣ Visualization
# -------------------------------
sns.set_style("whitegrid")

# 4a. Incidents per Year
if "IncidentsPerYear" in dfs:
    plt.figure(figsize=(8,5))
    sns.lineplot(data=dfs["IncidentsPerYear"], x="Year", y="Total_Incidents", marker="o")
    plt.title("Cybersecurity Incidents Per Year")
    plt.ylabel("Total Incidents")
    plt.show()

# 4b. Average Resolution Time by Attack Type
if "ResolutionTime" in dfs:
    plt.figure(figsize=(10,6))
    sns.barplot(data=dfs["ResolutionTime"], x="Attack_Type", y="Avg_Resolution_Time", palette="Blues_d")
    plt.title("Average Incident Resolution Time by Attack Type (Hours)")
    plt.xticks(rotation=45)
    plt.ylabel("Avg Resolution Time")
    plt.show()

# 4c. Top 5 Industries by Financial Loss
if "TopIndustries" in dfs:
    plt.figure(figsize=(8,5))
    sns.barplot(data=dfs["TopIndustries"], x="Total_Financial_Loss", y="Target_Industry", palette="Reds_r")
    plt.title("Top 5 Industries by Financial Loss ($M)")
    plt.xlabel("Total Financial Loss ($M)")
    plt.show()

# 4d. Avg Affected Users vs Financial Loss by Attack Type
if "AvgAffectedVsLoss" in dfs:
    plt.figure(figsize=(8,6))
    sns.scatterplot(
        data=dfs["AvgAffectedVsLoss"],
        x="Avg_Affected_Users", y="Avg_Financial_Loss",
        hue="Attack_Type", s=100, palette="tab10"
    )
    plt.title("Average Affected Users vs Financial Loss by Attack Type")
    plt.xlabel("Avg Number of Affected Users")
    plt.ylabel("Avg Financial Loss ($M)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

# 4e. Vulnerability Type vs Defense Mechanism Usage Count (top 20 for visibility)
if "VulnerabilityDefense" in dfs:
    plt.figure(figsize=(12,6))
    sns.barplot(
        data=dfs["VulnerabilityDefense"].head(20),
        x="Usage_Count", y="Security_Vulnerability_Type",
        hue="Defense_Mechanism_Used"
    )
    plt.title("Top 20 Vulnerability Types and Defense Mechanisms Used")
    plt.xlabel("Usage Count")
    plt.ylabel("Vulnerability Type")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

# -------------------------------
# ✅ Complete
# -------------------------------
print("All queries executed and visualizations generated successfully!")
