# Word Embeddings Interview Summary

## What Are Word Embeddings?

Dense vector representations of words that capture **semantic meaning** and **relationships**, unlike frequency-based methods like TF-IDF.

## Key Concepts

* **K-dimensional dense vectors** (e.g., 100–300 dims)
* **Semantic similarity**: Similar words → similar vectors
* **Cosine similarity** measures vector closeness:

  $$
  \text{sim}(V₁, V₂) = \frac{V₁ \cdot V₂}{\|V₁\|\|V₂\|}
  $$
* Vector arithmetic reflects relationships (e.g., `king - man + woman ≈ queen`)

## Popular Models

| Model    | Highlights                            |
| -------- | ------------------------------------- |
| Word2Vec | Learns from local context windows     |
| GloVe    | Uses global co-occurrence stats       |
| FastText | Uses subword info (handles OOV words) |

## From Words to Document Vectors

**Challenge:** Each word is a vector; models need fixed-size input per document

### Pooling Methods

| Method       | Description                 | Use Case                    |
| ------------ | --------------------------- | --------------------------- |
| Average      | Mean of all word vectors    | General context             |
| Max          | Max value in each dimension | Emphasizes key signals      |
| TF-IDF Avg   | Weighted average by TF-IDF  | Reduces generic word impact |
| Dual Pooling | Concatenate Avg + Max       | Captures context + signals  |

## Word2Vec Training Summary

* **vector\_size**: Output dimension (e.g., 100)
* **window**: Context size
* **min\_count**: Ignore rare words
* **Workflow:**

  1. Preprocess text
  2. Train model (Gensim)
  3. Convert docs to vectors
  4. Train classifier
  5. Evaluate performance

## Pros and Cons

| Pros                              | Cons                                         |
| --------------------------------- | -------------------------------------------- |
| Captures meaning + relationships  | Needs large corpus for good training         |
| Dense, compact vectors            | Context-independent (same vector per word)   |
| Enables transfer learning         | May not handle domain shifts or OOV          |
| Reduces dimensionality & sparsity | TF-IDF may outperform for small vocabularies |

## When to Use Word Embeddings

| Situation                     | Preferred Method      |
| ----------------------------- | --------------------- |
| Semantic meaning needed       | Word Embeddings       |
| Large vocab / sparse data     | Word Embeddings       |
| Small data or baseline needed | TF-IDF                |
| Domain-specific terminology   | Custom embeddings     |
| Fast prototyping              | Pretrained embeddings |

## Interview Must-Knows

* **Intuition**: Embeddings reflect meaning, not frequency
* **Math**: Cosine similarity, vector norms
* **Aggregation**: Convert word vectors to doc-level vectors
* **When to use**: Embeddings vs. TF-IDF
* **Limitations**: Fixed vocab, context blindness
* **Tools**: Gensim, pooling strategies
* **Performance Tip**: Pooling method and vector choice affect accuracy

---

### Bottom Line

Word embeddings are compact, semantic-rich vectors ideal for capturing meaning in NLP. Combined with smart pooling and training strategies, they offer a powerful alternative to sparse methods like TF-IDF—especially when understanding relationships matters.

