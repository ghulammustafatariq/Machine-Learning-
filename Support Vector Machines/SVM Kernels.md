# 📌 SVM Kernels

## 🧠 Introduction to Support Vector Machine Kernels

Support Vector Machine (SVM) **kernels** are mathematical functions that transform data into higher-dimensional spaces, making it possible to **linearly separate data** that is not linearly separable in its original form.

Previously, we discussed support vector classifiers and regressors, including concepts like **hinge loss**.  
The primary goal of SVM is to find the **best fit line (or hyperplane)** along with **marginal planes** that efficiently separate data points.

---

## 📈 Linear Support Vector Classifier (Linear SVC)

For **binary classification problems**, we use the Support Vector Classifier (SVC).  
When creating a best fit line and marginal planes in the original feature space, this variant is called **Linear SVC**.  
It essentially creates a straight line (in 2D) or hyperplane (in higher dimensions) to separate data points.

---

## ⚠️ Limitations of Linear SVC

Consider a dataset with two dimensions:

$$
x_1 \quad \text{and} \quad x_2
$$

If the data points are distributed such that they overlap and are **not linearly separable**, then applying a linear SVC to create a best fit line and marginal planes will **not work effectively**.

- Overlapping points make it impossible to separate classes clearly.  
- This results in **low accuracy** and **high error**.

---

## 🧮 Introduction to SVM Kernels

When data points are not linearly separable, we can use **SVM kernels**.  
SVM kernels apply mathematical **transformations** to the dataset, mapping it into a **higher-dimensional space** where the data becomes linearly separable.

---

## 🪄 Transformation from 2D to 3D

Suppose we have data in two dimensions that overlap and are not separable.  
By applying a transformation, we can map these points into three dimensions.  

This transformation creates an additional axis:

$$
Z
$$

turning the 2D data into 3D data.  
In this new space, the points become clearly separable, allowing us to create a **3D hyperplane** and marginal planes to separate the classes effectively.

---

## ✅ Benefits of Transformation

- Enables the use of **Linear SVC** in higher-dimensional space.  
- Improves classification accuracy.  
- Makes the data **linearly separable** through mathematical mapping.

---

## 🧭 Example: Transforming 1D Data to 2D

Consider a dataset in one dimension along the **x-axis** with two categories of data points.  
Applying a linear SVC here can only create one separation line, which may misclassify many points.

To solve this, we apply a transformation by creating a new axis **y** where:

$$
y = x^2
$$

This maps the 1D data into 2D space, making the data points **clearly separable** with a linear boundary.

---

## 🖼️ Visualization of Transformation

- Initially, the data points lie on a line (1D).  
- After applying the transformation:

$$
y = x^2
$$

the points are mapped into a **two-dimensional space** with coordinates:

$$
(x, y)
$$

This allows us to create a **best fit line** and **marginal planes** to separate the categories effectively, improving classification accuracy.

---

## 🧪 Types of SVM Kernels

There are several types of kernels used in SVM to perform these transformations:

1. **Polynomial Kernel**  
2. **Radial Basis Function (RBF) Kernel**  
3. **Sigmoid Kernel**

Each kernel applies a different mathematical formula to map data into higher-dimensional spaces, enabling linear separation.

---

## 🧠 Importance of Kernels

Understanding the **transformation formulas** applied by these kernels is crucial.

For example, the **RBF kernel** can transform 2D data into **three or more dimensions**.  
These kernels are powerful tools in SVM and are frequently discussed in **technical interviews**.

---

## 🏁 Conclusion

SVM kernels enable the transformation of non-linearly separable data into higher-dimensional spaces where linear separation is possible.  
This **significantly enhances** the performance of SVM classifiers.

In upcoming lessons, each kernel type will be explored in detail with practical examples.

---

## 📝 Key Takeaways

- SVM aims to find the **best fit line** and **marginal planes** to separate data points efficiently.  
- **Linear SVC** works well for linearly separable data but fails when data overlaps.  
- **Kernels** apply mathematical transformations to map data into higher dimensions.  
- Common SVM kernels:
  - Polynomial  
  - RBF  
  - Sigmoid
