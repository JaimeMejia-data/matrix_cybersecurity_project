
-- Q1: Total incidents per year
SELECT Year, COUNT(*) AS Total_Incidents
FROM dbo.global_cybersecurity_threats
GROUP BY Year
ORDER BY Year;

-- Q2: Average resolution time by attack type
SELECT Attack_Type, AVG(Incident_Resolution_Time_in_Hours) AS Avg_Resolution_Time
FROM dbo.global_cybersecurity_threats
GROUP BY Attack_Type
ORDER BY Avg_Resolution_Time;

-- Q3: Top 5 industries with the highest total financial losses
SELECT TOP 5 Target_Industry, SUM(Financial_Loss_in_Million) AS Total_Financial_Loss
FROM dbo.global_cybersecurity_threats
GROUP BY Target_Industry
ORDER BY Total_Financial_Loss DESC;

-- Q4: Correlation between number of users affected and financial loss (grouped by attack type)
SELECT Attack_Type,
       AVG(Number_of_Affected_Users) AS Avg_Affected_Users,
       AVG(Financial_Loss_in_Million) AS Avg_Financial_Loss
FROM dbo.global_cybersecurity_threats
GROUP BY Attack_Type
ORDER BY Avg_Financial_Loss DESC;

-- Q5: Most common vulnerability type and how often each defense was used
SELECT Security_Vulnerability_Type, Defense_Mechanism_Used, COUNT(*) AS Usage_Count
FROM dbo.global_cybersecurity_threats
GROUP BY Security_Vulnerability_Type, Defense_Mechanism_Used
ORDER BY Usage_Count DESC;
