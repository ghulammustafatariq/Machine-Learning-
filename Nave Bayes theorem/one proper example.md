# Naive Bayes — Worked Example (step-by-step)

**Goal:** Given a new day with features  
**Outlook = Sunny**, **Temperature = Hot**, **Humidity = High**, **Wind = Weak**,  
use **Naive Bayes** to predict whether **Play = Yes** or **No**.

We use the classic **Play Tennis** dataset with 14 examples.

---

## 1. Dataset (14 rows)

| # | Outlook  | Temperature | Humidity | Wind   | Play |
|---:|:--------:|:-----------:|:--------:|:------:|:----:|
| 1 | Sunny    | Hot         | High     | Weak   | No   |
| 2 | Sunny    | Hot         | High     | Strong | No   |
| 3 | Overcast | Hot         | High     | Weak   | Yes  |
| 4 | Rain     | Mild        | High     | Weak   | Yes  |
| 5 | Rain     | Cool        | Normal   | Weak   | Yes  |
| 6 | Rain     | Cool        | Normal   | Strong | No   |
| 7 | Overcast | Cool        | Normal   | Strong | Yes  |
| 8 | Sunny    | Mild        | High     | Weak   | No   |
| 9 | Sunny    | Cool        | Normal   | Weak   | Yes  |
|10 | Rain     | Mild        | Normal   | Weak   | Yes  |
|11 | Sunny    | Mild        | Normal   | Strong | Yes  |
|12 | Overcast | Mild        | High     | Strong | Yes  |
|13 | Overcast | Hot         | Normal   | Weak   | Yes  |
|14 | Rain     | Mild        | High     | Strong | No   |

Total examples = **14**  
Counts:  
- \(N_{Yes} = 9\)  
- \(N_{No} = 5\)

---

## 2. Step 1 — Compute Priors

Prior probabilities (class priors):

$$
P(\text{Yes}) = \frac{N_{Yes}}{N} = \frac{9}{14} \approx 0.6429
$$

$$
P(\text{No}) = \frac{N_{No}}{N} = \frac{5}{14} \approx 0.3571
$$

---

## 3. Step 2 — Compute Likelihoods (feature probabilities given class)

We need $(P(\text{feature} \mid \text{class}))$ for each feature value in our query:  
Query = (Sunny, Hot, High, Weak)

From the dataset counts:

### For class = **Yes** (9 examples)

- $(P(\text{Outlook=Sunny} \mid \text{Yes}) = \dfrac{2}{9})$  
  (2 of 9 Yes examples have Outlook = Sunny)

- $(P(\text{Temperature=Hot} \mid \text{Yes}) = \dfrac{2}{9})$

- $(P(\text{Humidity=High} \mid \text{Yes}) = \dfrac{3}{9})$

- $(P(\text{Wind=Weak} \mid \text{Yes}) = \dfrac{6}{9})$

### For class = **No** (5 examples)

- $(P(\text{Outlook=Sunny} \mid \text{No}) = \dfrac{3}{5})$

- $(P(\text{Temperature=Hot} \mid \text{No}) = \dfrac{2}{5})$

- $(P(\text{Humidity=High} \mid \text{No}) = \dfrac{4}{5})$

- $(P(\text{Wind=Weak} \mid \text{No}) = \dfrac{2}{5})$

---

## 4. Step 3 — Compute Unnormalized Posterior (product of prior × likelihoods)

Using **Naive Bayes** (features assumed independent given class):

### For **Yes**

$$
\begin{aligned}
P(\text{Yes} \mid & \ \text{Sunny, Hot, High, Weak}) \\
& \propto P(\text{Yes}) \times P(\text{Sunny}\mid\text{Yes}) \times P(\text{Hot}\mid\text{Yes}) \\
& \quad\quad \times P(\text{High}\mid\text{Yes}) \times P(\text{Weak}\mid\text{Yes}) \\[6pt]
&= \frac{9}{14} \times \frac{2}{9} \times \frac{2}{9} \times \frac{3}{9} \times \frac{6}{9}
\end{aligned}
$$

Compute decimal:

$$
P_{Yes}^{\text{unnorm}} \approx 0.642857 \times 0.222222 \times 0.222222 \times 0.333333 \times 0.666667
\approx 0.0070547
$$

---

### For **No**

$$
\begin{aligned}
P(\text{No} \mid & \ \text{Sunny, Hot, High, Weak}) \\
& \propto P(\text{No}) \times P(\text{Sunny}\mid\text{No}) \times P(\text{Hot}\mid\text{No}) \\
& \quad\quad \times P(\text{High}\mid\text{No}) \times P(\text{Weak}\mid\text{No}) \\[6pt]
&= \frac{5}{14} \times \frac{3}{5} \times \frac{2}{5} \times \frac{4}{5} \times \frac{2}{5}
\end{aligned}
$$

Compute decimal:

$$
P_{No}^{\text{unnorm}} \approx 0.357143 \times 0.6 \times 0.4 \times 0.8 \times 0.4
\approx 0.0274286
$$

---

## 5. Step 4 — Normalize to get posterior probabilities

Compute normalization constant:

$$
Z = P_{Yes}^{\text{unnorm}} + P_{No}^{\text{unnorm}} \approx 0.0070547 + 0.0274286 \approx 0.0344833
$$

Posterior probabilities:

$$
P(\text{Yes} \mid \text{features}) = \frac{0.0070547}{0.0344833} \approx 0.2045 \; (20.45\%)
$$

$$
P(\text{No} \mid \text{features}) = \frac{0.0274286}{0.0344833} \approx 0.7955 \; (79.55\%)
$$

**Prediction:** **No** (since \(P(\text{No}\mid\text{features})\) is larger)

---

## 6. Optional — Laplace (add-one) smoothing

Laplace smoothing prevents zero probabilities and is often used when some feature value/class combinations are unseen.

With smoothing parameter \(\alpha=1\), and letting \(K_f\) be number of distinct values of feature \(f\), we compute for each conditional probability:

$$
P_{\text{smoothed}}(x_i \mid y) = \frac{N(x_i,y) + \alpha}{N(y) + \alpha K_f}
$$

Applying smoothing for our features (Outlook has 3 values, Temperature 3, Humidity 2, Wind 2):

After applying Laplace (\(\alpha=1\)) the unnormalized posteriors become (calculated):

- \(P_{Yes}^{\text{unnorm, smooth}} \approx 0.0092975\)  
- \(P_{No}^{\text{unnorm, smooth}}  \approx 0.0204993\)

Normalized:

$$
P(\text{Yes}\mid\text{features}) \approx 0.3120 \; (31.20\%)
$$

$$
P(\text{No}\mid\text{features}) \approx 0.6880 \; (68.80\%)
$$

**Prediction with smoothing:** still **No**.

---

## 7. Final Answer & Interpretation

- **Without smoothing:** \(P(\text{Yes}\mid \text{Sunny,Hot,High,Weak})\approx 20.45\%\), \(P(\text{No}\mid \ldots)\approx 79.55\%\) → **Predict: No**.  
- **With Laplace smoothing (α=1):** \(P(\text{Yes})\approx 31.20\%\), \(P(\text{No})\approx 68.80\%\) → **Predict: No**.

**Takeaway:** Naive Bayes multiplies the prior by the likelihoods of each feature given the class, then normalizes. The naive independence assumption simplifies joint likelihoods to a product of conditional probabilities. Smoothing is recommended when your training set is small or when some combinations do not appear.

---

## 8. Short checklist to solve any similar example

1. Write down the dataset and count \(N\), \(N_{class}\).  
2. Compute priors \(P(class)=N_{class}/N\).  
3. For each feature value in the query compute \(P(feature=value \mid class)\).  
4. Multiply prior × all likelihoods to get unnormalized posterior for each class.  
5. Normalize across classes (divide by sum) to get final probabilities.  
6. Optionally use Laplace smoothing if some conditional counts are zero or dataset is small.

---

If you want, I can also:
- convert this to a **LaTeX PDF**,  
- provide the **Python code** to compute these numbers, or  
- give a **second example** with numeric (continuous) features using Gaussian Naive Bayes.

Which one next? 😊
