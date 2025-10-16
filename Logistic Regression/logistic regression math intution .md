# Logistic Regression – In-depth Mathematical Intuition

## 1. Introduction
- **Problem with Linear Regression for Classification:**
  1. Outliers shift the best fit line significantly.
  2. Predictions may fall outside the valid probability range **[0,1]**.
- **Solution:** Apply a **squashing function** (Sigmoid) to keep outputs strictly between 0 and 1.

---

## 2. Linear Regression Base
Best fit line:

$$
f(x) = \theta_0 + \theta_1 x_1
$$

This produces continuous values, not probabilities.  
For classification, we need an **activation function** to squash these outputs.

---

## 3. Sigmoid Activation Function
The **sigmoid function** is defined as:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Properties:
- As $z \to -\infty$, $\sigma(z) \to 0$
- As $z \to +\infty$, $\sigma(z) \to 1$
- At $z = 0$, $\sigma(z) = 0.5$

Thus, sigmoid maps any real number to **(0,1)**.

---

## 4. Applying Sigmoid to Linear Combination
Let

$$
z = \theta_0 + \theta_1 x_1
$$

Then the **hypothesis function** becomes:

$$
h_\theta(x) = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

For multiple features:

$$
z = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 + \dots
$$

Final **logistic regression hypothesis**:

$$
h_\theta(x) = \sigma(z) = \frac{1}{1 + e^{-\left(\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots\right)}}
$$

---

## 5. Cost Function in Linear Regression (Recall)
For comparison:

$$
J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^m \left(h_\theta(x^{(i)}) - y^{(i)}\right)^2
$$

This **squared error cost** is fine for regression, but **non-convex** when applied to logistic regression → multiple local minima.

---

## 6. Logistic Regression Cost Function (Log Loss)

### Case-wise definition:
- If $y=1$:

$$
\text{cost}(h_\theta(x), y) = -\log \left( h_\theta(x) \right)
$$

- If $y=0$:

$$
\text{cost}(h_\theta(x), y) = -\log \left( 1 - h_\theta(x) \right)
$$

### Combined formula:
$$
\text{cost}(h_\theta(x), y) = -y \log(h_\theta(x)) - (1-y)\log(1 - h_\theta(x))
$$

### Overall cost function:
$$
J(\theta_0, \theta_1) = -\frac{1}{m} \sum_{i=1}^m \Big[ y^{(i)} \log(h_\theta(x^{(i)})) + \big(1-y^{(i)}\big)\log\big(1-h_\theta(x^{(i)})\big) \Big]
$$

- This function is **convex** → guarantees gradient descent will find the **global minimum**.

---

## 7. Gradient Descent for Logistic Regression
Update rule:

$$
\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta_0, \theta_1)
$$

- $\alpha$ = learning rate  
- $j = 0,1,\dots,n$ (for all features)  
- Continue iterating until **convergence** (minimum cost function).

---

## 8. Workflow of Logistic Regression

1. **Linear Combination (Linear Regression Step)**  
   Compute weighted sum of features:  
   $$
   z = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots
   $$

2. **Apply Sigmoid Function (Squashing Step)**  
   Convert $z$ into probability:  
   $$
   h_\theta(x) = \sigma(z) = \frac{1}{1 + e^{-z}}
   $$

3. **Thresholding (Decision Step)**  
   Compare probability with threshold (default = 0.5):  
   $$
   \hat{y} =
   \begin{cases}
   1 & \text{if } h_\theta(x) \geq 0.5 \\
   0 & \text{if } h_\theta(x) < 0.5
   \end{cases}
   $$

4. **Compute Loss (Error Measurement)**  
   Use log loss for each prediction:  
   $$
   \text{cost}(h_\theta(x), y) = -y \log(h_\theta(x)) - (1-y)\log(1 - h_\theta(x))
   $$

5. **Optimize Parameters (Learning Step)**  
   Use **gradient descent** to minimize cost function and update $\theta_j$.

6. **Final Prediction**  
   After training, model predicts probability → threshold → final class label.

---

## 9. Summary
- Logistic regression applies the **sigmoid function** to squash linear regression outputs into **[0,1]**.
- Uses **log loss cost function**, which is convex.
- Gradient descent efficiently minimizes the cost to find optimal parameters.
- The **workflow** is:
  - Linear combination → Sigmoid → Threshold → Log Loss → Gradient Descent → Prediction.

---

## 10. Key Takeaways
- **Why sigmoid?** Ensures outputs are valid probabilities.  
- **Why log loss?** Ensures convexity → efficient optimization.  
- **Why gradient descent?** Iteratively updates parameters until convergence.  
- Logistic regression is a **classification algorithm**, despite its name.

---
