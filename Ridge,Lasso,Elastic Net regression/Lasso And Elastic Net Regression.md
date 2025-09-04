# 📘 Notes: Lasso & Elastic Net Regression

## 🔹 Introduction
- **Ridge Regression (L2 Regularization)**: Reduces overfitting by shrinking coefficients, but does **not** perform feature selection.  
- **Lasso Regression (L1 Regularization)**: Used for **feature selection** because it can shrink some coefficients **exactly to zero**.  
- **Elastic Net**: A combination of ridge and lasso, performing both overfitting reduction and feature selection.

---

## 🔹 Lasso Regression

### Cost Function
The cost function for lasso regression is:

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{n} |\theta_j|
$$

- $m$: number of samples  
- $n$: number of features  
- $\lambda$: regularization parameter  
- $|\theta_j|$: absolute value of coefficients  

✅ Unlike ridge, lasso uses **absolute values**, not squares.

---

### Effect of $\lambda$ on Coefficients
- **$\lambda = 0$** → behaves like **Ordinary Least Squares** (no penalty).  
- **As $\lambda$ increases** → coefficients shrink.  
- **At high $\lambda$** → some coefficients become **exactly zero**, removing the feature.  

---

### Example of Feature Selection
Hypothesis function:

$$
h_\theta(x) = \theta_0 + \theta_1x_1 + \theta_2x_2 + \theta_3x_3 + \theta_4x_4
$$

Suppose coefficients are:

$$
\theta_0 = 0.52, \quad
\theta_1 = 0.65, \quad
\theta_2 = 0.72, \quad
\theta_3 = 0.034, \quad
\theta_4 = 0.12
$$

- Since $\theta_4$ is very small, **lasso regression shrinks it to zero** → feature $x_4$ is removed.  
- Other coefficients remain, representing important features.  

---

### Importance
- Lasso is especially useful for **datasets with many features**.  
- Automatically removes irrelevant features → simpler, more interpretable model.  

---

## 🔹 Ridge Regression Recap
- Cost Function:

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{n} \theta_j^2
$$

- Helps reduce **overfitting**.  
- Does **not** shrink coefficients to zero → **no feature selection**.  

---

## 🔹 Elastic Net Regression

### Cost Function
Elastic Net combines both ridge and lasso penalties:

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \big(y_i - h_\theta(x_i)\big)^2 
+ \lambda_1 \sum_{j=1}^{n} \theta_j^2 
+ \lambda_2 \sum_{j=1}^{n} |\theta_j|
$$

- $\lambda_1$: Ridge penalty (L2)  
- $\lambda_2$: Lasso penalty (L1)  

---

### Benefits
- **Ridge part ($\lambda_1$)** → reduces overfitting.  
- **Lasso part ($\lambda_2$)** → performs feature selection.  
- Useful for **high-dimensional datasets** with many features.  

---

## 🔹 Summary Table

| Method        | Regularization Term                   | Effect |
|---------------|---------------------------------------|--------|
| **Ridge (L2)** | $\lambda \sum \theta_j^2$             | Reduces overfitting, no feature selection |
| **Lasso (L1)** | $\lambda \sum |\theta_j|$             | Feature selection by setting coefficients to zero |
| **Elastic Net** | $\lambda_1 \sum \theta_j^2 + \lambda_2 \sum |\theta_j|$ | Both reduce overfitting & feature selection |

---

## 🔑 Key Takeaways
- **Lasso (L1)** → feature selection.  
- **Ridge (L2)** → overfitting reduction.  
- **Elastic Net** → combines both advantages.  
- Choosing the right method depends on whether the problem needs **overfitting control, feature selection, or both**.  
