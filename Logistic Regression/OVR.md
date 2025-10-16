# 📘 Logistic Regression – One Versus Rest (OVR) for Multi-Class Classification

## 1. Introduction
- **Binary classification**: Logistic regression finds a decision boundary to separate **two classes**.  
- **Multi-class classification**: When the dataset has **3 or more classes** (e.g., Class A, Class B, Class C), we extend logistic regression using **One Versus Rest (OVR)**.  

---

## 2. Concept of OVR
- OVR creates **multiple binary classifiers**, one for each class.  
- Each classifier predicts **“this class vs. all others”**.  
- If we have $K$ classes, then we build **$K$ models**:

$$
M_1: \text{Class 1 vs. (Class 2, Class 3, ..., Class K)}
$$

$$
M_2: \text{Class 2 vs. (Class 1, Class 3, ..., Class K)}
$$

$$
M_K: \text{Class K vs. (Class 1, Class 2, ..., Class K-1)}
$$

---

## 3. Example with 3 Classes
Suppose features: $f_1, f_2, f_3$  
Output categories: $1, 2, 3$

- **Model $M_1$**: Classifies category 1 vs. {2, 3}  
- **Model $M_2$**: Classifies category 2 vs. {1, 3}  
- **Model $M_3$**: Classifies category 3 vs. {1, 2}  

Each model is a binary classifier.

---

## 4. One-Hot Encoding
To prepare labels for each binary model:
- Class 1 → [1, 0, 0]  
- Class 2 → [0, 1, 0]  
- Class 3 → [0, 0, 1]  

Each binary classifier uses the same input features but a different binary output (targeted class vs. others).

---

## 5. Prediction Phase
- A new test data point is passed to all models.  
- Each model outputs a **probability** using the sigmoid function:

$$
P(y = k \mid X) = \frac{1}{1 + e^{-(\beta_0^{(k)} + \beta_1^{(k)}x_1 + \dots + \beta_n^{(k)}x_n)}}
$$

Where:
- $k$ = class index (1, 2, ..., K)  
- $\beta^{(k)}$ = parameters of model $M_k$  

- Example:  
  - $M_1 \to 0.25$  
  - $M_2 \to 0.20$  
  - $M_3 \to 0.55$  

✅ Final prediction = **Class 3**, since it has the highest probability.

---

## 6. Key Takeaways
- Logistic regression can be extended to **multi-class classification** using **OVR**.  
- Build **$K$ binary classifiers** for $K$ classes.  
- Each classifier outputs a probability.  
- The class with the **highest probability** is chosen as the prediction.  
- **One-hot encoding** is used to represent labels for training.  

---
