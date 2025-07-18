# NLP Interview Preparation Summary

## What is NLP?
**Natural Language Processing (NLP)** is a branch of machine learning that enables computers to understand, interpret, and generate human language. It's used in applications like sentiment analysis, automated translation, chatbots, and search engines.

## Core NLP Pipeline

### 1. **Data Cleaning & Preprocessing**
- **Stop word removal**: Remove common words ("the", "and", "in") that add little meaning
- **Lowercasing**: Ensure text uniformity
- **Stemming**: Reduce words to root form ("running" → "run")
- **Lemmatization**: Convert to base form ("went" → "go")
- **POS Tagging**: Label parts of speech (noun, verb, etc.)
- **Named Entity Recognition (NER)**: Identify entities (Microsoft = organization)

### 2. **Tokenization**
Split text into smaller units (words, phrases, or subwords) that can be processed by models.

### 3. **Vectorization Methods**
Convert text tokens into numerical features:

- **Binary Vectorization**: 1 if word present, 0 if absent
- **Count Vectorization**: Number of times each word appears
- **TF-IDF**: Weights words by frequency and importance across documents
  - Emphasizes words frequent in one document but rare overall
  - Better for distinguishing document characteristics

### 4. **Model Development**
Train machine learning models (logistic regression, neural networks) on vectorized text.

## Task-Specific Preprocessing Strategies

| Task | Preprocessing Approach | Rationale |
|------|----------------------|-----------|
| **Sentiment Analysis** | Minimal preprocessing | Preserve nuanced word choices like "not great" |
| **Topic Classification** | Aggressive preprocessing | Focus on keywords, remove noise |
| **Named Entity Recognition** | Minimal preprocessing | Preserve original text structure and capitalization |
| **Text Generation** | No/minimal preprocessing | Maintain full linguistic context |

## Key Concepts for Interviews

### **N-grams**
- **Unigrams**: Single words
- **Bigrams**: Two-word combinations ("not great")
- **Trigrams**: Three-word combinations
- **Purpose**: Capture phrases that lose meaning when words are separated

### **TF-IDF Explained**
- **Term Frequency**: How often a word appears in a document
- **Inverse Document Frequency**: Penalizes words appearing in many documents
- **Result**: Highlights words that are distinctive to specific documents

### **Scikit-learn Pipeline**
```python
Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])
```
Benefits: Automates preprocessing, ensures consistent transformations, enables hyperparameter tuning

### **Document Frequency Parameters**
- **min_df**: Ignore words appearing in too few documents
- **max_df**: Ignore words appearing in too many documents
- **Purpose**: Balance between feature richness and noise reduction

## Real-World Applications

### **Pros of NLP**
- Automates large-scale text processing
- Enhances user experience (recommendations, search)
- Enables accessibility features
- Extracts insights from unstructured data

### **Cons of NLP**
- Struggles with ambiguity, sarcasm, context
- Can perpetuate biases from training data
- Requires large datasets and computational resources
- Challenges with multilingual and dialect variations

## Interview Tips

1. **Understand the trade-offs**: More preprocessing isn't always better - it depends on the task
2. **Know when to use what**: Minimal preprocessing for sentiment analysis, aggressive for topic classification
3. **Explain TF-IDF intuitively**: It finds words that are "important" to a specific document
4. **Demonstrate pipeline thinking**: Show you understand the full workflow from raw text to predictions
5. **Discuss evaluation**: Know metrics like AUC for classification tasks

This foundation covers the essential NLP concepts you'll need for most data science interviews, focusing on practical implementation rather than just theory.