# 🧠 SVM — Complete Workflow (Training to Prediction)

Support Vector Machine (SVM) is a **supervised machine learning algorithm** used for both **classification** and **regression** tasks.  
It works by finding the **optimal hyperplane** that separates data points of different classes (or fits regression data with margins).

Below is the **step-by-step workflow** of how SVM trains on data and how it predicts new data points.

---

## 🧾 1. Data Preparation

Before training an SVM model, the data must be prepared properly.

**Steps:**
- Gather and clean the dataset.  
- Separate features and labels:  
  - $ X $ → features (input variables)  
  - $ y $ → labels (output variable)  
- Standardize or normalize the data to bring all features to the same scale.

**Example:**  
- Suppose you have data points for classification.  
  - $ X = [x_1, x_2, \dots, x_n] $  
  - $ y = [y_1, y_2, \dots, y_n] $

---

## 🧭 2. Splitting the Dataset

Divide the dataset into:
- **Training set** → Used to train the SVM model.  
- **Testing set** → Used to evaluate the performance on unseen data.

Typical split ratio: **80% training**, **20% testing**.

---

## ⚙️ 3. Selecting the Kernel

Depending on the data’s nature:

- **Linear Kernel** → If data is linearly separable.  
- **Polynomial / RBF / Sigmoid Kernel** → If data is not linearly separable (maps to higher dimensions).

This kernel determines **how the hyperplane is built**.

---

## 🧮 4. Training the Model (Finding the Optimal Hyperplane)

SVM learns by finding a **hyperplane** that best separates the classes with the **maximum margin**.

The objective is to minimize:

$$
\min_{w, b} \ \frac{1}{2} \| w \|^2
$$

Subject to the constraint:

$$
y_i \bigl(w^T x_i + b \bigr) \geq 1
$$

Where:  
- $ w $ = weight vector (defines the direction of the hyperplane)  
- $ b $ = bias term  
- $ x_i $ = training sample  
- $ y_i $ = class label ($+1$ or $-1$)

🔸 If using a **non-linear kernel**, the data is **transformed** into a higher-dimensional space before applying the above optimization.

✅ **Result:** SVM stores the **support vectors**, $ w $, and $ b $ after training.

---

## 📊 5. Model Representation After Training

After training, the decision boundary (hyperplane) is:

$$
f(x) = w^T x + b
$$

For non-linear kernels, it becomes:

$$
f(x) = \sum_{i=1}^{n} \alpha_i y_i K(x_i, x) + b
$$

Where:  
- $ \alpha_i $ = Lagrange multipliers  
- $ K(x_i, x) $ = kernel function  
- $ x_i $ = support vectors  
- $ x $ = new input vector

---

## 🚀 6. Prediction on New Data

When a **new data point** $ x_{\text{new}} $ arrives:

1. SVM applies the **same kernel transformation** (if used during training).  
2. It evaluates the **decision function**:

$$
f(x_{\text{new}}) = \sum_{i=1}^{n} \alpha_i y_i K(x_i, x_{\text{new}}) + b
$$

3. Based on the **sign of** $ f(x_{\text{new}}) $:
   - If $ f(x_{\text{new}}) > 0 $ → Class = $ +1 $  
   - If $ f(x_{\text{new}}) < 0 $ → Class = $ -1 $

✅ SVM **does not retrain** for new data — it only **uses the learned support vectors** to predict efficiently.

---

## 🧪 7. Model Evaluation

To check performance on the test set:
- Accuracy  
- Precision, Recall, F1-score  
- Confusion Matrix  
- For regression: $ R^2 $, MAE, RMSE

---

## 📝 Summary of Workflow

| Step                          | Description                                                   | Output                                 |
|-------------------------------|----------------------------------------------------------------|-----------------------------------------|
| 1. Data Preparation           | Clean, normalize, and split data                               | Features and labels                    |
| 2. Kernel Selection           | Choose linear or non-linear kernel                             | Mapping function                        |
| 3. Model Training             | Find optimal hyperplane using support vectors                  | $ w $, $ b $, support vectors          |
| 4. Model Representation       | Build decision function                                       | $ f(x) $                               |
| 5. Prediction                 | Apply decision function on new data                           | Predicted label                        |
| 6. Evaluation                 | Check performance on test set                                 | Metrics like accuracy, F1-score, etc.  |

---

## 🧠 Intuition Recap

- **SVM learns a hyperplane** during training.  
- It **stores only a few critical data points** (support vectors).  
- During prediction, it **uses support vectors** and **kernel function** to decide the class of new data.  
- It doesn’t memorize the entire dataset, making it efficient.

✅ **Formula for prediction:**

$$
\hat{y} = \mathrm{sign} \left( \sum_{i=1}^{n} \alpha_i y_i K(x_i, x_{\text{new}}) + b \right)
$$

---

## 🏁 Final Takeaway

- SVM **trains** by maximizing the margin between classes.  
- It **stores** support vectors, $ \alpha_i $, and $ b $.  
- It **predicts** by checking on which side of the hyperplane the new point lies.  
- Using **kernels**, SVM can handle both linear and non-linear data effectively.
