# Linear Regression with Ordinary Least Squares (OLS) — Summary Notes

## What is OLS?
Ordinary Least Squares (OLS) is a method to find the best-fit line for a set of data points in linear regression by minimizing the sum of squared errors between predicted and actual values.

## Simple Linear Regression Equation
The best-fit line is:
$$
\hat{y}_i = \beta_0 + \beta_1 x_i
$$
where:
- $\hat{y}_i$ = predicted value
- $x_i$ = input feature
- $\beta_0$ = intercept
- $\beta_1$ = coefficient (slope)

## Error to Minimize
OLS minimizes the Mean Squared Error (MSE):
$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \frac{1}{n} \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2
$$

## OLS Formulas

### Coefficient ($\beta_1$)
$$
\beta_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

### Intercept ($\beta_0$)
$$
\beta_0 = \bar{y} - \beta_1 \bar{x}
$$
where:
- $\bar{x}$ = mean of $x$
- $\bar{y}$ = mean of $y$

## Steps to Compute OLS
1. Calculate means: $\bar{x}$ and $\bar{y}$
2. Compute $\beta_1$ using the formula above
3. Compute $\beta_0$ using the formula above

## Key Points
- OLS provides a closed-form solution (no iterative optimization).
- The formulas use averages and summations of the data.
- OLS minimizes squared error, just like MSE.
- For multiple linear regression, formulas are extended but follow similar principles.
