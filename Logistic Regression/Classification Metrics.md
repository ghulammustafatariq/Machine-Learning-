# 📘 Performance Metrics in Classification

## 1. Introduction
- In **regression**, we use metrics like **$R^2$** and **adjusted $R^2$**.  
- In **classification**, we need different metrics:
  - Confusion Matrix
  - Accuracy
  - Precision
  - Recall
  - F-beta Score  

These help evaluate how well a classifier (e.g., logistic regression) performs.

---

## 2. Confusion Matrix

For binary classification, the **confusion matrix** is a $2 \times 2$ table:

| Actual \ Predicted | 1 (Positive) | 0 (Negative) |
|--------------------|--------------|--------------|
| 1 (Positive)       | **TP** (True Positive) | **FN** (False Negative) |
| 0 (Negative)       | **FP** (False Positive) | **TN** (True Negative) |

- **True Positive (TP):** Model correctly predicts positive.  
- **True Negative (TN):** Model correctly predicts negative.  
- **False Positive (FP):** Model predicts positive but actual is negative.  
- **False Negative (FN):** Model predicts negative but actual is positive.  

✅ Diagonal (TP, TN) → correct predictions.  
❌ Off-diagonal (FP, FN) → errors.

---

## 3. Accuracy

Accuracy is the proportion of correct predictions:

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

Example:  
If $TP = 4, FP = 2, FN = 1, TN = 1$:  

$$
\text{Accuracy} = \frac{4+1}{4+2+1+1} = \frac{5}{8} = 0.625
$$

⚠️ **Limitation:** Accuracy can be misleading on **imbalanced datasets**.

---

## 4. Precision and Recall

### Precision
Measures **how many predicted positives are actually correct**:

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

- Focus: **minimize false positives**.  

---

### Recall
Measures **how many actual positives were correctly predicted**:

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

- Focus: **minimize false negatives**.  

---

### When to Use Precision vs Recall
- **Spam Detection (Precision important):**  
  - FP = important email marked as spam → costly.  
- **Medical Diagnosis (Recall important):**  
  - FN = sick patient predicted as healthy → dangerous.  

---

## 5. F-beta Score

Balances **precision** and **recall** into one metric:

$$
F_\beta = (1 + \beta^2) \cdot \frac{\text{Precision} \cdot \text{Recall}}{(\beta^2 \cdot \text{Precision}) + \text{Recall}}
$$

- **$\beta = 1$ → F1 Score** (equal weight to precision & recall).  
- **$\beta < 1$** → precision more important (minimize false positives).  
- **$\beta > 1$** → recall more important (minimize false negatives).  

---

## 6. Summary

- **Confusion Matrix** → complete picture of predictions.  
- **Accuracy** → useful but misleading for imbalanced datasets.  
- **Precision** → focus on **false positives**.  
- **Recall** → focus on **false negatives**.  
- **F-beta Score** → combines precision & recall with adjustable importance.  

---

## 🔑 Key Takeaways
- Classification metrics differ from regression metrics.  
- Confusion matrix provides detailed breakdown.  
- Use **precision** when false positives are costly.  
- Use **recall** when false negatives are costly.  
- **F-beta score** allows balancing based on the problem.  
