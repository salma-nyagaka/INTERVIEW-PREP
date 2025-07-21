### 1. What is Natural Language Processing (NLP)?

**Answer:**
NLP is a field of AI that focuses on the interaction between computers and human languages. It enables machines to understand, interpret, generate, and respond to human language in a meaningful way.

---

### 2. What are some common NLP tasks?

**Answer:**

* Text Classification (e.g., spam detection)
* Named Entity Recognition (NER)
* Sentiment Analysis
* Machine Translation
* Text Summarization
* Part-of-Speech (POS) Tagging
* Language Modeling
* Question Answering

---

### 3. What is tokenization in NLP?

**Answer:**
Tokenization is the process of splitting text into smaller units called tokens, such as words, subwords, or characters, which serve as inputs for NLP models.

---

### 4. Explain the difference between stemming and lemmatization.

**Answer:**

* **Stemming:** Cuts off word endings crudely to reduce words to a root form (may not be a valid word).
* **Lemmatization:** Uses vocabulary and morphological analysis to reduce a word to its base or dictionary form (lemma).

---

### 5. What is a Bag-of-Words (BoW) model?

**Answer:**
BoW is a simple text representation technique that counts the frequency of each word in a document ignoring grammar and word order.

---

### 6. What are word embeddings? Name some popular ones.

**Answer:**
Word embeddings are dense vector representations of words that capture semantic meanings and relationships. Popular embeddings include Word2Vec, GloVe, and FastText.

---

### 7. What is the difference between count-based and prediction-based word embeddings?

**Answer:**

* **Count-based:** Uses statistical information like co-occurrence counts (e.g., GloVe).
* **Prediction-based:** Learns embeddings by training a predictive model to guess a word given its context (e.g., Word2Vec).

---

### 8. Explain the concept of Attention in NLP.

**Answer:**
Attention mechanisms allow models to focus on relevant parts of the input sequence when generating output, improving performance in tasks like translation and summarization.

---

### 9. What is the Transformer model?

**Answer:**
The Transformer is a neural network architecture based entirely on self-attention mechanisms without recurrent or convolutional layers, enabling efficient parallel processing of sequences.

---

### 10. How do you handle Out-Of-Vocabulary (OOV) words?

**Answer:**
- **Subword tokenization:** BPE, WordPiece, SentencePiece
- **Character-level models:** Process at character level
- **Assigning Unknown token:** Replace rare words with `<UNK>`
- **Pretrained embeddings:** Use embeddings covering larger vocabulary
- **Spelling correction:** Correct misspelled words before processing

---

### 11. What is POS tagging?

**Answer:**
Part-of-Speech tagging assigns word classes (noun, verb, adjective, etc.) to each token in a text.

---

### 12. Explain Named Entity Recognition (NER).

**Answer:**
NER identifies and classifies key information in text into predefined categories like person names, locations, dates, organizations, etc.

---

### 13. What is TF-IDF?

**Answer:**
Term Frequency-Inverse Document Frequency (TF-IDF) measures how important a word is to a document relative to a corpus, emphasizing words that are frequent in one document but rare in others.

---

### 14. What are language models? Give examples.

**Answer:**
Language models predict the probability of a sequence of words. Examples include n-gram models, RNNs, LSTMs, and large pretrained models like BERT and GPT.

---

### 15. How do you evaluate NLP models?

**Answer:**
Using metrics relevant to the task, such as accuracy, precision, recall, F1-score (for classification), BLEU (for translation), ROUGE (for summarization), or perplexity (for language models).

---


### 16. RNNs, LSTMs, and Transformer Architectures

**RNNs (Recurrent Neural Networks):**

* Designed to process sequential data by maintaining a hidden state that captures infor6mation from previous time steps.
* They take one input at a time and update their hidden state, allowing them to model dependencies across sequences.
* **Problem:** They suffer from **vanishing and exploding gradients**, which makes it hard to learn long-range dependencies.
* **Core Components**
    - **Encoder**: Takes word sequence → outputs vector/code (summary of input)
    - **Decoder**: Takes encoder vector → outputs scalar or sequence
    - **Hidden State**: Memory that persists throughout sequence

**LSTMs (Long Short-Term Memory networks):**

* A special kind of RNN designed to overcome the vanishing gradient problem.
* They have a more complex architecture with gates — input gate, forget gate, and output gate — that regulate the flow of information.
* These gates allow the model to **remember or forget** information selectively over long sequences, making LSTMs effective at capturing long-term dependencies.

**Transformer Architectures:**

* Introduced in the paper "Attention Is All You Need" (Vaswani et al., 2017).
* Unlike RNNs, Transformers do **not** process data sequentially. Instead, they rely entirely on a mechanism called **self-attention** to weigh the importance of different words in a sequence relative to each other.
* This enables **parallel processing** of sequence elements, leading to faster training and better scalability.
* Key components:

  * **Multi-head self-attention layers:** Learn different relationships from multiple representation subspaces.
  * **Positional encoding:** Since the model does not process sequence data in order, positional encoding adds information about the position of words.
  * **Feed-forward networks:** Fully connected layers applied after attention.
* Transformers have become the basis for most state-of-the-art NLP models.

---

### 18. Architecture of BERT and Its Training Objectives

**BERT (Bidirectional Encoder Representations from Transformers):**

* BERT is a Transformer-based model, specifically **the encoder part of the Transformer architecture** stacked multiple times (usually 12 or 24 layers).
* It is **bidirectional**, meaning it looks at context from both left and right of a token simultaneously, unlike traditional unidirectional models.

**Key Architectural Features:**

* Input representation combines tokens, segment embeddings (to distinguish sentence pairs), and positional embeddings.
* Uses multi-layer bidirectional self-attention to build deep contextual representations.

**Training Objectives:**
BERT is pretrained on large corpora using two main unsupervised objectives:

1. **Masked Language Modeling (MLM):**

   * Randomly masks (hides) about 15% of input tokens and the model tries to predict these masked tokens based on their context (both left and right).
   * This forces the model to understand context deeply and learn bidirectional representations.

2. **Next Sentence Prediction (NSP):**

   * Given pairs of sentences, the model predicts whether the second sentence logically follows the first.
   * Helps BERT understand relationships between sentences, useful for tasks like Question Answering and Natural Language Inference.

After pretraining, BERT can be **fine-tuned** on specific NLP tasks with relatively small datasets by adding simple task-specific layers on top.

---

