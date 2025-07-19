# Machine Learning Taxonomy Interview Preparation Summary

## Machine Learning Overview

**Machine Learning** encompasses various algorithms that serve as building blocks for sophisticated applications. These methods fall into two main families: **supervised** and **unsupervised learning**.

## Core Terminology

### **Data Structure**
- **Dataset**: Collection of data used in machine learning
- **Data Matrix**: Structured table with rows and columns
- **Features (X)**: Input variables/attributes in columns that describe the data
- **Labels (y)**: Target variable we want to predict
- **Example/Data Point**: Single instance of data (one row in data matrix)

### **Example Types**
- **Labeled Example**: Contains both features and a label
- **Unlabeled Example**: Contains only features, no label

## Supervised Learning

### **Definition**
**Supervised learning** attempts to discover relationships between features and labels for future prediction. It uses labeled examples to train models that can make predictions on new, unseen data.

### **Key Characteristics**
- **Training Data**: Uses labeled examples as input
- **Goal**: Learn to predict labels based on features
- **Supervision**: Label provides feedback on model correctness
- **Two Phases**: Training phase (build model) and prediction/inference phase (make predictions)

### **Training Process**
1. **Learning**: Model gradually learns feature-label relationships from training data
2. **Iteration**: Model is iteratively improved using labels to check correctness
3. **Optimization**: Features are weighted based on their predictive power
4. **Result**: Optimal model capable of making future predictions

### **Types of Supervised Learning**

#### **Classification**
- **Definition**: Predicts discrete/categorical values (classes)
- **Output**: Categories or class probability membership
- **Subtypes**:
  - **Binary Classification**: Two possible outcomes (spam/not spam, fraud/not fraud)
  - **Multiclass Classification**: Multiple categories (animal types, weather conditions)

#### **Regression**
- **Definition**: Predicts continuous/numerical values
- **Output**: Real-valued numbers (prices, temperatures, heights)
- **Key Difference**: "Closeness" to correct answer matters

### **Classification vs. Regression Decision**
- **Regression**: When being "close" to correct answer matters (predicting height: 182cm vs 183cm is close)
- **Classification**: When errors are binary - right or wrong, no similarity between classes (facial recognition: Bill Gates vs Steve Jobs)

## Unsupervised Learning

### **Definition**
**Unsupervised learning** discovers patterns in data without using labeled examples. It finds hidden structures and relationships in data.

### **Key Characteristics**
- **No Labels**: Works with unlabeled data only
- **Pattern Discovery**: Identifies hidden structures
- **Subjective Interpretation**: Requires human insight to derive business value
- **No Accuracy Metrics**: Can't measure "correctness" like supervised learning

### **Main Technique: Clustering**
- **Definition**: Groups data into clusters based on similarity
- **Goal**: Members within clusters are similar; different from other clusters
- **Applications**: Customer segmentation, market research, recommendation systems

## Real-World Examples

### **Supervised Learning: Credit Scoring**
- **Business Problem**: Credit lending company wants to reduce default risk
- **ML Translation**: Build default prediction model (binary classification)
- **Features**: Age, income, credit history
- **Label**: Default (yes/no) - missing 3+ consecutive payments in 6 months
- **Advantage**: Mathematical optimization beats human heuristics

### **Unsupervised Learning: Customer Segmentation**
- **Business Problem**: Create tailored products for different customer types
- **ML Translation**: Identify clusters of similar customers
- **Features**: Age, income, spending patterns
- **No Label**: No specific outcome to predict
- **Output**: Customer segments for targeted product development

## Key Differences: Supervised vs. Unsupervised

| Aspect | Supervised Learning | Unsupervised Learning |
|--------|--------------------|-----------------------|
| **Data** | Labeled examples | Unlabeled data |
| **Goal** | Predict labels | Discover patterns |
| **Evaluation** | Accuracy metrics | Subjective interpretation |
| **Output** | Predictions | Clusters/segments |
| **Business Value** | Direct predictions | Insights for strategy |

## Generalization

### **Definition**
**Generalization** is a model's ability to adapt to new, previously unseen data that is similar to training data.

### **Importance**
- **Critical Success Factor**: Determines real-world model effectiveness
- **Beyond Memorization**: Model must learn patterns, not just memorize training data
- **Business Value**: Enables predictions on future, unseen cases

## Practical Considerations

### **Cold Start Problem**
- **Challenge**: New companies lack historical data
- **Solution**: Experimental approach (initially broad data collection)
- **Example**: Credit company initially approving all applicants to gather data

### **Traditional vs. ML Approaches**
- **Traditional Heuristics**: Simple rules based on domain expertise
- **ML Advantage**: Mathematical optimization, scalability, precision
- **Fairness**: Treats similar risk profiles equally

### **Business Applications**
- **Scalability**: Works with hundreds of features
- **Precision**: Mathematical optimization beats human intuition
- **Nuanced Decisions**: Can use confidence scores for risk-based decisions
- **Fairness**: Consistent treatment of similar cases

## Interview Key Points

### **What's the difference between supervised and unsupervised learning?**
**Supervised learning uses labeled data to make predictions; unsupervised learning finds patterns in unlabeled data**

### **What's the difference between classification and regression?**
**Classification predicts categories (discrete); regression predicts numerical values (continuous)**

### **What is generalization and why is it important?**
**The ability to make accurate predictions on new, unseen data - it's what makes models useful in the real world**

### **When would you use unsupervised learning?**
**When you want to discover hidden patterns or segments in data without knowing what you're looking for**

### **How do you choose between classification and regression?**
**Based on the output: if 'closeness' to the answer matters, use regression; if categories are distinct, use classification**

### **What are the key components of supervised learning?**
**Features (input variables), labels (target variable), training data (labeled examples), and a model that learns relationships**

## Bottom Line for Interviews

**Machine Learning has two main families: supervised learning (uses labeled data to make predictions) and unsupervised learning (discovers patterns in unlabeled data). Supervised learning includes classification (predicting categories) and regression (predicting numbers). The key to success is generalization - the model's ability to perform well on new, unseen data. Choose the approach based on whether you have labels and what type of output you need.**