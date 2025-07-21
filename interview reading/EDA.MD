# Exploratory Data Analysis (EDA) Common Interview Questions

## **1. What is Exploratory Data Analysis and why is it important?**

**Answer:**
is the data preparation stage focused on understanding your data quality and structure before building models. It's a systematic approach to inspect, visualize, and analyze data to inform modeling decisions.

**Importance:**
- **Data Quality Assessment**: Identify missing values, outliers, inconsistencies
- **Pattern Discovery**: Uncover hidden relationships and trends
- **Minimal missing values**: Identify and handle gaps in data
- **Outlier detection**: Find unusual or erroneous data points
- **Data integrity**: Verify data format and consistency
- **Error identification**: Catch problems early in the pipeline

- **Business Insights**: Generate hypotheses for further investigation



##  **Main Steps in EDA**

1. **Data Collection & Understanding**

   * Load data, check structure, types, dimensions
   * Review data dictionary or metadata

2. **Data Quality Assessment**

   * Handle missing values, outliers, duplicates
   * Ensure consistency and validity

3. **Univariate Analysis**

   * Analyze individual variables. Can help you understand the data distribution and identify any outliers.

   * Use stats (mean, median) and plots (histogram, box plot)

4. **Bivariate Analysis**

   * Study variable relationships (e.g. correlation, cross-tabs)and identify any patterns that might exist.
   * Use scatter plots, heatmaps

5. **Multivariate Analysis**

   * Explore interactions between variables  and identify any complex patterns or outliers that might exist.
   * Apply dimensionality reduction (e.g. PCA), advanced plots

6. **Insights & Documentation**

   * Summarize key findings
   * Generate hypotheses for modeling
   * Communicate clearly to stakeholders



## **3. Handling Missing Data in EDA**

1. **Identify** – Use `.isnull().sum()` to detect missing values
2. **Visualize** – Use heatmaps or missingno plots to see patterns
3. **Assess Impact** – Check percentage of missing data per column/row
4. **Handle Appropriately**:

   * **Drop** rows/columns (if missing is minimal or uninformative)
   * **Impute** using mean/median/mode, forward/backward fill, or model-based methods
   * **Flag** with indicators if missingness may carry meaning


## **4. What techniques do you use to identify outliers?**

1. **Box Plot / IQR Method** – Values outside Q1–1.5×IQR or Q3+1.5×IQR
2. **Z-Score** – Points with z-scores > 3 or < -3 (for normal data)
3. **Scatter Plots** – Visual detection in bivariate data
4. **Histogram / KDE Plot** – Unusual spikes or tails
5. **Isolation Forest / DBSCAN** – Model-based methods for complex datasets



## **5. How do you analyze relationships between variables?**
1. **Correlation Matrix** – For numeric variables (Pearson/Spearman)
2. **Scatter Plots** – Visualize linear/non-linear trends
3. **Cross-tabulation / Groupby** – For categorical vs categorical/numeric
4. **Box Plots / Violin Plots** – Compare distributions across groups
5. **Heatmaps** – Visualize correlations or interactions



### 📈 **6. Visualization Techniques in EDA**

1. **Histogram / KDE Plot** – For distribution
2. **Box Plot** – For outliers and spread
3. **Bar Chart** – For categorical comparisons
4. **Scatter Plot** – For relationships between variables
5. **Heat Map** – For correlation or matrix data
6. **Line Plot** – For trends over time (especially time 

## **7. How do you assess data quality during EDA?**
1. **Missing Values** – Identify and analyze with `.isnull().sum()` or heatmaps.
2. **Duplicates** – Use `df.duplicated().sum()` to find and handle redundancy.
3. **Inconsistent Formats** – Check types and category labels using `.info()`, `.unique()`.
4. **Outliers** – Detect using box plots, IQR, or z-scores.
5. **Invalid Values** – Look for negative or out-of-range entries.
6. **Distribution Checks** – Use histograms/KDE to spot skewness or spikes.
7. **Cross-Field Logic** – Validate related fields (e.g., `start_date < end_date`).

Tools: `pandas-profiling`, `sweetviz`, `great_expectations`.


## **8. What statistical measures do you focus on during EDA?**


1. **Mean, Median, Mode** – Central tendency
2. **Std Dev, IQR, Range** – Spread of data
3. **Skewness, Kurtosis** – Distribution shape
4. **Correlation (Pearson/Spearman)** – Variable relationships
5. **Value Counts** – Categorical frequency



## **9. How do you determine if variables are normally distributed?**
1. **Visual Methods**

   * **Histogram**, **Q-Q Plot**, **KDE Plot** – Look for bell shape or linearity.

2. **Statistical Tests**

   * **Shapiro-Wilk**, **Kolmogorov-Smirnov**, **Anderson-Darling** – Test normality.

3. **Skewness & Kurtosis**

   * Near **0** skewness and **3** kurtosis suggest normality.



### 🔠 **10. Handling Categorical Variables in EDA**

1. **Value Counts** – Use `.value_counts()` to check distribution.
2. **Bar Plots** – Visualize category frequencies.
3. **Groupby Stats** – Compare means/counts across categories.
4. **Encoding** – Label or one-hot encode for modeling.
5. **Missing/Anomalies** – Check for blanks or rare labels.



### ⚠️ **11. Common EDA Mistakes to Avoid**

1. **Ignoring missing values**
2. **Not checking data types**
3. **Skipping outlier analysis**
4. **Assuming normality**
5. **Overlooking time/context**
6. **Failing to validate assumptions**



### ⏱️ **12. EDA on Time Series Data**

1. **Datetime Parsing** – Ensure correct date format.
2. **Trend & Seasonality** – Use line plots and decomposition.
3. **Rolling Stats** – Apply moving averages or window functions.
4. **Time-based Aggregation** – Resample (e.g., daily → monthly).
5. **Stationarity Check** – Use ADF test or visualize shifts.


### 🗣️ **13. Communicating EDA Findings to Stakeholders**

1. **Summarize Key Insights** – Highlight trends, anomalies, and patterns clearly.
2. **Use Visuals** – Charts (bar, box, heatmaps) speak louder than raw stats.
3. **Avoid Jargon** – Use plain language tailored to the audience.
4. **Tell a Story** – Frame findings in a business-relevant context.
5. **Actionable Recommendations** – Link insights to decisions or next steps.

