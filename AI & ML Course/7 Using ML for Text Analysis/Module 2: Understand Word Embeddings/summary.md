# Word Embeddings Interview Preparation Summary

## What are Word Embeddings?

**Word embeddings** are dense numerical vector representations of words that capture semantic meaning and relationships. Unlike simple vectorization methods like TF-IDF that convert words to numbers based on frequency, word embeddings learn the **actual meaning** of words by analyzing large text corpora.

## Key Concepts

### **Vector Representation**
- Each word is represented as a **K-dimensional vector** (typically 50, 100, or 300 dimensions)
- **Dense vectors**: mostly non-zero values (vs. sparse TF-IDF vectors)
- **Semantic similarity**: words with similar meanings have similar vectors
- Example: "doctor" and "patient" have similar vectors; "doctor" and "tree" have dissimilar vectors

### **Cosine Similarity**
```
Cosine Similarity = (V₁ · V₂) / (||V₁|| ||V₂||)
```
- Measures angle between two vectors
- **Same direction**: similarity = 1 (0° angle)
- **Opposite direction**: similarity = -1 (180° angle)
- **Orthogonal**: similarity = 0 (90° angle)

### **Semantic Relationships**
Word embeddings capture amazing semantic properties:
```
King - Man + Woman ≈ Queen
Paris - France + Italy ≈ Rome
```

## Popular Word Embedding Models

| Model | Description | Key Features |
|-------|-------------|--------------|
| **Word2Vec** | Uses context windows to learn representations | Fast, efficient, good for general use |
| **GloVe** | Based on word co-occurrence statistics | Captures global corpus statistics |
| **FastText** | Includes subword information | Handles out-of-vocabulary words better |

## Converting Text to Model Input

### **The Aggregation Problem**
- Text examples contain multiple words
- Each word → K-dimensional vector
- Need: Single fixed-length vector per document

### **Pooling Methods**
| Method | Description | Use Case |
|--------|-------------|----------|
| **Average Pooling** | Element-wise average of all word vectors | General context representation |
| **Max Pooling** | Maximum value in each dimension | Captures standout signals |
| **Min Pooling** | Minimum value in each dimension | Less commonly used |

### **Weighted Aggregation with TF-IDF**
1. Compute TF-IDF scores for words in document
2. Multiply each word vector by its TF-IDF weight
3. Apply pooling on weighted vectors
4. **Result**: Emphasizes meaningful words, reduces generic word influence

### **Dual Pooling (Average + Max)**
- Concatenate average and max pooled vectors
- Output dimension: **2 × K**
- Balances general context (average) with strong signals (max)

## Word2Vec Implementation Process

### **Training Parameters**
- **vector_size**: Dimension of each word vector (e.g., 100)
- **window**: Context words before/after target word (e.g., 5)
- **min_count**: Minimum word frequency to include (e.g., 2)

### **Typical Workflow**
1. **Preprocess text**: Tokenize, lowercase, remove punctuation
2. **Train Word2Vec model** on training corpus
3. **Convert documents to vectors**: Average word embeddings per document
4. **Train classifier** on document vectors
5. **Evaluate performance**

## Advantages vs. Disadvantages

### **Advantages**
- **Dimensionality reduction**: From hundreds of thousands to <300 features
- **Computational efficiency**: Lower memory and CPU usage
- **Less data sparsity**: Rare words share features with similar words
- **Semantic understanding**: Captures word relationships and meaning
- **Transfer learning**: Use pretrained embeddings

### **Disadvantages**
- **Training requirements**: Need large corpus for good embeddings
- **Domain dependency**: Embeddings should match your domain
- **Fixed vocabulary**: Can't handle out-of-vocabulary words (except FastText)
- **Context limitations**: Single vector per word regardless of context

## When to Use Word Embeddings vs. TF-IDF

| Scenario | Recommended Approach |
|----------|---------------------|
| **Small vocabulary, high-frequency words** | TF-IDF |
| **Large vocabulary, low-frequency words** | Word Embeddings |
| **Domain-specific text** | Custom-trained embeddings |
| **Limited training data** | Pretrained embeddings |
| **Semantic understanding needed** | Word Embeddings |
| **Fast, simple baseline** | TF-IDF |

## Interview Tips

1. **Explain the intuition**: Word embeddings capture meaning, not just frequency
2. **Know the math**: Understand cosine similarity and L2 norm
3. **Discuss aggregation**: How to convert variable-length text to fixed vectors
4. **Compare approaches**: When to use embeddings vs. TF-IDF
5. **Mention limitations**: Domain dependency, vocabulary limitations
6. **Show practical knowledge**: Gensim, Word2Vec parameters, pooling strategies
7. **Performance considerations**: Embeddings can improve performance on semantic tasks

## Key Takeaways

- Word embeddings are **dense, semantic representations** of words
- They excel at capturing **word relationships and meaning**
- **Pooling strategies** are crucial for converting document text to model input
- **Domain-specific training** often outperforms generic pretrained models
- Choose between embeddings and TF-IDF based on **vocabulary size and semantic requirements**
- **Experimentation is key**: Try different embeddings, pooling methods, and dimensions

This foundation covers the essential word embedding concepts needed for most NLP interviews, emphasizing both theoretical understanding and practical implementation considerations.