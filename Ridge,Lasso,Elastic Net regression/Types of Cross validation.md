# 📘 Notes: Types of Cross-Validation

## 🔹 Introduction
- In ML, we split data into:
  - **Training set** → used to train the model.
  - **Validation set** → used for hyperparameter tuning (e.g., GridSearchCV, RandomizedSearchCV).
  - **Test set** → used only for final evaluation on unseen data.

- The **test data must remain untouched** during training & validation to ensure unbiased performance.

---

## 🔹 Why Cross-Validation?
- A single train/validation split may give different results depending on random state.
- Cross-validation (CV) improves reliability by averaging performance across multiple splits.

Example:  
One split → 85% accuracy, another → 92%, another → 75%.  
CV gives an **average accuracy** → more reliable estimate.

---

## 🔹 Types of Cross-Validation

### 1. Leave-One-Out Cross Validation (LOOCV)
- If dataset has $n$ records → perform $n$ experiments.
- Each experiment uses:
  - 1 record as validation.
  - $n-1$ records as training.

Example ($n=500$):
- Exp. 1 → Record 1 validation, Records 2–500 training.
- Exp. 2 → Record 2 validation, Records 1, 3–500 training.
- Continue until Exp. 500.

**Disadvantages:**
- Computationally very expensive.
- Validation set is too small (1 record).
- High variance in accuracy.  
👉 Rarely used for large datasets.

---

### 2. Leave-P-Out Cross Validation
- Generalization of LOOCV → leave $p$ records out for validation each time.
- $p$ can be 10, 20, etc. (chosen as hyperparameter).
- Same drawbacks: **computationally heavy** and not widely used.

---

### 3. K-Fold Cross Validation
- Training data is split into $k$ equal parts (**folds**).
- Each fold is used once as validation, others as training.

Formula for test size per fold:

$$
\text{Test size per fold} = \frac{n}{k}
$$

where $n$ = number of records, $k$ = number of folds.

Example ($n=500$, $k=5$):
- Each fold = 100 records.
- Exp. 1 → Fold 1 validation, Folds 2–5 training.
- Exp. 2 → Fold 2 validation, Folds 1, 3–5 training.
- Continue until Exp. 5.

**Advantages:**
- Less variance than single split.
- Much cheaper than LOOCV.
- Gives reliable performance estimate.  
Final report includes:
- Max accuracy
- Min accuracy
- Average accuracy

---

### 4. Stratified K-Fold Cross Validation
- Variation of K-Fold, mainly for **classification problems**.
- Ensures each fold has **same class proportion** as original dataset.

Example:  
Binary classification with 60% ones, 40% zeros → each fold keeps 60:40 ratio.

👉 Prevents unbalanced folds that could mislead evaluation.

---

### 5. Time Series Cross Validation
- Used for **time-dependent data**.
- Random splitting is not valid (causes data leakage).
- Splitting respects **temporal order**.

Example:
- Train: Day 1 → Day 4  
- Validate: Day 5 → Day N  

- Validation always comes **after training data in time**.
- Used in stock predictions, sentiment analysis, etc.

---

## 🔹 Summary Table

| Method                  | Description | Pros | Cons |
|--------------------------|-------------|------|------|
| **LOOCV** | Leave 1 record out per experiment | Uses all data | Very expensive, prone to overfitting |
| **Leave-P-Out** | Leave $p$ records out | Generalization of LOOCV | Still expensive |
| **K-Fold** | Split into $k$ folds | Efficient, reliable | Random splits may cause imbalance |
| **Stratified K-Fold** | Keeps class ratio in folds | Best for classification | Slightly slower |
| **Time Series CV** | Sequential split by time | Prevents leakage | Only for temporal data |

---

## 🔑 Key Takeaways
- Cross-validation ensures **reliable evaluation** & **hyperparameter tuning**.
- **LOOCV** → theoretical, expensive, not practical for large data.
- **Leave-P-Out** → same drawbacks as LOOCV.
- **K-Fold** → most common & efficient for general tasks.
- **Stratified K-Fold** → best choice for classification.
- **Time Series CV** → mandatory for time-dependent data.
