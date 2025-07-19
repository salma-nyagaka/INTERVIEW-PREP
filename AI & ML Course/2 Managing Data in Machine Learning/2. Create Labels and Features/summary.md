# Feature Engineering and Data Types Interview Preparation Summary

## Data Types in Machine Learning

### **Why Data Types Matter**
**Data types determine how features are processed, transformed, and used in models.** While all ML models operate on numbers, understanding data types guides preprocessing decisions and affects model performance.

### **Four Core Data Types**

#### **1. Continuous (Float)**
- **Definition**: Real numbers with meaningful differences between values
- **Examples**: Temperature, price, weight, probability scores
- **Usage**: Ready for modeling as features or regression labels
- **Considerations**: May contain outliers and skewed distributions
- **Preprocessing**: Scaling, normalization, outlier handling

#### **2. Integer**
- **Definition**: Whole numbers, often representing counts
- **Examples**: Number of clicks, age in years, quantity purchased
- **Usage**: Similar to continuous data, regression labels
- **Note**: Model output might be non-integer even with integer labels
- **Preprocessing**: Similar to continuous data

#### **3. Ordinal**
- **Definition**: Categorical with inherent order but no meaningful differences
- **Examples**: Ratings (1-5 stars), education levels, satisfaction scores
- **Usage**: Features or labels (regression/classification)
- **Key Issue**: Avoid treating as simple integers (1,2,3,4,5)
- **Preprocessing**: Binary encoding, ordinal encoding, sometimes one-hot

#### **4. Nominal (Categorical)**
- **Definition**: Categories with no inherent order
- **Examples**: Colors, brands, countries, job titles
- **Usage**: Features or classification labels
- **Storage**: Often as strings or encoded integers
- **Preprocessing**: **Must be transformed** (one-hot encoding essential)

## Feature Engineering Process
After defining the modeling population and label, the next step is **feature engineering**, which involves two main strategies:

1. **Mapping predictive or causal concepts to data representations** – this is the first and most impactful strategy, often guided by intuition and a conceptual model of the problem. It involves aggregating and converting raw data into meaningful features.
2. **Manipulating data for machine learning APIs** – the second strategy focuses on preparing these features in ways models can use (e.g., normalization, encoding). Of these transformations, **one-hot encoding** is essential for categorical data and cannot be skipped.

### **Feature Transformation Techniques**

| Technique | Input | Output | Purpose |
|-----------|--------|--------|---------|
| **Binary Indicator** | Categorical/Numeric | Binary (0/1) | Flag presence/absence |
| **One-Hot Encoding** | Categorical | Binary (0/1) | Handle categories |
| **Functional Transform** | Numeric | Numeric | Log, square, etc. |
| **Interaction Terms** | Numeric | Numeric | Feature combinations |
| **Binning** | Numeric | Categorical | Discretize continuous |
| **Scaling** | Numeric | Numeric | Normalize ranges |

## Domain-Driven Feature Engineering

### **When Feature Engineering Matters Less**
- **Image recognition**: Deep neural networks learn features automatically
- **Language translation**: End-to-end deep learning
- **Special property**: Auto-learn feature concepts from raw data
- **Outside these applications**: Feature engineering still critically important

### **Principles of Effective Feature Engineering**

#### **1. Think Like a Scientist**
- **Study cause and effect** relationships
- **Identify causal factors** based on domain knowledge
- **Test empirically** with data
- **Prefer causal features** but correlated factors also valid

#### **2. Seek Input from Other Experts**
- **You're not the only expert** - engage domain specialists
- **Non-technical experts** often have valuable insights
- **Customer-facing staff** understand user behavior
- **Years of experience** provide intuition
- **Avoid ineligible features** due to legal/system constraints

#### **3. Be Practical and Strategic**
- **Unlimited feature possibilities** but limited time/resources
- **Each feature takes similar time** to implement
- **Predictiveness varies greatly** across features
- **Can't know value in advance**

### **Feature Planning Process**
1. **Create feature planning list**
2. **Get input on expected value** from experts
3. **Build and evaluate iteratively**
4. **Stop at diminishing returns**

## Label Definition

### **Importance of Label Design**
- **Critical and underestimated step** in supervised ML
- **Closely tied to problem statement**
- **Influences nearly every part** of model development
- **Changing label changes the problem**

### **Clear Label Scenarios (Easy)**
- **Well-defined outcomes**: Yes/no, categorical options
- **Directly observable**: Ad clicks, digit recognition
- **Clean mapping**: Each input maps to one label

### **Challenging Label Scenarios**
- **Subjective goals**: User satisfaction, content quality
- **Unobservable labels**: Abstract concepts
- **Multiple valid interpretations**: Ambiguous outcomes
- **Long-term goals**: Delayed feedback (90-day retention)

### **Proxy Solutions**
- **Use proxies for difficult labels**: Short-term engagement for long-term retention
- **Introduce limitations**: Proxy may not perfectly represent true goal
- **Trade-off**: Measurable vs. ideal

### **Simplification Strategies**
- **Convert complex to simple**: Ordinal ratings (1-5) → binary (high/low)
- **Time-based simplification**: "Will event happen by time X?" vs. "When will event happen?"
- **Easier training and deployment**

## Real-World Example: Twitter "Who to Follow"

### **Problem**: Did user follow the recommended person?

### **Scientist Approach**
**Ask**: Why do I follow someone on Twitter?

**Avoid abstract reasons**:
- "Do I find the person interesting?"

**Seek concrete, codable concepts**:
- **Topic match**: Person tweets about topics I follow
- **Reciprocity**: Person follows me
- **Mutual connections**: People I follow also follow them
- **Popularity**: Person is widely followed

### **All convertible to measurable features**

## Performance and Diminishing Returns

### **Feature Development Reality**
- **Fixed cost per feature**
- **Not all add value**
- **Some redundant**
- **Performance curve shows diminishing returns**

### **Strategic Approach**
- **Effort 1**: Build 50 strong features
- **Effort 2**: Build 50 weaker/redundant features
- **Effort 1 gives more performance per unit time**

### **Decision Framework**
- **Use collective judgment** to prioritize
- **Test and evaluate** iteratively
- **Stop when gains don't justify effort**

## Interview Key Points

### **What are the main data types in ML and why do they matter?**
**Continuous, Integer, Ordinal, and Nominal. They determine preprocessing approach - ordinal needs careful encoding to preserve order, nominal requires one-hot encoding.**

### **What's the difference between ordinal and nominal data?**
**Ordinal has inherent order (ratings 1-5), nominal doesn't (colors, brands). Ordinal preserves ranking, nominal treats all categories as equally different.**

### **What are the two main feature engineering strategies?**
**1) Mapping concepts to data representations (most impactful), 2) Manipulating data for ML APIs (technical necessity like one-hot encoding).**

### **How do you approach feature engineering systematically?**
**Think like a scientist (identify causal factors), seek expert input (domain knowledge), be strategic (prioritize based on expected value and diminishing returns).**

### **What makes label definition challenging?**
**Subjective goals, unobservable outcomes, multiple interpretations, and long-term feedback. Often need proxies that introduce their own limitations.**

### **When is feature engineering less important?**
**Image recognition and language translation with deep neural networks that can automatically learn features from raw data.**

### **Why is one-hot encoding essential?**
**ML models need numerical input, and one-hot encoding converts categorical data into binary vectors that models can process without assuming false ordinal relationships.**

## Bottom Line for Interviews

**Feature engineering is where domain knowledge meets technical implementation. Understand your data types to choose proper preprocessing - ordinal preserves order, nominal needs one-hot encoding. Focus on mapping meaningful concepts to data representations rather than just technical transformations. Label definition is strategic and iterative - it changes the entire problem. Seek domain expert input, think causally, and manage diminishing returns through strategic prioritization. In most applications outside deep learning for images/text, thoughtful feature engineering is the key to model success.**