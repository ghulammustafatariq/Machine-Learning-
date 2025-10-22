# 🧭 SVM — Mathematical Intuition

In this section, we will understand **Support Vector Machines (SVM)** with a strong **mathematical foundation**.

Previously, we saw that the main aim is to create **the best fit line (or hyperplane)** along with **marginal planes** to maximize the separation between classes.

---

## 🪜 Step 1: Equation of the Hyperplane

Let's consider two coordinates $x$ and $y$ in a 2D plane.  
We want to create the best fit line with respect to this plane.

The general equation of the separating hyperplane is:

$$
w^T x + b = 0
$$

Where:

- $w$ = weight vector (normal to the hyperplane)  
- $b$ = bias term (intercept)

If the line passes through the origin, then $b = 0$,  
so the equation simplifies to:

$$
w^T x = 0
$$

The vector $w$ is **perpendicular** (normal) to the hyperplane.

---

## 📏 Step 2: Distance of a Point from the Hyperplane

Suppose we have a point $p = (-4, 0)$.  
We denote its perpendicular distance to the hyperplane as $d'$.

- If a point lies **below** the hyperplane → distance is **negative**.  
- If it lies **above** the hyperplane → distance is **positive**.

This is determined by the **angle between** the vectors $w$ and the point vector.

- Angle $> 90^\circ$ → negative distance  
- Angle $0^\circ \leq \theta \leq 90^\circ$ → positive distance

---

## 🧮 Step 3: Marginal Planes

The **main hyperplane** is defined as:

$$
w^T x + b = 0
$$

We create two **marginal planes** parallel to this hyperplane:

$$
w^T x + b = +1
$$

and

$$
w^T x + b = -1
$$

The points lying on these marginal planes are called **support vectors**.

---

## 📐 Step 4: Distance Between Marginal Planes

Let $x_1$ be a point on the plane:

$$
w^T x_1 + b = +1
$$

and $x_2$ be a point on the plane:

$$
w^T x_2 + b = -1
$$

Subtracting the two equations:

$$
w^T x_1 + b - (w^T x_2 + b) = 1 - (-1)
$$

$$
w^T (x_1 - x_2) = 2
$$

The unit vector of $w$ is:

$$
\frac{w}{\|w\|}
$$

Dividing both sides by $\|w\|$ gives the distance between the marginal planes:

$$
\text{Margin Distance} = \frac{2}{\|w\|}
$$

This distance is the **margin**, which we want to **maximize** by adjusting $w$ and $b$.

---

## 🧭 Step 5: Classification Constraints

For correct classification:

- If $y_i = +1$ then:
  $$
  w^T x_i + b \geq +1
  $$

- If $y_i = -1$ then:
  $$
  w^T x_i + b \leq -1
  $$

Combining both:

$$
y_i (w^T x_i + b) \geq 1
$$

This ensures all points are on the correct side of the margin.

---

## 🎯 Step 6: Optimization Objective

We want to maximize the margin:

$$
\frac{2}{\|w\|}
$$

This is equivalent to minimizing:

$$
\frac{1}{2} \|w\|^2
$$

subject to the constraint:

$$
y_i (w^T x_i + b) \geq 1
$$

for all training points $i = 1, 2, \dots, n$.

---

## 📝 Key Takeaways

- The equation of the decision boundary is:
  $$
  w^T x + b = 0
  $$

- Points **below** the hyperplane have negative distance.  
  Points **above** the hyperplane have positive distance.

- Marginal planes:
  $$
  w^T x + b = +1
  $$
  $$
  w^T x + b = -1
  $$

- The **margin** between marginal planes:
  $$
  \text{Margin} = \frac{2}{\|w\|}
  $$

- Classification constraint:
  $$
  y_i (w^T x_i + b) \geq 1
  $$

- Objective function (for hard margin SVM):
  $$
  \min_{w,b} \frac{1}{2} \|w\|^2
  $$
  subject to
  $$
  y_i (w^T x_i + b) \geq 1
  $$

---
