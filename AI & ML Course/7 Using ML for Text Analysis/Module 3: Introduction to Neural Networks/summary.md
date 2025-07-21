# Neural Networks Interview Summary

## What Are Neural Networks?

Models inspired by the brain, using layers of neurons to learn complex, non-linear patterns beyond linear models.

## Core Architecture

* **Input Layer:** Receives data
* **Hidden Layers:** Transform data via weighted sums + activations
* **Output Layer:** Produces predictions
* **Neurons:** Processing units in each layer

## Information Flow

1. Forward propagation: input → hidden layers → output
2. Weighted sums at each neuron
3. Non-linear activation applied
4. Pass to next layer

## Key Hyperparameters

| Aspect          | Options                        | Notes                           |
| --------------- | ------------------------------ | ------------------------------- |
| Layers          | 1–10+ (shallow to deep)        | More layers → complex patterns  |
| Nodes per Layer | 10–1000+                       | Higher capacity                 |
| Activation      | ReLU (standard), Sigmoid, Tanh | ReLU avoids vanishing gradients |

## Activation Functions

* **ReLU:** max(0, x), fast, no vanishing gradient, preferred
* **Sigmoid:** output 0–1, vanishing gradients, for binary outputs
* **Tanh:** output -1 to 1, vanishing gradients, less common

## Training Process

* Forward pass: compute predictions
* Backpropagation: compute gradients via chain rule
* Gradient descent (usually SGD) updates weights
* Challenges: vanishing gradients, huge parameter space, compute needs

## When to Use Neural Networks

* Complex, non-linear data relationships
* Large datasets
* Unstructured data (images, text, audio)
* When linear models fail

## Applications

* Computer vision
* NLP (sentiment analysis, translation)
* Speech recognition
* Time series forecasting

## Pros and Cons

| Pros                             | Cons                            |
| -------------------------------- | ------------------------------- |
| Universal function approximators | Hard to interpret (“black box”) |
| Automatic feature extraction     | Requires large data             |
| Scales with data and compute     | Computationally intensive       |
| Versatile across domains         | Prone to overfitting            |

## Gradient Descent Evolution

* Standard GD uses full dataset (slow, memory-heavy)
* **SGD:** uses mini-batches for faster, scalable training

## Interview Highlights

* Neural nets combine layers + non-linear activations for complex patterns
* ReLU solves vanishing gradient and speeds training
* Start simple, then grow model complexity iteratively
* Use for complex, large, unstructured data

---

### How do you evaluate NLP models?

**Answer:**
Using metrics relevant to the task, such as accuracy, precision, recall, F1-score (for classification), BLEU (for translation), ROUGE (for summarization), or perplexity (for language models).

**Bottom line:**
Neural networks model complex non-linear functions via stacked weighted layers and activations (ReLU preferred). They excel on large, complex datasets but need careful design and substantial compute. Training uses forward pass, backpropagation, and SGD for optimization.

