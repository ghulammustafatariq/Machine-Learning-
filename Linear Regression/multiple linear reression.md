# Multiple Linear Regression — Summary Notes

## Key Concepts

- **Simple Linear Regression** uses one input feature to predict an output:
    $$
    h(x) = \theta_0 + \theta_1 x
    $$
    - $\theta_0$: Intercept
    - $\theta_1$: Slope (coefficient)
    - $x$: Input feature

- **Multiple Linear Regression** uses multiple input features:
    $$
    h(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 + \ldots + \theta_n x_n
    $$
    - $\theta_0$: Intercept (always one)
    - $\theta_1, \theta_2, \ldots, \theta_n$: Coefficients for each input feature
    - $x_1, x_2, \ldots, x_n$: Input features

## Example

For house price prediction:
- Input features: Number of rooms ($x_1$), Size ($x_2$), Location ($x_3$)
- Output: Price

Equation:
$$
h(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3
$$

## Optimization

- **Cost Function**: Measures error between predictions and actual values
    $$
    J(\theta)
    $$
- **Gradient Descent**: Iteratively updates all parameters ($\theta_0, \theta_1, \ldots, \theta_n$) to minimize $J(\theta)$

    Gradient descent update rule for each parameter $\theta_j$:
    $$
    \theta_j := \theta_j - \alpha \frac{\partial J(\theta)}{\partial \theta_j}
    $$
    - $\alpha$: Learning rate
    - $\frac{\partial J(\theta)}{\partial \theta_j}$: Partial derivative of cost with respect to $\theta_j$

## Summary Table

| Regression Type         | Input Features | Equation                                      | Parameters         |
|------------------------ |---------------|-----------------------------------------------|--------------------|
| Simple Linear Regression| 1             | $h(x) = \theta_0 + \theta_1 x$               | $\theta_0, \theta_1$ |
| Multiple Linear Regression| $n$         | $h(x) = \theta_0 + \theta_1 x_1 + \ldots + \theta_n x_n$ | $\theta_0, \theta_1, \ldots, \theta_n$ |

## Key Takeaways

- Multiple linear regression generalizes simple linear regression to multiple features.
- The model always has one intercept ($\theta_0$) and as many coefficients as input features.
- Gradient descent optimizes all coefficients together using the update rule above.
- More features mean more coefficients, but only one intercept.
