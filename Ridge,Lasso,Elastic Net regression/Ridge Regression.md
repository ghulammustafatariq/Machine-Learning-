# Ridge Regression: Summary Notes

## What is Ridge Regression?
- **Ridge Regression** is a regularization technique for linear regression that helps reduce overfitting by adding a penalty term to the cost function.
- Also known as **L2 regularization**.

## Why Use Ridge Regression?
- Linear regression can overfit the training data, especially when there are many features or the model is too complex.
- Overfitting leads to high training accuracy but poor test accuracy (low generalization).
- Ridge Regression penalizes large coefficients, reducing model complexity and improving generalization.

## Ridge Regression Cost Function

The standard linear regression cost function (Mean Squared Error, MSE):

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2
$$

Ridge Regression adds a penalty term:

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2 + \lambda \sum_{j=1}^{n} \theta_j^2
$$

- $\lambda$ is the regularization hyperparameter (controls penalty strength).
- $\theta_j$ are the model coefficients (excluding the intercept).

## Effect of $\lambda$ on Coefficients

- $\lambda = 0$: Ridge Regression is equivalent to ordinary linear regression.
- As $\lambda$ increases: Coefficients $\theta_j$ shrink towards zero (but never exactly zero).
- Larger $\lambda$ reduces model complexity and overfitting.

## Ridge Regression in Multiple Linear Regression

For multiple features $x_1, x_2, x_3$:

$$
y = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3
$$

- Ridge Regression shrinks coefficients (e.g., from $0.52, 0.48, 0.24$ to $0.40, 0.38, 0.14$).
- Less important features have smaller coefficients, reducing their impact.

## Key Takeaways

- Ridge Regression reduces overfitting by penalizing large coefficients.
- The penalty term is $\lambda \sum_{j=1}^{n} \theta_j^2$.
- Increasing $\lambda$ decreases coefficient magnitudes.
- Coefficients are shrunk but not set to zero (unlike Lasso Regression).
- Improves model generalization by limiting complexity.

---

*Next: Lasso Regression and comparison with Ridge Regression.*