# Common NLP Interview Questions

## Foundation & Concepts

### **Q1: What is NLP and why is it challenging?**
**A:** Natural Language Processing is a field that enables computers to understand, interpret, and generate human language. 

**Challenges:**
- **Ambiguity:** "Bank" (financial institution vs river bank)
- **Context dependency:** "It's cool" (temperature vs impressive)
- **Syntax variations:** Multiple ways to express same meaning
- **Cultural nuances:** Idioms, sarcasm, cultural references
- **Data sparsity:** Long-tail words and phrases
- **Dynamic nature:** Language evolves constantly

### **Q2: Explain the difference between stemming and lemmatization.**
**A:** Both reduce words to their root forms, but differ in approach:

**Stemming:**
- **Method:** Rule-based suffix removal
- **Example:** "running", "runs", "ran" → "run"
- **Speed:** Faster
- **Accuracy:** Lower (may produce non-words)

**Lemmatization:**
- **Method:** Uses vocabulary and morphological analysis
- **Example:** "better" → "good", "mice" → "mouse"
- **Speed:** Slower
- **Accuracy:** Higher (produces actual words)

**When to use:** Stemming for search engines, lemmatization for analysis requiring meaning preservation.

### **Q3: What are stop words and when would you remove them?**
**A:** Stop words are common words like "the", "is", "and" that appear frequently but carry little semantic meaning.

**Remove when:**
- Building search engines (reduce index size)
- Topic modeling (focus on content words)
- Sentiment analysis with simple models

**Keep when:**
- Machine translation (grammatical structure matters)
- Named entity recognition (context important)
- Modern neural models (can learn relevance)

## Text Preprocessing & Feature Engineering

### **Q4: How do you handle out-of-vocabulary (OOV) words?**
**A:** 
- **Subword tokenization:** BPE, WordPiece, SentencePiece
- **Character-level models:** Process at character level
- **Unknown token:** Replace rare words with `<UNK>`
- **Pretrained embeddings:** Use embeddings covering larger vocabulary
- **Spelling correction:** Correct misspelled words before processing

### **Q5: Explain TF-IDF and its limitations.**
**A:** Term Frequency-Inverse Document Frequency measures word importance.

**Formula:** TF-IDF = TF(t,d) × IDF(t)
- **TF:** Term frequency in document
- **IDF:** log(Total docs / Docs containing term)

**Limitations:**
- **No semantic understanding:** "car" and "automobile" are different
- **Linear relationships:** Can't capture complex patterns
- **Sparse vectors:** High-dimensional, mostly zeros
- **No context:** Same word always gets same weight

### **Q6: How do you handle class imbalance in text classification?**
**A:**
- **Resampling:** Oversample minority, undersample majority
- **Class weights:** Penalize majority class errors more
- **SMOTE:** Generate synthetic minority examples
- **Ensemble methods:** Combine multiple models
- **Threshold tuning:** Adjust classification threshold
- **Focal loss:** Focus on hard examples

## Word Embeddings & Representations

### **Q7: What are word embeddings and how do Word2Vec models work?**
**A:** Word embeddings are dense vector representations capturing semantic relationships.

**Word2Vec variants:**
- **Skip-gram:** Predict context words from target word
- **CBOW:** Predict target word from context words

**Training:** Neural network with softmax, optimized with negative sampling
**Properties:** Similar words have similar vectors, captures analogies (king - man + woman = queen)

### **Q8: Compare Word2Vec, GloVe, and modern contextual embeddings.**
**A:**

| Feature | Word2Vec | GloVe | BERT/Contextual |
|---------|----------|-------|-----------------|
| **Context** | Local window | Global statistics | Full sequence |
| **Training** | Neural network | Matrix factorization | Transformer |
| **Polysemy** | Single vector | Single vector | Multiple vectors |
| **Performance** | Good | Good | State-of-art |
| **Speed** | Fast | Fast | Slower |

**Use cases:** Word2Vec for similarity, GloVe for analogy tasks, BERT for downstream tasks.

### **Q9: What is the attention mechanism and why is it important?**
**A:** Attention allows models to focus on relevant parts of input when making predictions.

**Benefits:**
- **Long sequences:** Doesn't lose information like RNNs
- **Parallelization:** All positions processed simultaneously  
- **Interpretability:** Can visualize what model focuses on
- **Better performance:** Captures long-range dependencies

**Types:** Self-attention (BERT), cross-attention (translation), multi-head attention

## Deep Learning for NLP

### **Q10: Explain the architecture of BERT and its training objectives.**
**A:** BERT (Bidirectional Encoder Representations from Transformers) uses transformer encoder architecture.

**Training objectives:**
- **Masked Language Model (MLM):** Predict masked tokens (15% of input)
- **Next Sentence Prediction (NSP):** Predict if sentence B follows sentence A

**Key features:**
- **Bidirectional:** Sees context from both directions
- **Transfer learning:** Pretrain then fine-tune
- **Attention-based:** No recurrence or convolution

### **Q11: What are the differences between RNN, LSTM, and Transformer architectures?**
**A:**

**RNN:**
- **Sequential processing:** One word at a time
- **Memory:** Hidden state carries information
- **Problem:** Vanishing gradient, can't remember long sequences

**LSTM:**
- **Gates:** Forget, input, output gates control information flow
- **Better memory:** Can remember longer sequences
- **Still sequential:** Cannot parallelize training

**Transformer:**
- **Parallel processing:** All positions simultaneously
- **Self-attention:** Directly connects any two positions
- **No recurrence:** Faster training, better long-range dependencies

### **Q12: How do you evaluate NLP models?**
**A:**

**Classification metrics:**
- **Accuracy:** Overall correctness
- **Precision/Recall:** Class-specific performance
- **F1-score:** Harmonic mean of precision/recall
- **Confusion matrix:** Detailed error analysis

**Sequence labeling:**
- **Entity-level F1:** For named entity recognition
- **Token-level accuracy:** Per-token correctness

**Text generation:**
- **BLEU:** N-gram overlap with reference
- **ROUGE:** Recall-oriented for summarization
- **Perplexity:** Model uncertainty measure
- **Human evaluation:** Fluency, coherence, relevance

## Advanced Topics

### **Q13: What is transfer learning in NLP and how do you implement it?**
**A:** Using pretrained models as starting point for specific tasks.

**Approach:**
1. **Pretrained model:** BERT, GPT, RoBERTa on large corpus
2. **Task-specific layer:** Add classification/regression head
3. **Fine-tuning:** Train on target dataset with lower learning rate
4. **Freezing:** Optionally freeze early layers

**Benefits:** Better performance with less data, faster training

### **Q14: Explain few-shot and zero-shot learning in NLP.**
**A:**

**Few-shot learning:**
- **Definition:** Learn from very few examples (1-10 per class)
- **Methods:** Meta-learning, prompt engineering, in-context learning
- **Example:** GPT-3 with few examples in prompt

**Zero-shot learning:**
- **Definition:** No training examples for target classes
- **Methods:** Use class descriptions, transfer from related tasks
- **Example:** "Classify sentiment: positive/negative" without training data

### **Q15: How do you handle multiple languages in NLP systems?**
**A:**

**Approaches:**
- **Multilingual models:** mBERT, XLM-R trained on multiple languages
- **Translation-based:** Translate to English, process, translate back
- **Language-specific models:** Separate models per language
- **Code-switching:** Handle mixed-language text

**Challenges:** Different writing systems, resource availability, cultural contexts

## Practical Implementation

### **Q16: How do you build a text classification system from scratch?**
**A:**

**Steps:**
1. **Data collection:** Gather labeled examples
2. **Preprocessing:** Clean, tokenize, normalize text
3. **Feature extraction:** TF-IDF, embeddings, or raw text
4. **Model selection:** Logistic regression → neural networks
5. **Training:** Split data, train with validation
6. **Evaluation:** Test set performance, error analysis
7. **Deployment:** API, monitoring, retraining pipeline

### **Q17: What are common challenges in production NLP systems?**
**A:**

**Technical challenges:**
- **Latency:** Real-time inference requirements
- **Scalability:** Handle high request volumes
- **Model drift:** Performance degradation over time
- **Data quality:** Inconsistent, noisy input data

**Business challenges:**
- **Interpretability:** Explaining model decisions
- **Bias:** Unfair treatment of groups
- **Privacy:** Sensitive information in text
- **Maintenance:** Keeping models updated

### **Q18: How do you debug an underperforming NLP model?**
**A:**

**Systematic approach:**
1. **Data analysis:** Check label distribution, text quality
2. **Error analysis:** Examine misclassified examples
3. **Feature inspection:** Visualize embeddings, attention weights
4. **Baseline comparison:** Simple models, random baseline
5. **Ablation studies:** Remove components to find issues
6. **Cross-validation:** Ensure consistent performance

## Domain-Specific Questions

### **Q19: How would you build a chatbot?**
**A:**

**Architecture components:**
1. **Intent classification:** Understand user goal
2. **Entity extraction:** Extract key information
3. **Dialogue management:** Track conversation state
4. **Response generation:** Template-based or neural
5. **Context handling:** Remember conversation history

**Approaches:** Rule-based → ML-based → end-to-end neural

### **Q20: Explain how you would approach sentiment analysis for social media.**
**A:**

**Challenges:**
- **Informal language:** Slang, abbreviations, typos
- **Sarcasm:** Opposite of literal meaning
- **Emoji handling:** Convert to text or special tokens
- **Context:** Reply chains, mentions

**Solution approach:**
1. **Data preprocessing:** Handle social media artifacts
2. **Feature engineering:** N-grams, emoji features, user features
3. **Model choice:** BERT fine-tuned on social media data
4. **Evaluation:** Consider class imbalance, use F1-score

## Practical Tips for Interviews

**Preparation strategy:**
✅ **Understand fundamentals:** Don't just memorize, understand concepts
✅ **Hands-on experience:** Build projects, experiment with libraries
✅ **Current trends:** Stay updated with latest research
✅ **Business context:** Connect technical solutions to business problems
✅ **Code examples:** Be ready to write preprocessing code
✅ **Trade-offs:** Discuss pros/cons of different approaches

**Key Point:** NLP interviews test both theoretical understanding and practical implementation skills. Focus on explaining concepts clearly and connecting them to real-world applications.