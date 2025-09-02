# Polynomial Regression Intuition

## Overview
Polynomial regression is a machine learning algorithm that extends linear regression to model nonlinear relationships between independent and dependent variables by including polynomial terms.

## Key Concepts

- **Simple Linear Regression Equation:**
    $$
    h_\theta(x) = \beta_0 + \beta_1 x
    $$
    - Fits a straight line to data.

- **Polynomial Regression Equation (Degree $n$):**
    $$
    h_\theta(x) = \beta_0 + \beta_1 x + \beta_2 x^2 + \cdots + \beta_n x^n = \sum_{i=0}^{n} \beta_i x^i
    $$
    - Fits a curve to data, capturing nonlinear relationships.

- **Degree Zero (Constant Model):**
    $$
    h_\theta(x) = \beta_0
    $$

- **Degree One (Linear Model):**
    $$
    h_\theta(x) = \beta_0 + \beta_1 x
    $$

- **Degree Two (Quadratic Model):**
    $$
    h_\theta(x) = \beta_0 + \beta_1 x + \beta_2 x^2
    $$

- **Multiple Features (Degree Two Example):**
    $$
    h_\theta(x) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1^2 + \beta_4 x_2^2
    $$

- **Multiple Features (Degree Three Example):**
    $$
    h_\theta(x) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1^2 + \beta_4 x_2^2 + \beta_5 x_1^3 + \beta_6 x_2^3
    $$

## Model Complexity

- Increasing the polynomial degree allows the model to fit the data more closely.
- **High degree** $\rightarrow$ risk of overfitting (model fits noise).
- **Low degree** $\rightarrow$ risk of underfitting (model misses patterns).
- Select degree to balance bias and variance.

## Summary

- Polynomial regression models nonlinear relationships by adding polynomial terms.
- The degree of the polynomial controls model flexibility.
- Can be extended to multiple features by including polynomial terms for each.
- Proper degree selection is crucial for generalization.
