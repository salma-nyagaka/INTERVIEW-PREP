## ✅ What is NLP?

NLP (Natural Language Processing) enables machines to understand, interpret, and generate human language. Applications: sentiment analysis, chatbots, machine translation, search engines.

---

## 🔄 Core NLP Workflow

### 1. **Preprocessing**

* **Lowercasing**: Normalize text
* **Stop Words Removal**: Eliminate common, uninformative words
* **Stemming/Lemmatization**: Reduce words to root/base form
* **POS Tagging**: Label grammatical roles
* **NER**: Identify entities (e.g., names, places)

### 2. **Tokenization**

Split text into words/subwords (e.g., “not great” → \[‘not’, ‘great’])

### 3. **Vectorization**

Transform text into numeric features:

* **Binary**: 1 if present
* **Count**: Frequency of word
* **TF-IDF**: Emphasizes rare-but-important words

### 4. **Modeling**

Train ML models (Logistic Regression, Naive Bayes, RNNs, Transformers) on vectorized data.

---

## 🛠️ Preprocessing by Task

| Task                 | Strategy     | Why?                        |
| -------------------- | ------------ | --------------------------- |
| Sentiment Analysis   | Minimal      | Preserve negations, context |
| Topic Classification | Aggressive   | Focus on core content       |
| NER                  | Minimal      | Preserve structure, casing  |
| Text Generation      | None/Minimal | Maintain full context       |

---

## 📚 Key Concepts

### **N-grams**

Word combinations (unigrams, bigrams, trigrams) to preserve phrase meaning.

### **TF-IDF**

* **TF**: Word frequency
* **IDF**: Downweight common words
* **Goal**: Highlight distinct terms per document

### **Scikit Pipeline**

```python
Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])
```

Ensures clean, reproducible ML workflows.

### **min\_df / max\_df**

* **min\_df**: Ignore rare terms
* **max\_df**: Ignore overly common terms

---

## 🌍 Pros & Cons

✅ Pros:

* Automates text analysis
* Improves UX (chatbots, recommendations)
* Unlocks value in unstructured data

⚠️ Cons:

* Struggles with sarcasm/context
* Data bias risk
* Multilingual complexity
* Resource intensive

---

## 💡 Interview Insights

* Preprocessing is **task-dependent**
* Know **when to use TF-IDF vs word embeddings**
* Be fluent in **pipeline building**
* Explain **evaluation metrics** (e.g., AUC, F1)
* Think end-to-end: **text → features → model → output**

