# Data Preparation and Management Interview Preparation Summary

## Problem Definition - Unit of Analysis

### **What is Unit of Analysis?**
**Unit of analysis** defines what each row in your data matrix represents. It's the fundamental "thing" you're modeling and should be clearly stated in the initial problem definition.

### **Examples by Problem Type**
| Problem Type | Unit of Analysis |
|--------------|------------------|
| **Fraud Detection** | Transaction |
| **Marketing** | Reader-ad pair |
| **Recommendation** | User-tweet pair |
| **Telemetry** | Engine |
| **Credit Scoring** | Loan application |
| **Image Classification** | Image |

### **Key Considerations**
- **Single Entity**: One customer, one transaction, one image
- **Paired Entity**: User-item pairs, reader-ad combinations
- **ID Columns**: Track units for merging but exclude from training (prevent data leakage)
- **Consistent Definition**: All rows must represent the same unit type

## Data Understanding Process

### **Step 0: Define the Problem**
- **Who**: Define the unit of analysis (what each row represents)
- **What**: Specify attributes that refine your population
- **Why**: Understand the business objective

### **Exploratory Data Analysis (EDA)**
- **"Poking around"** the data for obvious insights
- **Descriptive summary** using statistical libraries
- **Visualization**: Scatter plots, histograms, distributions
- **Data quality assessment**: Missing values, outliers, anomalies

### **Visualization Techniques**
- **Distribution analysis**: Understand data skew and shape
- **Outlier detection**: Identify unusual data points
- **Relationship exploration**: Feature correlations and patterns
- **Essential integration**: Part of data preparation workflow

## Sampling Techniques

### **Why Sampling Matters**
- **Generalization**: Sample should reflect larger data distribution
- **Efficiency**: Manage dataset size for training
- **Representation**: Ensure model works on target population

### **Key Sampling Concepts**

#### **Population Definition**
1. **Unit of Analysis**: What individual "thing" you're modeling
2. **Sample Population**: Specific attributes that refine your population
3. **Subgroup Modeling**: Different models for different segments

#### **IID Sampling**
- **Independent and Identically Distributed**: Achieved through random sampling
- **Ensures reliable training**: Prevents bias from systematic patterns
- **Random selection**: Each data point has equal probability of selection

#### **Sample Size vs. Performance**
- **More data generally improves performance** (with diminishing returns)
- **Quality over quantity**: Focus on balanced, representative samples
- **Computational constraints**: Balance accuracy with training efficiency

## Data Preparation Workflow
### Data Understanding
**Define Problem**: Establish target variable, unit of analysis, and success metrics before any data work.

**EDA**: Generate descriptive statistics and basic plots (histograms, scatter plots) to identify patterns and data quality issues.

**Visualization**: Apply distribution analysis, outlier detection, and correlation plots to inform preprocessing decisions.

### Data Preparation
**Sampling**: Validate data represents production environment; ensure I.I.D assumptions are met.

**Label Specification**: Define ground truth variable; determine classification vs regression task; handle label transformation if needed.

**Data Matrix Construction**: Structure as N×M matrix where N=samples, M-1=features, final column=target variable.

**Data Cleaning**: Handle missing values (imputation/deletion), remove/treat outliers (winsorization), eliminate corrupted records.

### Modeling
**Feature Engineering**: Transform raw data into model-compatible formats; address categorical encoding, scaling, and feature creation requirements.

Each step must be completed sequentially with validation checks before proceeding to model training.
## Fairness and Representation

### **Bias Prevention**
- **Underrepresented groups**: May lead to biased models
- **Subgroup evaluation**: Check performance across demographics
- **Balanced sampling**: Ensure proportional representation
- **Fairness metrics**: Evaluate model equity across groups

### **Addressing Imbalance**
- **Upsampling**: Add more examples from underrepresented groups
- **Downsampling**: Reduce overrepresented groups
- **Stratified sampling**: Maintain proportions across important categories
- **Balanced datasets**: Equal representation when appropriate

## Data Filtering and Analysis

### **Pandas Filtering Techniques**
```python
# Single condition
condition = df['column'] == 'value'
filtered_df = df[condition]

# Multiple conditions
condition1 = df['col1'] == 'value1'
condition2 = df['col2'] > threshold
combined = condition1 & condition2
result = df[combined]

# Missing value handling
df_clean = df[df['column'].notnull()]
```

### **DataFrame Operations**
- **`.loc[]`**: Label-based indexing (`df.loc[row_labels, column_labels]`)
- **`.iloc[]`**: Integer position-based indexing (`df.iloc[row_indices, column_indices]`)
- **`.shape`**: Get dimensions (rows, columns)
- **`.head()`**: Display first few rows
- **`.unique()`**: Get unique values in column
- **`.value_counts()`**: Count occurrences of each value

## Feature Engineering
- concerns bringing data into the right format and representations required by the intended machine learning model.

### **Common Transformations**
- **Categorical encoding**: Convert text to numerical values
- **Scaling/normalization**: Adjust feature ranges
- **Feature creation**: Derive new features from existing ones
- **Dimensionality reduction**: Reduce feature space complexity

## Label Specification

### **Supervised Learning Requirements**
- **Ground truth**: Each data point needs associated label
- **Label casting**: Convert between data types (e.g., 1-5 stars → Good/Bad)
- **Problem type determination**: Classification vs. regression
- **Consistent labeling**: Uniform label format across dataset

### **Label Types**
- **Binary**: Two classes (spam/not spam, fraud/legitimate)
- **Multiclass**: Multiple categories (animal types, ratings)
- **Regression**: Continuous values (prices, temperatures)

## Interview Key Points

### **What is unit of analysis and why is it important?**
**Unit of analysis defines what each row represents in your data. It's crucial because it determines how you collect, structure, and interpret your data for modeling.**

### **How do you ensure your sample is representative?**
**Use random sampling to achieve IID distribution, check for balanced representation across important subgroups, and ensure sample population matches prediction population.**

### **What's the difference between .loc and .iloc?**
**`.loc` uses labels for indexing, `.iloc` uses integer positions. Use `.loc` for named rows/columns, `.iloc` for position-based slicing.**

### **How do you handle missing values in data?**
**Use `.notnull()` to filter out missing values, or apply imputation techniques depending on the context and business requirements.**

### **What's the purpose of exploratory data analysis?**
**EDA helps understand data distribution, identify outliers, discover patterns, and inform data cleaning and feature engineering decisions.**

### **How do you address bias in sampling?**
**Check subgroup representation, use stratified sampling when needed, and consider upsampling underrepresented groups to ensure fairness.**

## Bottom Line for Interviews

**Data preparation is the foundation of successful ML projects. Start by clearly defining your unit of analysis, ensure representative sampling through random selection, and use EDA to understand your data quality and distribution. Balance efficiency with fairness by checking subgroup representation and addressing bias through appropriate sampling techniques. Master pandas operations (.loc, .iloc, filtering) for practical data manipulation, and remember that clean, well-prepared data is more valuable than complex algorithms applied to poor data.**