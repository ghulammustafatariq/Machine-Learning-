# Variants of Naive Bayes

Naive Bayes is a **classification algorithm** based on **Bayes Theorem**.  
Depending on the nature of the dataset (binary, text, or continuous values), we choose one of the following **three variants**:

1. **Bernoulli Naive Bayes**
2. **Multinomial Naive Bayes**
3. **Gaussian Naive Bayes**

---

## 1. Bayes Theorem Recap

Bayes theorem relates conditional probability:

$$
P(A \mid B) = \frac{P(A) \cdot P(B \mid A)}{P(B)}
$$

In classification:

$$
P(y \mid X_1, X_2, ..., X_n) \propto P(y) \cdot \prod_{i=1}^{n} P(X_i \mid y)
$$

This is the core equation behind all Naive Bayes models.

---

## 2. Bernoulli Naive Bayes

### When to Use
Use **Bernoulli Naive Bayes** when:
- Your features are **binary** (0/1, True/False, Yes/No)
- Example use cases:
  - Whether a keyword is present in a document
  - Pass/Fail outcomes
  - User clicked/not clicked

### Probability Model

Each feature follows a **Bernoulli distribution**.

For a given class \( y \):

$$
P(X_i = 1 \mid y) = \theta_{iy}
$$

The likelihood for a feature vector \(X = (x_1, x_2, ..., x_n)\):

$$
P(X \mid y) = \prod_{i=1}^{n} \theta_{iy}^{x_i} (1 - \theta_{iy})^{(1 - x_i)}
$$

### Summary
| Suitable For | Feature Type | Examples |
|---|---|---|
| Binary classification/multi-class | Binary (0/1) features | Document keyword presence, Yes/No attributes |

---

## 3. Multinomial Naive Bayes

### When to Use
Use **Multinomial Naive Bayes** when:
- Input is **text data**
- Features represent **word counts** or **term frequencies**
- Data is converted using:
  - **Bag of Words (BoW)**
  - **TF-IDF**
  - Word count vectors

### Example
Email classification:
- "You have won $1 million" → Spam
- "Meeting at 3 PM" → Not Spam (Ham)

### Probability Model

If \(x_i\) represents the **count** of word \(i\) in a document:

$$
P(X \mid y) = \frac{(\sum_i x_i)!}{\prod_i x_i!} \prod_{i=1}^{n} \theta_{iy}^{x_i}
$$

Where:

$$
\theta_{iy} = P(\text{word } i \mid \text{class } y)
$$

### Summary
| Suitable For | Feature Type | Examples |
|---|---|---|
| Text classification | Discrete counts of words | Spam detection, Topic classification, Sentiment Analysis |

---

## 4. Gaussian Naive Bayes

### When to Use
Use **Gaussian Naive Bayes** when:
- Features are **continuous**
- Values approximately follow a **normal (Gaussian) distribution**

### Example Datasets
- Iris Flower Dataset (petal length, sepal width, etc.)
- Height, weight, age-based classification tasks

### Probability Model

If a feature \(X_i\) is continuous, then:

$$
P(X_i \mid y) = \frac{1}{\sqrt{2\pi\sigma_{iy}^{2}}} \exp\left(-\frac{(X_i - \mu_{iy})^{2}}{2\sigma_{iy}^{2}}\right)
$$

Where:
- \( \mu_{iy} \) = mean of feature \(X_i\) for class \(y\)
- \( \sigma_{iy}^{2} \) = variance of feature \(X_i\) for class \(y\)

### Summary
| Suitable For | Feature Type | Examples |
|---|---|---|
| Numerical continuous features | Real numbers | Iris dataset, biometric data, sensor readings |

---

## 5. Choosing the Right Variant

| Variant | Feature Type Required | Typical Use Case |
|--------|----------------------|------------------|
| **Bernoulli NB** | Binary (0 or 1) features | Presence/absence of words |
| **Multinomial NB** | Word counts / categorical counts | NLP and text classification |
| **Gaussian NB** | Continuous numeric features | Scientific/measured data |

---

## 6. Key Takeaways

- Naive Bayes is a probability-based classification method using Bayes Theorem.
- Variant selection depends on **feature distribution**:
  - Binary → **Bernoulli NB**
  - Text (word counts) → **Multinomial NB**
  - Continuous (normal distribution) → **Gaussian NB**
- All variants share the same foundation but compute likelihoods differently.

---

