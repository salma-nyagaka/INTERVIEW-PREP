# Exploratory Data Analysis (EDA) Common Interview Questions

## **1. What is Exploratory Data Analysis and why is it important?**

**Answer:**
is the data preparation stage focused on understanding your data quality and structure before building models. It's a systematic approach to inspect, visualize, and analyze data to inform modeling decisions.

**Importance:**
- **Data Quality Assessment**: Identify missing values, outliers, inconsistencies
- **Pattern Discovery**: Uncover hidden relationships and trends
- **Feature Understanding**: Learn about variable distributions and relationships
- **Modeling Preparation**: Inform feature selection and engineering decisions
- **Assumption Validation**: Check if data meets model requirements
- **Business Insights**: Generate hypotheses for further investigation

## **2. What are the main steps in EDA?**

**Answer:**
1. **Data Collection & Understanding**
   - Load data and understand structure
   - Check data types and dimensions
   - Review data dictionary/metadata

2. **Data Quality Assessment**
   - Identify missing values patterns
   - Detect outliers and anomalies
   - Check for duplicates
   - Validate data consistency

3. **Univariate Analysis**
   - Analyze individual variables
   - Calculate descriptive statistics
   - Create histograms, box plots

4. **Bivariate Analysis**
   - Examine relationships between pairs of variables
   - Correlation analysis
   - Scatter plots, cross-tabulations

5. **Multivariate Analysis**
   - Analyze interactions between multiple variables
   - Dimensionality reduction techniques
   - Advanced visualizations

6. **Insights & Documentation**
   - Summarize findings
   - Generate hypotheses
   - Prepare for modeling

## **3. How do you handle missing data in EDA?**

**Answer:**

**Detection Methods:**
- Use `isnull()`, `info()`, `describe()` functions
- Create missing value heatmaps
- Calculate missing percentage per column

**Analysis Patterns:**
- **Missing Completely at Random (MCAR)**: No pattern
- **Missing at Random (MAR)**: Depends on observed variables
- **Missing Not at Random (MNAR)**: Depends on unobserved factors

**Handling Strategies:**
- **Removal**: Drop rows/columns with high missing percentages
- **Imputation**: Mean/median/mode for numerical/categorical data
- **Advanced Imputation**: KNN, iterative imputation
- **Indicator Variables**: Create binary flags for missingness
- **Domain Knowledge**: Use business logic for imputation

## **4. What techniques do you use to identify outliers?**

**Answer:**

**Statistical Methods:**
- **Z-Score**: Values beyond ±3 standard deviations
- **IQR Method**: Values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR
- **Modified Z-Score**: Using median absolute deviation

**Visual Methods:**
- **Box plots**: Show quartiles and outliers
- **Scatter plots**: Identify unusual data points
- **Histograms**: Reveal distribution shape and extremes

**Advanced Techniques:**
- **Isolation Forest**: Machine learning approach
- **DBSCAN**: Density-based clustering
- **Local Outlier Factor (LOF)**: Local density comparison

**Domain-Specific Approaches:**
- Business rules and domain knowledge
- Time series analysis for temporal outliers
- Multivariate outlier detection

## **5. How do you analyze relationships between variables?**

**Answer:**

**Numerical vs Numerical:**
- **Correlation coefficient**: Pearson, Spearman, Kendall
- **Scatter plots**: Visual relationship assessment
- **Regression analysis**: Linear/non-linear relationships

**Categorical vs Categorical:**
- **Cross-tabulation**: Frequency tables
- **Chi-square test**: Independence testing
- **Cramér's V**: Association strength measure

**Numerical vs Categorical:**
- **Box plots**: Distribution comparison across groups
- **ANOVA**: Mean differences testing
- **Point-biserial correlation**: For binary categorical

**Advanced Techniques:**
- **Mutual information**: Non-linear relationships
- **Distance correlation**: General dependency measure
- **Copulas**: Dependency structure modeling

## **6. What visualization techniques do you use in EDA?**

**Answer:**

**Univariate Visualizations:**
- **Histograms**: Distribution shape and spread
- **Box plots**: Quartiles, outliers, skewness
- **Density plots**: Smooth distribution curves
- **Bar charts**: Categorical variable frequencies

**Bivariate Visualizations:**
- **Scatter plots**: Numerical relationships
- **Heatmaps**: Correlation matrices
- **Grouped bar charts**: Categorical comparisons
- **Violin plots**: Distribution + density information

**Multivariate Visualizations:**
- **Pair plots**: Multiple variable relationships
- **Parallel coordinates**: High-dimensional data
- **3D scatter plots**: Three-variable relationships
- **Faceted plots**: Subgroup analysis

**Time Series Visualizations:**
- **Line plots**: Trends over time
- **Seasonal decomposition**: Trend, seasonal, residual
- **Lag plots**: Autocorrelation assessment

## **7. How do you assess data quality during EDA?**

**Answer:**

**Completeness Checks:**
- Missing value percentages
- Data availability across time periods
- Required field validation

**Consistency Checks:**
- Value range validation
- Format standardization
- Cross-field validation rules

**Accuracy Assessment:**
- Outlier detection and investigation
- Business rule validation
- Historical comparison

**Uniqueness Verification:**
- Duplicate record identification
- Primary key validation
- Deduplication strategies

**Validity Testing:**
- Data type consistency
- Format compliance
- Referential integrity

## **8. What statistical measures do you focus on during EDA?**

**Answer:**

**Central Tendency:**
- **Mean**: Average value, sensitive to outliers
- **Median**: Middle value, robust to outliers
- **Mode**: Most frequent value

**Dispersion Measures:**
- **Standard deviation**: Average distance from mean
- **Variance**: Squared standard deviation
- **Range**: Difference between max and min
- **Interquartile range**: Middle 50% spread

**Distribution Shape:**
- **Skewness**: Asymmetry measure
- **Kurtosis**: Tail heaviness
- **Percentiles**: Value distribution

**Advanced Statistics:**
- **Coefficient of variation**: Relative variability
- **Entropy**: Information content
- **Gini coefficient**: Inequality measure

## **9. How do you determine if variables are normally distributed?**

**Answer:**

**Visual Methods:**
- **Q-Q plots**: Compare quantiles to normal distribution
- **Histograms**: Check for bell curve shape
- **Box plots**: Assess symmetry and outliers

**Statistical Tests:**
- **Shapiro-Wilk test**: Small sample sizes (n<50)
- **Kolmogorov-Smirnov test**: Larger samples
- **Anderson-Darling test**: More sensitive to tails
- **Jarque-Bera test**: Based on skewness and kurtosis

**Descriptive Statistics:**
- **Skewness close to 0**: Symmetric distribution
- **Kurtosis close to 3**: Normal tail behavior
- **Mean ≈ Median**: Central tendency alignment

**Transformation Approaches:**
- **Log transformation**: For right-skewed data
- **Square root**: Moderate skewness
- **Box-Cox transformation**: Optimal lambda parameter

## **10. How do you handle categorical variables in EDA?**

**Answer:**

**Basic Analysis:**
- **Frequency tables**: Count occurrences
- **Proportion calculations**: Relative frequencies
- **Mode identification**: Most common categories

**Visualization Techniques:**
- **Bar charts**: Category frequencies
- **Pie charts**: Proportion visualization
- **Donut charts**: Alternative to pie charts

**Advanced Analysis:**
- **Chi-square tests**: Independence testing
- **Cramér's V**: Association strength
- **Contingency tables**: Cross-tabulation analysis

**Encoding Considerations:**
- **Ordinal encoding**: For ordered categories
- **One-hot encoding**: For nominal categories
- **Target encoding**: Mean target by category
- **Frequency encoding**: Category occurrence counts

## **11. What are some common EDA mistakes to avoid?**

**Answer:**

**Data Understanding Mistakes:**
- Not understanding business context
- Ignoring data collection methodology
- Assuming data quality without verification

**Analysis Mistakes:**
- Over-relying on correlation without causation
- Ignoring outliers without investigation
- Using inappropriate statistical measures

**Visualization Mistakes:**
- Misleading chart types or scales
- Over-complicated visualizations
- Not considering audience needs

**Process Mistakes:**
- Rushing through EDA to modeling
- Not documenting findings and assumptions
- Failing to validate findings with domain experts

## **12. How do you perform EDA on time series data?**

**Answer:**

**Temporal Pattern Analysis:**
- **Trend analysis**: Long-term direction
- **Seasonality detection**: Recurring patterns
- **Cyclical patterns**: Irregular recurring cycles

**Statistical Analysis:**
- **Stationarity testing**: ADF, KPSS tests
- **Autocorrelation**: ACF plots
- **Partial autocorrelation**: PACF plots

**Decomposition Techniques:**
- **Additive decomposition**: Trend + Seasonal + Residual
- **Multiplicative decomposition**: Non-constant seasonal variation
- **STL decomposition**: Seasonal and Trend using Loess

**Anomaly Detection:**
- **Seasonal outliers**: Unusual seasonal behavior
- **Point anomalies**: Individual unusual observations
- **Contextual anomalies**: Time-dependent unusual behavior

## **13. How do you communicate EDA findings to stakeholders?**

**Answer:**

**Structure and Organization:**
- **Executive summary**: Key findings upfront
- **Methodology explanation**: Approach and tools used
- **Detailed findings**: Supporting evidence and analysis

**Visualization Best Practices:**
- **Clear, simple charts**: Easy to understand
- **Consistent color schemes**: Professional appearance
- **Appropriate chart types**: Match data and message

**Stakeholder-Specific Communication:**
- **Technical audience**: Detailed methodology and statistics
- **Business audience**: Insights and implications
- **Executive audience**: High-level findings and recommendations

**Actionable Insights:**
- **Business implications**: How findings affect operations
- **Recommendations**: Next steps and actions
- **Risk identification**: Potential data quality issues

## **Key Interview Tips:**

✅ **Understand the business context** behind data analysis
✅ **Explain your thought process** step by step
✅ **Discuss trade-offs** in different analytical approaches
✅ **Show practical experience** with real-world examples
✅ **Demonstrate tool proficiency** (Python, R, SQL, visualization tools)
✅ **Emphasize data quality** and validation importance
✅ **Connect EDA to downstream modeling** decisions

**Remember:** EDA is both an art and a science - combine statistical rigor with domain expertise and business intuition to extract meaningful insights from data.