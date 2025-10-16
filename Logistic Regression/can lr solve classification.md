# Can Linear Regression Solve Classification Problems?

## 1. Introduction
- **Linear Regression**: Previously studied for predicting continuous values.
- **Logistic Regression**: A new algorithm designed for **binary classification problems**.

Example:  
- Input feature: **Study Hours**  
- Output feature: **Pass (1) / Fail (0)**  

Goal → Predict whether a student **passes or fails** given study hours.

---

## 2. What is Binary Classification?
- A **binary classification problem** means the target variable has **two categories**.
- Example:
  - Study = 2, 3, 4 hours → **Fail (0)**
  - Study ≥ 5 hours → **Pass (1)**

---

## 3. Can We Use Linear Regression for Classification?
- If we use linear regression:
  - Find best fit line.
  - Apply thresholding:
    - If prediction ≤ 0.5 → Class 0 (Fail)
    - If prediction > 0.5 → Class 1 (Pass)

Mathematically:

$$
\hat{y} = w_0 + w_1 x
$$

Classification rule:

$$
\hat{y}_{class} =
\begin{cases}
0 & \text{if } \hat{y} \leq 0.5 \\
1 & \text{if } \hat{y} > 0.5
\end{cases}
$$

---

## 4. Problems with Linear Regression in Classification
1. **Effect of Outliers**  
   - Example: A student studies for 12 hours → Pass.  
   - Outlier drastically shifts the regression line → Wrong predictions.

2. **Predictions Outside [0,1]**  
   - Linear regression can give $\hat{y} < 0$ or $\hat{y} > 1$.  
   - Invalid as probabilities must lie in **[0,1]**.

---

## 5. Need for Squashing Function
- For classification, we want predictions **restricted between 0 and 1**.
- Linear regression **cannot squash outputs**.

---

## 6. Why Logistic Regression?
- Logistic regression introduces a **squashing function** (Sigmoid Function):

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

where

$$
z = w_0 + w_1 x
$$

- Properties:
  - Maps any real value into **(0,1)**.
  - Ensures valid probability outputs.

Classification decision:

$$
\hat{y}_{class} =
\begin{cases}
0 & \text{if } \sigma(z) \leq 0.5 \\
1 & \text{if } \sigma(z) > 0.5
\end{cases}
$$

---

## 7. Summary: Why Not Use Linear Regression?
- **Problem 1**: Outliers shift regression line → wrong predictions.  
- **Problem 2**: Predictions may fall outside [0,1].  
- **Logistic Regression Fix**: Uses sigmoid to squash outputs into [0,1].

---

## 8. Key Takeaways
- Logistic regression is designed for **binary classification**.
- Linear regression is **not suitable** for classification due to:
  - Sensitivity to outliers.
  - Invalid probability predictions (<0 or >1).
- Logistic regression ensures outputs are squashed to **[0,1]**, making it ideal for classification.

---
