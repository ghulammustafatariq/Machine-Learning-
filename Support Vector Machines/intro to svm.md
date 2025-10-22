# 📘 Introduction to Support Vector Machine (SVM)

Support Vector Machine (SVM) is a **powerful supervised machine learning algorithm** used for both:
- **Classification** → Support Vector Classifier (SVC)
- **Regression** → Support Vector Regression (SVR)

Before learning SVM, it's recommended to **understand logistic regression**, as SVM builds upon similar geometric ideas.

---

## 🧭 Logistic Regression Recap

- Suppose we have **two features** \( x_1 \) and \( x_2 \).  
- In logistic regression, the goal is to **find a best fit line** that separates two categories (classes) of data points.
- For **three features** \( x_1, x_2, x_3 \), this separating structure becomes a **plane** in 3D space.
- In **\( n \)-dimensional space**, it becomes a **hyperplane**.

A hyperplane can be represented mathematically as:

$$
w^T x + b = 0
$$

where:
- \( w \) = weight vector  
- \( x \) = input vector  
- \( b \) = bias term

A test point is classified based on which **side of the hyperplane** it lies.

---

## 🚀 Support Vector Machine (SVM) — Classifier

- SVM also aims to create a **hyperplane** to separate data into categories.
- But it **does more than just finding any separating hyperplane** — it finds the one that **maximizes the margin**.

### ✨ Key Concept: Marginal Planes

- Along with the best fit line (hyperplane), SVM creates **two parallel marginal planes**.
- These marginal planes pass through the **nearest data points** from each class.
- These nearest points are called **support vectors**.

If the hyperplane is:

$$
w^T x + b = 0
$$

Then the marginal planes are:

$$
w^T x + b = 1 \quad \text{and} \quad w^T x + b = -1
$$

### 📏 Margin Distance

The distance between the two marginal planes is:

$$
D = \frac{2}{\|w\|}
$$

👉 The **goal of SVM** is to **maximize \( D \)** to achieve the best separation between classes.

---

## 🧠 How SVM Chooses the Best Hyperplane

- Suppose we have two different hyperplanes.
- One has a **large margin** \( D \), the other has a **smaller margin** \( D' \).
- Since \( D > D' \), SVM selects the hyperplane with **larger margin**.

This improves:
- Generalization
- Robustness
- Classification accuracy

---

## 📌 Support Vectors

- The data points that **lie exactly on the marginal planes** are called **support vectors**.
- They determine the **orientation and position** of the hyperplane.
- Only these critical points influence the final decision boundary.

---

## 🧭 Extending to Higher Dimensions

- In 3D with \( x_1, x_2, x_3 \), the separating structure is a **plane**, and marginal planes are parallel to it.
- In \( n \)-dimensions, it remains a **hyperplane** with parallel marginal planes maximizing the margin.

---

## 📝 Key Takeaways

- ✅ **SVM** is used for both classification and regression.  
- 🧭 It finds a **hyperplane** that separates data with **maximum margin**.  
- 🧮 Marginal planes are parallel to the hyperplane and pass through **support vectors**.  
- 📈 Maximizing margin improves model performance and generalization.

---

## ⏭️ Coming Next: Soft Margin vs Hard Margin

- **Hard Margin** → Perfect separation of classes (no error allowed).  
- **Soft Margin** → Allows some misclassification to handle noisy data better.

We'll also explore the **mathematics behind optimization** for creating these hyperplanes.

---

## 🧮 Formulas Recap

- **Hyperplane:**
  $$
  w^T x + b = 0
  $$

- **Marginal Planes:**
  $$
  w^T x + b = 1 \quad \text{and} \quad w^T x + b = -1
  $$

- **Margin Distance:**
  $$
  D = \frac{2}{\|w\|}
  $$

- **Prediction Rule:**
  $$
  \text{Sign}(w^T x + b) \rightarrow \text{Class Label}
  $$
