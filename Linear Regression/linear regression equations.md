# Simple Linear Regression: Summary Notes

## Key Concepts

- **Simple Linear Regression** models the relationship between one independent variable ($x$) and one dependent variable ($y$) by fitting a straight line to the data.
- The goal is to find the **best fit line** that minimizes prediction errors.

## Equation of the Best Fit Line

- The general form of the regression line:
    $$
    y = mx + c
    $$
- In machine learning notation (Andrew Ng's style):
    $$
    h_\theta(x) = \theta_0 + \theta_1 x
    $$
    - $x$: Independent variable (e.g., weight)
    - $h_\theta(x)$: Predicted value (e.g., height)
    - $\theta_0$: Intercept (value of $y$ when $x = 0$)
    - $\theta_1$: Slope or coefficient (change in $y$ for a unit change in $x$)

- For multiple features:
    $$
    h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_n x_n
    $$

## Prediction

- For a new $x$ value, predict $y$ using:
    $$
    \hat{y} = h_\theta(x)
    $$

## Error Calculation

- The error for a data point:
    $$
    \text{error} = y - \hat{y}
    $$
- The objective is to minimize the **sum of errors** (often squared errors) across all data points.

## Optimization

- Adjust $\theta_0$ and $\theta_1$ iteratively to minimize the total error.
- This process finds the optimal parameters for the best fit line.

## Summary Table

| Term         | Meaning                                              |
|--------------|-----------------------------------------------------|
| $\theta_0$   | Intercept (value of $y$ when $x = 0$)               |
| $\theta_1$   | Slope (change in $y$ per unit change in $x$)        |
| $h_\theta(x)$| Predicted value for input $x$                       |
| $\hat{y}$    | Another notation for predicted value                 |
| Error        | $y - \hat{y}$ (difference between actual and predicted) |

## Takeaways

- Simple linear regression fits a line to model $y$ as a function of $x$.
- The best fit line is found by minimizing prediction errors.
- Optimization techniques (like gradient descent) are used to efficiently find $\theta_0$ and $\theta_1$.
