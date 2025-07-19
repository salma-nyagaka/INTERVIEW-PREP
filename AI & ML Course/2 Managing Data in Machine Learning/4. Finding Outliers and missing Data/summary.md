# Data Quality and Outlier Management Interview Preparation Summary

## Core Statistical Concepts

### **Measures of Centrality**
- **Mean**: Average of all values (sensitive to outliers)
- **Median**: Middle value when sorted (robust to outliers)
- **Mode**: Most frequent value (useful for categorical data)

### **Measures of Spread**
- **Variance**: How spread out data is from the mean
- **Standard Deviation (σ)**: Square root of variance, same units as data
- **IQR (Interquartile Range)**: Q3 - Q1, measures middle 50% spread
- **Percentiles/Quantiles**: Values below which a percentage of data falls

## Outlier Detection and Management

### **What Are Outliers?**
**Data points that deviate significantly from the rest of the dataset**
- **Univariate**: Visible in single feature
- **Multivariate**: Visible in combination with other features
- **Somewhat subjective**: Threshold depends on context

### **Why Outliers Matter**
- **Distort statistics**: Skew mean and standard deviation
- **Increase variance**: Make models less stable
- **Indicate errors**: May reveal data collection problems
- **Cause unreliable predictions**: Models perform poorly in sparse regions

### **Outlier Causes**
- **Human error**: Data entry mistakes
- **System error**: Integer overflow, sensor malfunction
- **Legitimate but rare**: Valid but unrepresentative values

## Outlier Detection Methods

### **1. Z-Score Method**
- **Formula**: Z = (value - mean) / standard_deviation
- **Threshold**: |Z| > 3 (99.7% of normal distribution within 3σ)
- **Assumption**: Data is normally distributed
- **Use case**: Good for normally distributed data

### **2. IQR Method**
- **Formula**: IQR = Q3 - Q1
- **Outlier boundaries**:
  - Lower bound = Q1 - K × IQR
  - Upper bound = Q3 + K × IQR
  - K typically = 1.5 or 2
- **More robust**: Works better with non-normal data
- **Visualization**: Box plots show IQR method clearly

### **Detection Visualization**
- **Histograms**: Show distribution shape and potential outliers
- **Scatter plots**: Reveal bivariate outliers
- **Box plots**: Visualize IQR method with whiskers and outlier points

## Handling Outliers

### **1. Remove Outliers**
- **When to use**: Rare occurrences or likely errors
- **Caution**: May lose important information
- **Document**: Always record removal decisions

### **2. Winsorization**
- **Definition**: Cap outliers at set threshold (e.g., 99.9th percentile)
- **Advantage**: Reduces skew without deletion
- **Preserves**: Data points while limiting extreme influence

### **3. Transformation**
- **Log transformation**: Reduce impact of extreme values
- **Square root**: Compress large values
- **Standardization**: Convert to z-scores

## Missing Data Management

### **Common Causes**
- **System failures**: Timeouts, crashes
- **Invalid values**: Out-of-range entries
- **Incomplete forms**: Partial survey responses

### **Identification**
- **Database**: `null` values
- **Pandas**: `NaN` values
- **Custom encoding**: Negative values where impossible
- **Detection**: Use `df.describe()` and `df.isna()`

### **Handling Strategies**

#### **1. Drop Rows/Columns**
- **When**: Few missing values or mostly missing column
- **Pro**: Simple, avoids unreliable records
- **Con**: Loses potentially valuable data

#### **2. Imputation**
- **Mean imputation**: Replace with average (for normal data)
- **Median imputation**: Replace with median (for skewed data)
- **Mode imputation**: Replace with most frequent (for categorical)
- **Constant imputation**: Replace with specific value

#### **3. Predictive Imputation**
- **Method**: Use other features to predict missing values
- **Advantage**: More sophisticated, feature-aware
- **Complexity**: Requires building sub-models

## Preparing Modeling Dataset

### **What is a Modeling Dataset?**
**Data that has gone through complete preparation process:**
- **Clean data**: No missing values, outliers handled
- **Proper sampling**: Representative of production environment
- **Labeled**: Ground truth for supervised learning
- **Structured**: Data matrix format (rows=examples, columns=features)
- **Engineered features**: Compatible with ML algorithms

### **Raw Data → Modeling Dataset Process**

#### **1. Data Understanding**
- **Problem definition**: Clear problem statement
- **EDA**: Statistical analysis and visualization
- **Quality assessment**: Identify issues early

#### **2. Data Preparation**
- **Sampling**: IID data from target environment
- **Label specification**: Define target variable
- **Matrix organization**: Structure rows/columns properly
- **Data cleaning**: Handle missing values and outliers

#### **3. Feature Engineering**
- **Transformation**: Format for ML algorithms
- **Optimization**: Enhance predictive power
- **Compatibility**: Ensure model requirements met

## Bias and Ethical Considerations

### **Addressing Bias**
- **Integrate social science concepts**: Recognize broader context
- **Embed equity**: At every pipeline stage
- **Human involvement**: Essential for ethical decisions
- **Continuous awareness**: Not a checklist, but a mindset

### **Best Practices**
- **Document decisions**: Record outlier and missing data handling
- **Consistent preprocessing**: Apply same steps to all datasets
- **Validation**: Test different approaches empirically
- **Stakeholder input**: Include domain experts in decisions

## Interview Key Points

### **What's the difference between mean and median for outlier detection?**
**Mean is sensitive to outliers and gets pulled toward extreme values; median is robust and represents the true center of the data**

### **When would you use Z-score vs IQR for outlier detection?**
**Z-score for normally distributed data, IQR for skewed or non-normal data since it's more robust**

### **How do you handle missing data?**
**Three approaches: drop (if few missing), impute (mean/median/mode), or predict (use other features). Choice depends on amount and pattern of missingness**

### **What is winsorization?**
**Capping outliers at a threshold (e.g., 99th percentile) instead of removing them - reduces extreme influence while preserving data points**

### **Why is consistent preprocessing important?**
**Same steps must be applied to training, validation, test, and production data to avoid introducing bias or inconsistencies**

### **What makes a dataset "modeling-ready"?**
**Clean data with handled missing values and outliers, proper sampling, clear labels, structured format, and engineered features compatible with ML algorithms**

## Bottom Line for Interviews

**Data quality is fundamental to ML success. Understand that outliers and missing data are common issues requiring systematic detection and handling. Use Z-score for normal data, IQR for skewed data. Handle missing values through dropping, imputation, or prediction based on the situation. Apply consistent preprocessing across all datasets. Remember that these decisions are subjective and should be validated empirically. The goal is a clean, structured, representative dataset that enables effective model training.**