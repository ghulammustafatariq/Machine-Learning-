# Simple Linear Regression Introduction

Simple linear regression is a foundational supervised machine learning algorithm used for regression problems. The concepts learned here are essential for understanding more advanced techniques, including deep learning and artificial neural networks.

---

## Problem Statement

Simple linear regression is used when we have one independent feature (input) and one dependent feature (output). For example, given a dataset:

| Weight (kg) | Height (cm) |
|-------------|-------------|
| 74          | 170         |
| 80          | 180         |
| 75          | 175.5       |

The goal is to predict the height for a new weight value.

- **Independent Feature:** Weight
- **Dependent Feature:** Height

---

## Why "Simple" Linear Regression?

- **Simple:** Only one input feature and one output feature.
- **Linear:** The relationship between input and output is modeled as a straight line.

If there are multiple input features, the technique is called **multiple linear regression**.

---

## Geometric Interpretation

- Plot the independent feature (weight) on the x-axis and the dependent feature (height) on the y-axis.
- Data points are scattered on the graph.
- Simple linear regression fits a **best fit line** through these points.

---

## Mathematical Equation

The best fit line is represented by the equation:

$$
y = mx + c
$$

Where:
- \( y \): Predicted output (height)
- \( x \): Input feature (weight)
- \( m \): Slope of the line
- \( c \): Intercept

---

## Error Minimization

The best fit line is chosen to minimize the total error, defined as the sum of squared differences between actual and predicted values:

$$
\text{Total Error} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Where:
- \( y_i \): Actual value
- \( \hat{y}_i \): Predicted value from the line

---

## Prediction

Once the best fit line is established, for any new input \( x \) (weight), the predicted output \( y \) (height) is:

$$
\hat{y} = mx + c
$$

---

## Key Takeaways

- Simple linear regression is used for regression problems with one input and one output.
- The algorithm fits a straight line to minimize the total error.
- The best fit line enables prediction of output values for new input data.

---

## Next Steps

- Explore the mathematical derivation of the best fit line.
- Understand error metrics in more detail.
- Implement simple linear regression using Python and relevant libraries.
