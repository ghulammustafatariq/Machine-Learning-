# K-Nearest Neighbor (KNN) — Classification & Regression (In-Depth Intuition)

## 1. Introduction
**K-Nearest Neighbor (KNN)** is one of the simplest machine learning algorithms.  
It can be used for:
- **Classification** (categorical output)
- **Regression** (continuous numerical output)

KNN is known as a **lazy learner** because it does **not** build a model during training.  
It simply stores the dataset and performs computation **during prediction time**.

---

## 2. KNN for Classification

### Problem Setting
We have a dataset with features \( F_1, F_2, \dots, F_n \) and a target class \( Y \).  
Some points belong to **Class 0**, and others belong to **Class 1**.

Our task is to classify a **new incoming data point**.

---

## 3. Steps in KNN Classification

### Step 1: Choose the value of \( k \)
- \( k \) represents the number of nearest neighbors considered.
- \( k \) is a **hyperparameter**.
- A common approach is to choose odd \( k \) for binary classification to avoid ties.

---

### Step 2: Calculate Distance Between Points
To determine “nearest” neighbors, we use a distance metric.

#### **Euclidean Distance**
For two points \( (x_1, y_1) \) and \( (x_2, y_2) \):

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

For higher dimensions:

$$
d = \sqrt{\sum_{i=1}^{n}(p_i - q_i)^2}
$$

#### **Manhattan Distance**
$$
d = \sum_{i=1}^{n} |p_i - q_i|
$$

- Euclidean = straight line distance
- Manhattan = city-block distance (like moving through streets)

---

### Step 3: Find the \( k \) Nearest Neighbors
Sort all distances and pick the **top \( k \)** smallest ones.

---

### Step 4: Perform Majority Voting
The new data point is assigned to the class that occurs **most frequently** among its \( k \) nearest neighbors.

Example:
- If \( k = 5 \)
- Neighbors → 3 belong to Class 1 and 2 belong to Class 0  
→ Prediction = **Class 1**

---

## 4. KNN for Regression

When the output variable is **continuous**, KNN works by **averaging** instead of voting.

### Steps:
1. Find the \( k \) nearest neighbors.
2. Take the **mean** of their output values.

#### Prediction Formula:
If the nearest neighbor outputs are \( y_1, y_2, \dots, y_k \):

$$
\hat{y} = \frac{1}{k} \sum_{i=1}^{k} y_i
$$

If there are **outliers**, instead of mean, **median** can be used.

---

## 5. Choosing the Right Distance Metric
| Metric | When to Use | Interpretation |
|-------|-------------|----------------|
| Euclidean | Data is continuous | Straight-line distance |
| Manhattan | Movement is grid-like or features have different scales | Add absolute differences |

---

## 6. Computational Complexity
To classify one test point, the model must:
- Compute distance from all \( n \) training samples  
→ **Time Complexity = \( O(n) \)** per prediction

To optimize, we use data structures:
- **KD Tree**
- **Ball Tree**

These reduce search operations and speed up KNN.

---

## 7. Summary (Key Takeaways)

- KNN is simple, intuitive, and works for both **classification and regression**.
- The **value of \( k \)** heavily affects model performance.
- Distance metrics such as **Euclidean** and **Manhattan** determine how “closeness” is measured.
- KNN does **not** train a model — it is a **lazy learner**.
- For regression, prediction is done using **mean/median** of neighbors.
- KD Tree and Ball Tree can optimize KNN for large datasets.

---
