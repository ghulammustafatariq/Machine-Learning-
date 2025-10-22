# 📊 Support Vector Regression (SVR)

## 📌 Introduction to Support Vector Regression

Support Vector Regression (SVR) is the **regression counterpart of Support Vector Machines (SVM)**.  
Previously we explored the Support Vector Classifier (SVC), its cost function, constraints, and hinge loss that involve hyperparameters such as $C$ and $\epsilon$.  
The goal of SVR is to **minimize the cost function** by adjusting the parameters $w$ and $b$.

---

## 🧮 Regression Problem Statement

For regression we want a **best fit line** and two **margin planes** such that the distance between those planes is maximized while keeping most points inside the margin.

Example:
- $x$ = size of a house  
- $y$ = price of a house

The task: predict $y$ (price) from $x$ (size). Because $y$ is continuous, this is a regression problem.

---

## ⚙️ Cost Function (Flatness) — Basic Idea

To keep the solution “flat” we minimize the norm of the weight vector. The flatness term (same as in SVC) is:

$$
\frac{1}{2}\|w\|^2
$$

This term penalizes large weights and encourages a smoother/less complex function.

---

## 📐 Best Fit Line and Margin Planes in SVR

The predicted value (regression function) is:

$$
f(x) = w^T x + b
$$

We define two parallel margin planes that form an $\epsilon$-insensitive tube around $f(x)$:

$$
w^T x + b + \epsilon
\qquad\text{and}\qquad
w^T x + b - \epsilon
$$

Here $ \epsilon $ is the **margin error** (the half-width of the tube). Points inside this tube incur no loss.

---

## 🧭 Constraint for Points Inside the Tube

A point $(x_i, y_i)$ is considered well-predicted if it lies within the $\epsilon$-tube:

$$
|y_i - (w^T x_i + b)| \le \epsilon .
$$

If this holds, the prediction error for that point is ignored (zero loss).

---

## 🪜 Handling Points Outside the Tube — Slack Variables

For points outside the tube we introduce nonnegative slack (deviation) variables $\xi_i$ and $\xi_i^*$ (commonly used in SVR formulation) to measure how far a point lies outside the $\epsilon$-tube:

- $\xi_i \ge 0$ measures deviation when $y_i$ is above the tube.  
- $\xi_i^* \ge 0$ measures deviation when $y_i$ is below the tube.

The constraints become:

$$
\begin{aligned}
y_i - (w^T x_i + b) &\le \epsilon + \xi_i,\\
(w^T x_i + b) - y_i &\le \epsilon + \xi_i^*,
\end{aligned}
\qquad \xi_i,\,\xi_i^* \ge 0 .
$$

Equivalently:

$$
|y_i - (w^T x_i + b)| \le \epsilon + \eta_i
$$

where $\eta_i$ denotes the total deviation (one can set $\eta_i = \xi_i + \xi_i^*$ if you prefer a single deviation variable).

---

## 📝 Soft Margin SVR Objective (Primal Form)

Balancing flatness and deviations gives the standard primal objective:

$$
\min_{w,b,\xi,\xi^*}\;
\frac{1}{2}\|w\|^2 \;+\; C\sum_{i=1}^n (\xi_i + \xi_i^*)
$$

subject to, for each $i$,

$$
\begin{aligned}
y_i - (w^T x_i + b) &\le \epsilon + \xi_i,\\
(w^T x_i + b) - y_i &\le \epsilon + \xi_i^*,\\
\xi_i,\,\xi_i^* &\ge 0.
\end{aligned}
$$

- $C$ controls the trade-off between model flatness ($\|w\|^2$) and the tolerated deviations outside the $\epsilon$-tube.  
- Large $C$ → penalize deviations heavily (fit closely).  
- Small $C$ → allow more deviations (smoother function).

---

## 🔍 Loss View: $\epsilon$-Insensitive (Hinge-like) Loss

SVR uses the $\epsilon$-insensitive loss (a hinge-like loss):

$$
L_{\epsilon}(y, f(x)) = \max\{0,\; |y-f(x)| - \epsilon\}.
$$

The primal objective above is equivalent to minimizing:

$$
\frac{1}{2}\|w\|^2 + C\sum_{i=1}^n L_{\epsilon}(y_i, w^T x_i + b).
$$

---

## 🧠 Interpretation of Hyperparameters

- $\epsilon$: width of the tube — errors smaller than $\epsilon$ are ignored. Larger $\epsilon$ → more points inside tube → sparser support set.  
- $C$: penalty weight — controls how much we penalize deviations beyond $\epsilon$. Larger $C$ → stricter fitting, smaller $C$ → smoother model.

---

## 🏁 Summary & Key Takeaways

- SVR fits a function $f(x)=w^T x + b$ with an $\epsilon$-insensitive tube: predictions within $\epsilon$ are not penalized.  
- Slack variables $\xi_i,\xi_i^*$ handle deviations outside the tube.  
- Objective: minimize $\tfrac{1}{2}\|w\|^2 + C\sum(\xi_i+\xi_i^*)$ subject to tube constraints.  
- Tune $\epsilon$ and $C$ to balance bias–variance and to control sparsity (number of support vectors).

---

## ✨ Final Equations (Compact)

Prediction:
$$
f(x) = w^T x + b
$$

Primal objective:
$$
\min_{w,b,\xi,\xi^*}\; \frac{1}{2}\|w\|^2 + C\sum_{i=1}^n (\xi_i + \xi_i^*)
$$

Constraints:
$$
\begin{aligned}
y_i - f(x_i) &\le \epsilon + \xi_i,\\
f(x_i) - y_i &\le \epsilon + \xi_i^*,\\
\xi_i,\,\xi_i^* &\ge 0.
\end{aligned}
$$

Loss per point:
$$
L_{\epsilon}(y_i,f(x_i)) = \max(0,\,|y_i-f(x_i)|-\epsilon).
$$
