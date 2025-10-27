# Naive Bayes Algorithm — Notes

## 1. Introduction
Naive Bayes is a **supervised machine learning classification algorithm** that applies **Bayes Theorem** with the assumption that features are **independent** of each other.

It works for:
- Binary Classification (Yes/No)
- Multi-Class Classification (A/B/C…)

---

## 2. Probability Concepts

### Independent Events
Events are **independent** if the outcome of one does *not* affect the outcome of another.

Example: Rolling a dice

$$
P(1) = P(2) = P(3) = P(4) = P(5) = P(6) = \frac{1}{6}
$$

Each roll is independent.

### Dependent Events
Events are **dependent** if one outcome affects the probability of another.

Example: Picking marbles **without replacement**

Bag: 3 Orange, 2 Yellow

$$
P(\text{Orange}) = \frac{3}{5}
$$

After removing Orange, remaining = 2 Orange, 2 Yellow:

$$
P(\text{Yellow} \mid \text{Orange}) = \frac{2}{4} = \frac{1}{2}
$$

### Conditional Probability

$$
P(A \text{ and } B) = P(A) \times P(B \mid A)
$$

---

## 3. Bayes Theorem

$$
P(A \mid B) = \frac{P(A) \times P(B \mid A)}{P(B)}
$$

Where:
- \( P(A) \) = Prior probability of event A
- \( P(B \mid A) \) = Likelihood of B given A is true
- \( P(B) \) = Total probability of event B
- \( P(A \mid B) \) = Posterior probability (updated probability)

---

## 4. Naive Bayes in Machine Learning

We want to find the probability of class \( y \) given features \( X_1, X_2, X_3... \)

$$
P(y \mid X_1, X_2, X_3) = \frac{P(y) \times P(X_1, X_2, X_3 \mid y)}{P(X_1, X_2, X_3)}
$$

### Naive Assumption (Feature Independence)

$$
P(X_1, X_2, X_3 \mid y) = P(X_1 \mid y) \times P(X_2 \mid y) \times P(X_3 \mid y)
$$

So:

$$
P(y \mid X_1, X_2, X_3) \propto P(y) \times P(X_1 \mid y) \times P(X_2 \mid y) \times P(X_3 \mid y)
$$

**Denominator is ignored** because it remains constant for all classes.

---

## 5. Example (Play Tennis Dataset)

Suppose:

- Outlook = Sunny
- Temperature = Hot
- Target = Play (Yes/No)

Example probabilities:

$$
P(\text{Sunny} \mid \text{Yes}) = \frac{2}{9}, \quad
P(\text{Hot} \mid \text{Yes}) = \frac{2}{9}, \quad
P(\text{Yes}) = \frac{9}{14}
$$

Prediction:

$$
P(\text{Yes} \mid \text{Sunny, Hot}) \propto P(\text{Yes}) \times P(\text{Sunny} \mid \text{Yes}) \times P(\text{Hot} \mid \text{Yes})
$$

Similarly, calculate for "No".  
Whichever probability is **higher**, that is the **predicted class**.

---

## 6. Key Points Summary

| Concept | Meaning |
|--------|---------|
| Naive Bayes | Classification using probabilities |
| Uses Bayes Theorem | Updates probability using evidence |
| Naive Assumption | Features are independent |
| Output | Class with highest posterior probability |

---

