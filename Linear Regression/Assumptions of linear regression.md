# 📒 Assumptions of Linear Regression

Linear Regression works well only if certain **assumptions** are satisfied.  
There are 5 major assumptions:

---

## 🔹 1. Linearity
- There should be a **linear relationship** between input features (X) and the target variable (Y).  
- The relationship can be positive or negative, but it should roughly follow a straight-line pattern.  

**Check:**  
- Scatter plot of X vs Y  

---

## 🔹 2. No Multicollinearity
- Independent variables should **not be highly correlated** with each other.  
- If there is high correlation, regression coefficients (β) become unreliable.  

**Check:**  
- Correlation heatmap  
- VIF (Variance Inflation Factor) → VIF > 5/10 indicates a problem  

**Fix:**  
- Drop correlated features  
- PCA (Dimensionality Reduction)  
- Regularization (Ridge/Lasso)  

---

## 🔹 3. Normality of Residuals
- Residuals (errors) should be **normally distributed** (bell-shaped curve).  
- This ensures correct hypothesis testing and p-value calculation.  

**Check:**  
- Histogram / KDE of residuals  
- Q-Q Plot  

---

## 🔹 4. Homoscedasticity (Constant Variance of Residuals)
- The spread of residuals should be **the same for every predicted value**.  
- If there is less spread for small values and more spread for large values → **Heteroscedasticity** (undesirable).  

**Check:**  
- Residuals vs Predicted values scatter plot  

**Fix:**  
- Log/sqrt transformation  
- Weighted regression  
- Robust models  

---

## 🔹 5. No Autocorrelation of Residuals
- Residuals should be **independent** of each other.  
- This violation is common in **time-series data** (when one error depends on the previous error).  

**Check:**  
- Residual plot → Should show random spread  
- Durbin-Watson test (value ~2 is good)  

**Fix:**  
- Use time-series models (ARIMA, SARIMA)  
- Add lag variables  

---

# 📊 Residual Plots & Their Purpose
- **Actual vs Predicted** → Check Linearity  
- **Histogram/Q-Q Plot of Residuals** → Check Normality  
- **Residuals vs Predicted** → Check Homoscedasticity  
- **Residuals over Time/Index** → Check Autocorrelation  

---

# 📝 Interview Tip
👉 *"What are the assumptions of Linear Regression?"*  

Answer:  
**There are 5 main assumptions: Linearity, No Multicollinearity, Normality of residuals, Homoscedasticity, and No autocorrelation of residuals.**  

Also explain how to check them using plots or statistical tests.
