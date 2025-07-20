# Machine Learning Algorithms

## Supervised Learning

### **Classification Algorithms**

**Logistic Regression**
- **Purpose:** Binary and multi-class classification
- **How it works:** Uses probability and logistic function
- **Use cases:** Email spam detection, medical diagnosis, marketing response
- **Pros:** Simple, interpretable, fast
- **Cons:** Assumes linear relationship

**Decision Trees**
- **Purpose:** Classification and regression
- **How it works:** Creates tree-like model of decisions
- **Use cases:** Credit approval, medical diagnosis, feature selection
- **Pros:** Easy to understand, handles mixed data types
- **Cons:** Prone to overfitting, unstable

**Random Forest**
- **Purpose:** Classification and regression
- **How it works:** Combines multiple decision trees
- **Use cases:** Feature importance, complex datasets, general-purpose
- **Pros:** Reduces overfitting, handles missing values
- **Cons:** Less interpretable, can overfit with noisy data

**Support Vector Machine (SVM)**
- **Purpose:** Classification and regression
- **How it works:** Finds optimal boundary between classes
- **Use cases:** Text classification, image recognition, bioinformatics
- **Pros:** Works well with high dimensions, memory efficient
- **Cons:** Slow on large datasets, sensitive to scaling

**K-Nearest Neighbors (KNN)**
- **Purpose:** Classification and regression
- **How it works:** Classifies based on nearest neighbors
- **Use cases:** Recommendation systems, pattern recognition, anomaly detection
- **Pros:** Simple, no training period, works with small datasets
- **Cons:** Computationally expensive, sensitive to irrelevant features

**Naive Bayes**
- **Purpose:** Classification
- **How it works:** Based on Bayes' theorem with independence assumption
- **Use cases:** Text classification, spam filtering, sentiment analysis
- **Pros:** Fast, works well with small datasets, handles multiple classes
- **Cons:** Strong independence assumption, can be outperformed by other methods

### **Regression Algorithms**

**Linear Regression**
- **Purpose:** Predicting continuous values
- **How it works:** Finds best line through data points
- **Use cases:** Sales forecasting, price prediction, risk assessment
- **Pros:** Simple, interpretable, fast
- **Cons:** Assumes linear relationship, sensitive to outliers

**Polynomial Regression**
- **Purpose:** Non-linear relationships
- **How it works:** Uses polynomial features
- **Use cases:** Curve fitting, growth modeling
- **Pros:** Captures non-linear patterns
- **Cons:** Can overfit easily, computationally complex

**Ridge Regression**
- **Purpose:** Regression with regularization
- **How it works:** Adds penalty term to reduce overfitting
- **Use cases:** High-dimensional data, multicollinearity
- **Pros:** Prevents overfitting, handles multicollinearity
- **Cons:** Less interpretable, requires parameter tuning

**Lasso Regression**
- **Purpose:** Regression with feature selection
- **How it works:** L1 regularization that can zero out features
- **Use cases:** Feature selection, sparse models
- **Pros:** Automatic feature selection, prevents overfitting
- **Cons:** Can be unstable, may remove useful features

## Unsupervised Learning

### **Clustering Algorithms**

**K-Means**
- **Purpose:** Grouping similar data points
- **How it works:** Divides data into k clusters around centroids
- **Use cases:** Customer segmentation, market research, image segmentation
- **Pros:** Simple, fast, works well with spherical clusters
- **Cons:** Need to specify k, sensitive to initialization

**Hierarchical Clustering**
- **Purpose:** Creating tree of clusters
- **How it works:** Bottom-up or top-down cluster merging/splitting
- **Use cases:** Phylogenetic analysis, social network analysis
- **Pros:** Don't need to specify number of clusters, creates hierarchy
- **Cons:** Computationally expensive, difficult to handle large datasets

**DBSCAN**
- **Purpose:** Density-based clustering
- **How it works:** Groups dense regions, identifies outliers
- **Use cases:** Anomaly detection, image processing, geolocation clustering
- **Pros:** Finds arbitrary shapes, identifies outliers, no need to specify clusters
- **Cons:** Sensitive to parameters, struggles with varying densities

### **Dimensionality Reduction**

**Principal Component Analysis (PCA)**
- **Purpose:** Reduce dimensions while preserving variance
- **How it works:** Finds principal components that explain most variance
- **Use cases:** Data visualization, feature reduction, compression
- **Pros:** Reduces overfitting, removes correlation, fast
- **Cons:** Components not interpretable, linear transformation only

**t-SNE**
- **Purpose:** Non-linear dimensionality reduction for visualization
- **How it works:** Preserves local structure in lower dimensions
- **Use cases:** Data visualization, exploratory analysis
- **Pros:** Great for visualization, preserves local structure
- **Cons:** Computationally expensive, mainly for visualization

**Linear Discriminant Analysis (LDA)**
- **Purpose:** Dimensionality reduction for classification
- **How it works:** Finds dimensions that separate classes best
- **Use cases:** Face recognition, marketing analysis
- **Pros:** Supervised reduction, good for classification
- **Cons:** Assumes normal distribution, limited to C-1 dimensions

## Deep Learning

### **Neural Networks**

**Artificial Neural Network (ANN)**
- **Purpose:** General-purpose learning
- **How it works:** Layers of interconnected neurons
- **Use cases:** Pattern recognition, function approximation
- **Pros:** Universal approximators, flexible
- **Cons:** Black box, requires large data, prone to overfitting

**Convolutional Neural Network (CNN)**
- **Purpose:** Image and spatial data processing
- **How it works:** Uses convolution layers to detect features
- **Use cases:** Image recognition, medical imaging, autonomous vehicles
- **Pros:** Translation invariant, hierarchical features, efficient for images
- **Cons:** Requires large datasets, computationally intensive

**Recurrent Neural Network (RNN)**
- **Purpose:** Sequential data processing
- **How it works:** Has memory to process sequences
- **Use cases:** Natural language processing, time series, speech recognition
- **Pros:** Handles sequential data, variable input length
- **Cons:** Vanishing gradient problem, slow training

**Long Short-Term Memory (LSTM)**
- **Purpose:** Long sequence processing
- **How it works:** Special RNN with gates to control information flow
- **Use cases:** Language translation, stock prediction, sentiment analysis
- **Pros:** Solves vanishing gradient, remembers long-term dependencies
- **Cons:** Complex architecture, computationally expensive

## Ensemble Methods

**Bagging**
- **Purpose:** Reduce overfitting through averaging
- **How it works:** Trains multiple models on different subsets
- **Examples:** Random Forest, Extra Trees
- **Pros:** Reduces variance, parallel training
- **Cons:** May not improve bias

**Boosting**
- **Purpose:** Convert weak learners to strong learner
- **How it works:** Sequential training, focusing on errors
- **Examples:** AdaBoost, Gradient Boosting, XGBoost
- **Pros:** Often achieves high accuracy, reduces bias
- **Cons:** Prone to overfitting, sequential training

**Stacking**
- **Purpose:** Combine different types of models
- **How it works:** Meta-learner combines base model predictions
- **Use cases:** Competitions, complex problems
- **Pros:** Can capture different patterns, often best performance
- **Cons:** Complex, risk of overfitting

## Reinforcement Learning

**Q-Learning**
- **Purpose:** Learn optimal actions in environment
- **How it works:** Learns action-value function
- **Use cases:** Game playing, robotics, autonomous systems
- **Pros:** Model-free, learns optimal policy
- **Cons:** Requires exploration, may be slow to converge

**Deep Q-Network (DQN)**
- **Purpose:** Q-learning with neural networks
- **How it works:** Neural network approximates Q-function
- **Use cases:** Complex games, robotics
- **Pros:** Handles high-dimensional states, powerful
- **Cons:** Unstable training, requires careful tuning

## Algorithm Selection Guide

### **Classification Problems:**
- **Small dataset:** Naive Bayes, KNN
- **Linear problem:** Logistic Regression
- **Non-linear problem:** Random Forest, SVM
- **Need interpretability:** Decision Trees, Logistic Regression
- **High accuracy needed:** Random Forest, XGBoost

### **Regression Problems:**
- **Linear relationship:** Linear Regression
- **Non-linear relationship:** Random Forest, Neural Networks
- **High dimensions:** Ridge/Lasso Regression
- **Need interpretability:** Linear Regression, Decision Trees

### **Clustering:**
- **Known cluster count:** K-Means
- **Unknown cluster count:** Hierarchical Clustering
- **Outlier detection:** DBSCAN
- **Large dataset:** K-Means, Mini-batch K-Means

### **Time Series:**
- **Short sequences:** Traditional statistical methods
- **Long sequences:** LSTM, GRU
- **Multiple variables:** Vector Autoregression, Neural Networks

## Evaluation Metrics

### **Classification:**
- **Accuracy:** Overall correctness
- **Precision:** True positives / (True positives + False positives)
- **Recall:** True positives / (True positives + False negatives)
- **F1-Score:** Harmonic mean of precision and recall
- **ROC-AUC:** Area under receiver operating characteristic curve

### **Regression:**
- **Mean Absolute Error (MAE):** Average absolute differences
- **Mean Squared Error (MSE):** Average squared differences
- **Root Mean Squared Error (RMSE):** Square root of MSE
- **R-squared:** Proportion of variance explained

### **Clustering:**
- **Silhouette Score:** Measure of cluster separation
- **Inertia:** Within-cluster sum of squares
- **Adjusted Rand Index:** Similarity to true clustering

**Key Point:** Algorithm choice depends on problem type, data size, interpretability needs, and performance requirements. Start simple, then increase complexity as needed.