# Distance of a Point from a Plane

## Introduction
Understanding how to calculate the distance from a point to a plane is a key concept in linear algebra, especially relevant for machine learning algorithms like logistic regression and Support Vector Machines (SVM).

## Plane Equation
A plane passing through the origin can be represented as:
$$
w^T x = 0
$$
where:
- $w$ is a vector perpendicular (normal) to the plane,
- $x$ is any point on the plane.

## Distance Formula
Given a point $s = (x_1, x_2, ..., x_n)$ in $n$-dimensional space, the distance $d$ from $s$ to the plane $\pi$ is:
$$
d = \frac{w^T s}{\|w\|}
$$
where:
- $w^T s$ is the dot product of $w$ and $s$,
- $\|w\|$ is the magnitude (Euclidean norm) of $w$.

## Geometric Interpretation
- $w^T s = \|w\| \|s\| \cos\theta$, where $\theta$ is the angle between $w$ and $s$.
- If $\theta < 90^\circ$, $d$ is positive (point is above the plane in the direction of $w$).
- If $\theta > 90^\circ$, $d$ is negative (point is below the plane, opposite to $w$).

## Example: Point Below the Plane
For a point $s'$ below the plane:
$$
d' = \frac{w^T s'}{\|w\|}
$$
$d'$ will be negative, indicating $s'$ is on the opposite side of the plane relative to $w$.

## Key Takeaways
- The distance from a point to a plane is given by $\frac{w^T s}{\|w\|}$.
- $w$ defines the orientation of the plane.
- Positive distance: point is above the plane (in the direction of $w$).
- Negative distance: point is below the plane (opposite to $w$).
- This concept is fundamental in classification algorithms like logistic regression and SVM.
