# 🧮 SVC Cost Function — Support Vector Classifier

## 📌 Introduction

The main objective of a **Support Vector Classifier (SVC)** is to **maximize the margin** between the marginal planes.  
This is done by adjusting the parameters $w$ (weights) and $b$ (bias).

The margin is given by:

$$
\text{Margin} = \frac{2}{\|w\|}
$$

Maximizing the margin means finding $w$ and $b$ such that this distance is as large as possible.

---

## 🧭 Constraints for Classification

There are two main classification rules:

- If $w^T x + b \geq 1$ → label as **$+1$**  
- If $w^T x + b \leq -1$ → label as **$-1$**

For all correctly classified points:

$$
y_i (w^T x_i + b) \geq 1
$$

This holds even when multiplying two negative values, because the product remains positive.

---

## 🧮 Reformulating the Cost Function

The cost function can be written in two equivalent forms:

1. **Maximizing the margin**:

$$
\max_{w, b} \frac{2}{\|w\|}
$$

2. **Minimizing the weight norm** (preferred in ML optimization):

$$
\min_{w, b} \frac{1}{2} \|w\|^2
$$

Both are equivalent since maximizing $\frac{2}{\|w\|}$ is the same as minimizing $\|w\|$.

---

## ☁️ Real-World Scenario — Need for Soft Margin

In practice, data is **not always linearly separable**.  
Some points may overlap, making perfect separation impossible.

To address this, we introduce **hyperparameters** that allow **controlled misclassification**.

---

## ⚙️ Introducing Hyperparameters: $C_i$ and $\eta_i$

- $C_i$ controls how many misclassifications are allowed.  
  - Example: $C_i = 5$ means we can tolerate up to 5 misclassified points.
- $\eta_i$ (slack variables) represent the **distance of misclassified points** from the margin.

We sum the $\eta_i$ values over all $i$:

$$
\sum_{i=1}^n \eta_i
$$

This measures the **total violation** of the margin by all misclassified points.

---

## 🧱 Soft Margin Cost Function (with Hinge Loss)

By incorporating $C_i$ and $\eta_i$, we get the **soft margin** cost function:

$$
\min_{w, b, \eta} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^n \eta_i
$$

subject to:

$$
y_i (w^T x_i + b) \geq 1 - \eta_i
$$

$$
\eta_i \geq 0
$$

This is similar in spirit to **logistic loss**, but here we use **hinge loss**:

$$
\text{Hinge Loss} = \max(0, 1 - y_i (w^T x_i + b))
$$

---

## 📝 Key Takeaways

- The **SVC cost function** aims to maximize the margin by adjusting $w$ and $b$.
- Maximizing the margin is equivalent to minimizing $\frac{1}{2}\|w\|^2$.
- Real-world data is rarely perfectly separable → **soft margin** is needed.
- $C_i$ controls tolerance for misclassified points.
- $\eta_i$ measures margin violations.
- **Soft margin SVC** uses **hinge loss** to balance margin maximization with error minimization.

---

## 📎 Final Objective Function (Soft Margin SVC)

$$
\min_{w, b} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^n \max(0, 1 - y_i (w^T x_i + b))
$$

This formulation allows us to build robust classifiers even in the presence of **noisy** or **overlapping** data.

