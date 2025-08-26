# Cost Function in Simple Linear Regression

## 1. Introduction
- The goal in **simple linear regression** is to find the **best fit line** that minimizes the error between predicted values and actual data points.
- To measure how good a line is, we use a **cost function**.

---

## 2. Cost Function Definition
The cost function (also called **Mean Squared Error, MSE**) is defined as:

$$
J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} \big( h_\theta(x^{(i)}) - y^{(i)} \big)^2
$$

Where:
- $( m )$ = number of data points  
- $( h_\theta(x^{(i)}) )$ = predicted value  
- $( y^{(i)} )$ = true value  
- $( \theta_0 )$ = intercept  
- $( \theta_1 )$ = slope  

The **error term** is:

$$
h_\theta(x^{(i)}) - y^{(i)}
$$

We square it to avoid negatives and sum over all points, then take the average.

---

## 3. Hypothesis (Best Fit Line)
The hypothesis (prediction function) is:

$$
h_\theta(x) = \theta_0 + \theta_1 x
$$

- If we assume \(\theta_0 = 0\) (line passes through the origin):

$$
h_\theta(x) = \theta_1 x
$$

---

## 4. Example Dataset
Consider data points:

- \( x: [1, 2, 3] \)  
- \( y: [1, 2, 3] \)

---

### Case 1: \(\theta_1 = 1\)
Predictions: \([1, 2, 3]\)  
Errors: \([0, 0, 0]\)  
Cost:

$$
J(1) = \frac{1}{6}(0^2 + 0^2 + 0^2) = 0
$$

👉 Perfect fit (global minimum).

---

### Case 2: \(\theta_1 = 0.5\)
Predictions: \([0.5, 1, 1.5]\)  
Errors: \([-0.5, -1, -1.5]\)  
Squared errors: \([0.25, 1, 2.25]\)  
Sum = 3.5  

Cost:

$$
J(0.5) = \frac{1}{6}(3.5) = 0.58
$$

---

### Case 3: \(\theta_1 = 0\)
Predictions: \([0, 0, 0]\)  
Errors: \([-1, -2, -3]\)  
Squared errors: \([1, 4, 9]\)  
Sum = 14  

Cost:

$$
J(0) = \frac{1}{6}(14) = 2.33
$$

---

## 5. Observations
- Plotting \( J(\theta_1) \) vs. \(\theta_1\) gives a **U-shaped curve (convex function)**.
- The minimum point occurs at:

$$
\theta_1 = 1, \quad J(1) = 0
$$

This is the **global minimum**.

---

## 6. Gradient Descent & Convergence
- Randomly picking \(\theta_1\) values is inefficient.  
- Instead, we use **Gradient Descent**, an optimization algorithm.  
- Gradient descent updates parameters step by step until reaching the **global minimum** of the cost function.  

---

## 7. Key Takeaways
- The cost function for linear regression is:

$$
J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} \big( h_\theta(x^{(i)}) - y^{(i)} \big)^2
$$

- Minimizing this function gives the best fit line.
- \(\theta_0\) (intercept) and \(\theta_1\) (slope) are adjusted to reduce error.
- The cost function curve is convex with a unique **global minimum**.
- **Gradient Descent** is used as a convergence algorithm to find this minimum efficiently.
