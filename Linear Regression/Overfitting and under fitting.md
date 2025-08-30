# Overfitting and Underfitting: Summary Notes

## Key Terminologies
- **Training Data Set**: Used to train the model.
- **Test Data Set**: Used to evaluate model performance on unseen data.
- **Validation Data Set**: Used for hyperparameter tuning.

## Data Splitting
- Typical split: **70% training**, **30% test**.
- Training data may be further split into **train** and **validation** sets.

## Model Scenarios

| Scenario         | Training Accuracy | Test Accuracy | Bias | Variance |
|------------------|------------------|--------------|------|----------|
| Generalized      | High             | High         | Low  | Low      |
| Overfitting      | High             | Low          | Low  | High     |
| Underfitting     | Low              | Low          | High | High     |

## Bias-Variance Tradeoff

- **Bias**: Error from overly simplistic assumptions.
- **Variance**: Error from sensitivity to small fluctuations in training data.

### Summary Table

| Model Type      | Bias | Variance |
|-----------------|------|----------|
| Generalized     | Low  | Low      |
| Overfitting     | Low  | High     |
| Underfitting    | High | High     |

## Regression Example

- **Generalized Model**: Best fit line predicts both training and test data well.
- **Overfitting**: Best fit line fits training data too closely, poor on test data.
- **Underfitting**: Best fit line does not fit training or test data well.

## Evaluation Metrics

- **R Squared ($R^2$)**: Measures proportion of variance explained by the model.
    $$
    R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}
    $$
- **Adjusted R Squared ($\text{Adjusted } R^2$)**: Adjusts $R^2$ for number of predictors.
    $$
    \text{Adjusted } R^2 = 1 - \left( \frac{(1 - R^2)(n - 1)}{n - p - 1} \right)
    $$
    Where $n$ = number of observations, $p$ = number of predictors.

## Key Takeaways

- **Training data**: For model training.
- **Test data**: For unbiased evaluation.
- **Overfitting**: High variance, low bias.
- **Underfitting**: High bias, high variance.
- **Goal**: Achieve a generalized model (low bias, low variance).
