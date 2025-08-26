# 📘 Convergence Algorithm & Gradient Descent (Linear Regression)

## 🔹 Objective
- Minimize the **Cost Function** $J(\theta)$.  
- Reach the **global minima** → corresponds to the **best fit line**.  

---

## 🔹 Gradient Descent Update Rule
General update equation:

$$
\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)
$$

Where:
- $\theta_j$ = parameter (slope/intercept)  
- $\alpha$ = learning rate  
- $J(\theta)$ = cost function  

---

## 🔹 Cost Function
For **Simple Linear Regression**:

$$
J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2
$$

Where:
- $m$ = number of training examples  
- $h_\theta(x) = \theta_0 + \theta_1 x$ (hypothesis)  
- $y^{(i)}$ = actual value  

---

## 🔹 Derivatives of Cost Function
We need partial derivatives w.r.t. each parameter:

1. For $\theta_0$:
$$
\frac{\partial}{\partial \theta_0} J(\theta_0, \theta_1) = \frac{1}{m} \sum_{i=1}^{m} \Big( h_\theta(x^{(i)}) - y^{(i)} \Big)
$$

2. For $\theta_1$:
$$
\frac{\partial}{\partial \theta_1} J(\theta_0, \theta_1) = \frac{1}{m} \sum_{i=1}^{m} \Big( h_\theta(x^{(i)}) - y^{(i)} \Big) x^{(i)}
$$

---

## 🔹 Parameter Update Rules
Using derivatives, the parameters are updated iteratively:

1. Update $\theta_0$:
$$
\theta_0 := \theta_0 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} \Big( h_\theta(x^{(i)}) - y^{(i)} \Big)
$$

2. Update $\theta_1$:
$$
\theta_1 := \theta_1 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} \Big( h_\theta(x^{(i)}) - y^{(i)} \Big) x^{(i)}
$$

---

## 🔹 Intuition Behind Gradient Descent
- If slope **positive** → decrease parameter.  
- If slope **negative** → increase parameter.  
- Repeat **until convergence** (i.e., cost function stops decreasing).  

---

## 🔹 Learning Rate ($\alpha$)
- Controls step size in each iteration.  
- **Too small** → very slow convergence.  
- **Too large** → overshooting, may never converge.  
- Typical values: $0.001$, $0.01$ (experimentally chosen).  

---

## 🔹 Key Takeaways
- Gradient descent = iterative optimization to minimize $J(\theta)$.  
- Both $\theta_0$ and $\theta_1$ updated simultaneously.  
- Proper choice of $\alpha$ ensures smooth convergence.  
- Final result = parameters giving the **best fit line**.  
