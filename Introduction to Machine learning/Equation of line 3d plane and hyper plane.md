# Equation of Line, 3D Plane, and Hyperplane

In this topic, we discuss the equation of a straight line and extend the concept to 3D planes and hyperplanes. This foundation is important for understanding machine learning algorithms such as **Logistic Regression** and **Support Vector Machines**.

---

## 1. Equation of a Line in 2D

A straight line in 2D (x, y plane) can be written in multiple equivalent forms:

1. **Slope-Intercept Form**:

$$
y = mx + c
$$

- $m$: slope (change in y per unit change in x)  
- $c$: intercept (where the line crosses the y-axis)

2. **Regression Notation**:

$$
y = \beta_0 + \beta_1 x
$$

3. **General Form**:

$$
ax + by + c = 0
$$

- Rearranging:  
  $$
  y = -\frac{a}{b}x - \frac{c}{b}
  $$
- Here slope $m = -\frac{a}{b}$, intercept $c = -\frac{c}{b}$.

---

## 2. Vector Form in 2D

In 2D with variables $x_1, x_2$:

$$
W_1 x_1 + W_2 x_2 + b = 0
$$

In vector notation:

$$
w^T x + b = 0
$$

Where:  
- $w = [W_1, W_2]^T$  
- $x = [x_1, x_2]^T$

---

## 3. Equation of a Plane in 3D

For 3D space with $x_1, x_2, x_3$:

$$
W_1 x_1 + W_2 x_2 + W_3 x_3 + b = 0
$$

Or in vector form:

$$
w^T x + b = 0
$$

Where:  
- $w = [W_1, W_2, W_3]^T$  
- $x = [x_1, x_2, x_3]^T$

---

## 4. Hyperplane in n-Dimensions

In $n$-dimensions, the equation generalizes to:

$$
\sum_{i=1}^n W_i x_i + b = 0
$$

Or vectorially:

$$
w^T x + b = 0
$$

- If the hyperplane passes through the origin ($b = 0$):

$$
w^T x = 0
$$

---

## 5. Geometric Interpretation

From linear algebra, the dot product:

$$
w^T x = \|w\| \|x\| \cos\theta
$$

If:

$$
w^T x = 0
$$

Then:

$$
\cos\theta = 0 \quad \Rightarrow \quad \theta = 90^\circ
$$

Thus, **$w$ is perpendicular (normal) to the line/plane/hyperplane**.

---

## 6. Key Points

- Line equations in 2D: $y = mx + c$, $y = \beta_0 + \beta_1 x$, or $ax + by + c = 0$.  
- In higher dimensions: $w^T x + b = 0$.  
- Vector $w$ is always normal (perpendicular) to the plane/hyperplane.  
- Intercept $b$ shifts the plane away from the origin.  
- This concept is fundamental in ML algorithms (Logistic Regression, SVM).  

---
