# Deep Learning & RNNs Interview Summary

## Deep Learning Overview

Neural networks with many layers that learn complex patterns automatically, powering breakthroughs in NLP, vision, and speech.

## Why Deep Learning Dominates

* Proven success on complex tasks
* GPU/cloud enable large-scale training
* Big datasets fuel model learning

## Feed-Forward Network Limitations

* No memory of prior inputs
* Cannot handle sequence or context
* No notion of time or order

## Recurrent Neural Networks (RNNs)

* Designed for sequential data with memory
* Maintain a hidden state to remember past inputs
* Process input step-by-step, accumulating context

## RNN Architecture

* **Encoder:** Converts input sequence to vector
* **Decoder:** Generates output from vector
* **Hidden State:** Carries sequence memory
* Recurrence: hidden state at step *i* depends on previous state and current input
* Formula: $h_i = \sigma(W h_{i-1} + U s_i)$

## Advanced RNN Variants

* **LSTM:** Adds gates to preserve long-term memory, solves vanishing gradients
* **BiLSTM:** Processes sequence forward & backward for better context capture

## Training RNNs

* Use backpropagation through time (BPTT) with SGD(Stochastic Gradient Descent)
   - Backpropagation Through Time: Updates parameters across sequence
   Sequence Learning: Learns from input-output sequence pairs
* Example: machine translation via encoder-decoder RNNs

## Applications

* Machine Translation, Sentiment Analysis, Summarization, Question Answering, Text Generation
* Excel at sequential, context-dependent tasks

## Encoder-Decoder Model

* Encoder summarizes input to fixed vector
* Decoder generates output sequence from vector
* Used in translation, summarization, Q\&A

## Key Interview Takeaways

* RNNs have memory through hidden states, unlike feed-forward nets
* LSTMs improve long-term dependency learning
* Bidirectional RNNs capture context from both directions
* Ideal for sequential data like text, speech, time series

## RNN vs Feed-Forward Summary

| Aspect             | Feed-Forward    | RNN                 |
| ------------------ | --------------- | ------------------- |
| Memory             | None            | Hidden state memory |
| Sequential Data    | No              | Yes                 |
| Context Handling   | No              | Yes                 |
| Text Processing    | Word-wise only  | Sequence-aware      |
| Suitable for Tasks | Static patterns | Dynamic sequences   |

---

**Bottom line:**
RNNs add memory to handle sequences, essential for NLP tasks involving order and context. LSTM and BiLSTM variants enhance this with better long-term memory and bidirectional understanding, forming the backbone of modern NLP models.

