# Exploratory Data Analysis (EDA) Interview Preparation Summary

## What is Exploratory Data Analysis (EDA)?

**EDA** is the data preparation stage focused on understanding your data quality and structure before building models. It's a systematic approach to inspect, visualize, and analyze data to inform modeling decisions.

## Two Main Goals of EDA

### **1. Ensure High-Quality Data**
- **Minimal missing values**: Identify and handle gaps in data
- **Outlier detection**: Find unusual or erroneous data points
- **Data integrity**: Verify data format and consistency
- **Error identification**: Catch problems early in the pipeline

### **2. Gain Insights**
- **Understand the problem better**: Learn from data patterns
- **Inform model decisions**: Guide feature selection and preprocessing
- **Build domain knowledge**: Develop intuition about the data
- **Validate assumptions**: Check if data matches expectations

## Three Key EDA Questions

### **1. How is the data distributed?**
- **Purpose**: Detect skewness, outliers, and unusual patterns
- **Methods**: Histograms, summary statistics, distribution plots
- **Insights**: Data transformation needs, normalization requirements

### **2. Which features are redundant?**
- **Purpose**: Identify correlated features to reduce dimensionality
- **Methods**: Correlation matrices, scatter plots, mutual information
- **Decision**: Keep, drop, or combine features

### **3. How do features correlate with the label?**
- **Purpose**: Identify predictive features
- **Methods**: Feature-label correlation analysis, bivariate plots
- **Insights**: Feature importance, relationship strength

## Data Quality Assessment with Pandas

### **Using .describe() Method**
```python
df.describe()  # Summary statistics for all numeric columns
```

### **Key Insights from .describe()**
- **Missing values**: Count lower than expected
- **Class imbalance**: Binary label mean near 0 or 1
- **Skewness**: Mean much higher than median
- **Outliers**: Extreme min/max values
- **Data errors**: Negative values where impossible

### **Automated Quality Checks**
- **Use .describe() output**: Programmatically flag issues
- **Count validation**: Ensure expected number of records
- **Range validation**: Check min/max values make sense
- **Data type validation**: Verify appropriate formats

## Visualization Techniques

### **Univariate Analysis**
- **Purpose**: Understand single feature distribution
- **Primary tool**: Histograms
- **Insights**: Range, central tendency, skew, variance, multi-modal distributions

### **Bivariate Analysis**
- **Purpose**: Explore relationships between two variables
- **Types**:
  - **Scatter plots**: Numeric vs. numeric relationships
  - **Bar plots**: Categorical vs. binary label
  - **Binned bar plots**: Numeric vs. binary label

### **Histogram Insights**
- **Multi-modal distributions**: Multiple peaks indicating subgroups
- **Skewed data**: Need for log transformation or other scaling
- **Outliers**: Extreme values requiring investigation
- **Normal distributions**: Ready for many ML algorithms

## Correlation and Dependency Analysis

### **Correlation (Linear Relationships)**
- **Pearson correlation**: Standardized covariance (-1 to 1)
- **Formula**: Corr(x,y) = Cov(x,y)/(σₓσᵧ)
- **Interpretation**: 
  - +1: Perfect positive correlation
  - 0: No linear relationship
  - -1: Perfect negative correlation
- **Limitation**: Only detects linear relationships

### **Mutual Information (All Relationships)**
- **Definition**: Measures uncertainty reduction about one variable given another
- **Formula**: I(x₁,x₂) = H(x₁) - H(x₁|x₂)
- **Range**: 0 to 1
- **Advantage**: Captures both linear and non-linear dependencies
- **Based on**: Information theory and entropy concepts

### **Covariance**
- **Formula**: Cov(x,y) = Σ(xᵢ - x̄)(yᵢ - ȳ)/(N-1)
- **Issue**: Unbounded values make interpretation difficult
- **Solution**: Use correlation instead (standardized covariance)

## Practical EDA Workflow

### **Initial Data Inspection**
1. **Visual inspection**: Use `head()`, `tail()`, `info()`
2. **File structure**: Check delimiters, headers, data types
3. **Dataset size**: Verify expected number of records
4. **Missing values**: Initial count of nulls

### **Statistical Analysis**
1. **Summary statistics**: Use `.describe()` for all numeric columns
2. **Categorical analysis**: Use `.value_counts()` for categories
3. **Missing value patterns**: Identify systematic gaps
4. **Outlier detection**: Flag extreme values

### **Visualization Pipeline**
1. **Univariate plots**: Histograms for each feature
2. **Bivariate plots**: Feature-label relationships
3. **Correlation heatmaps**: Feature-feature relationships
4. **Pair plots**: Multiple relationships at once

### **Feature Analysis**
1. **Correlation matrix**: Identify redundant features
2. **Mutual information**: Capture non-linear dependencies
3. **Feature-label correlation**: Rank predictive power
4. **Redundancy removal**: Drop highly correlated features

## Real-World Example Analysis

### **Income Prediction Dataset**
From the pairs plot analysis:

**Key Patterns**:
- **Age**: Right-skewed, higher earners in middle ages
- **Capital gains**: Highly skewed, strong predictor of high income
- **Work hours**: Peak at 40 hours, high earners work longer
- **Income distribution**: Dominated by <=50K earners

**Insights**:
- **Capital gains**: Strongest differentiator between income categories
- **Age and hours**: Weak positive correlation with income
- **Feature importance**: Capital gains > age > hours worked

## Tools and Libraries

### **Python Libraries**
- **Pandas**: Data manipulation and `.describe()`
- **Matplotlib**: Basic plotting functionality
- **Seaborn**: Statistical visualization and advanced plots
- **NumPy**: Numerical computations and statistics

### **Linux Commands** (for initial inspection)
- **`head`**: View first few lines
- **`tail`**: View last few lines
- **`wc`**: Count lines, words, characters
- **`cat`**: Display file contents

## Interview Key Points

### **What are the main goals of EDA?**
**Ensure data quality (minimal missing values/outliers) and gain insights to inform modeling decisions**

### **What are the three key EDA questions?**
**1) How is data distributed? 2) Which features are redundant? 3) How do features correlate with the label?**

### **What's the difference between correlation and mutual information?**
**Correlation measures linear relationships (-1 to 1), mutual information measures all dependencies (0 to 1) including non-linear**

### **How do you detect data quality issues?**
**Use `.describe()` to check for missing values (low count), outliers (extreme min/max), and skewness (mean >> median)**

### **What visualization techniques are most important?**
**Histograms for distribution, scatter plots for numeric relationships, bar plots for categorical relationships**

### **How do you handle missing values in EDA?**
**First identify patterns - are they random or systematic? Then decide: impute, drop, or create missingness indicators**

### **What makes a good feature for prediction?**
**High correlation/mutual information with the label, low correlation with other features (avoid redundancy)**

## Bottom Line for Interviews

**EDA is systematic data investigation with two goals: ensure quality and gain insights. Use `.describe()` for quick quality checks, histograms for distributions, and correlation/mutual information for relationships. The three key questions are: How is data distributed? Which features are redundant? How do features correlate with the label? Master these fundamentals and you'll catch data issues early and build better models through informed feature selection and preprocessing decisions.**