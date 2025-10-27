# Optimization of KNN: K-d Tree and Ball Tree (In-depth Intuition)

## 1. Introduction
In standard **K-Nearest Neighbor (KNN)**, to classify or predict a new point, we compute the distance between the query point and **every** point in the dataset.

This leads to a time complexity of:
$$
O(n)
$$
for each query, which becomes slow when **n is large**.

To optimize this, we use:

- **K-d Tree**
- **Ball Tree**

Both methods **reduce the number of distance computations** by organizing data in hierarchical structures.

---

## 2. K-d Tree (K-dimensional Tree)

### Purpose
Efficiently partition the feature space so that nearest neighbor search does **not require checking all points**.

### Dataset Example (Points in 2D)
(7, 2)
(5, 4)
(9, 6)
(8, 1)
(2, 3)
(4, 7)


### Construction Steps
1. **Choose a feature to split on**  
   - First split on feature \( f_1 \) (x-axis).
2. **Sort values of \( f_1 \)** and find median:  
   Sorted \( f_1 \) values → 2, 4, 5, 7, 8, 9  
   Median ≈ 7 → first split at:
   $$
   f_1 = 7
   $$
3. Points are divided into two regions:
   - Left: points where \( f_1 < 7 \)
   - Right: points where \( f_1 ≥ 7 \)

4. **Next split uses the other feature** \( f_2 \) (y-axis) inside each region.
   Example left region points: (2,3), (4,7), (5,4)  
   Sort by \( f_2 \): 3, 4, 7 → median is 4  
   Split at:
   $$
   f_2 = 4
   $$

5. Alternate splitting between \( f_1 \) and \( f_2 \) recursively.

### Visual Insight
- First split: **Vertical line** at \( f_1 = 7 \)
- Second split: **Horizontal line** at \( f_2 = 4 \)
- Third split: Vertical again, and so on...

This process creates a **binary tree**.

---

## 3. Searching in a K-d Tree

Given a query point (e.g., (5, 7)):

1. Traverse tree based on split rules.
   - If \( 5 < 7 \) → go **left**.
   - If \( 7 > 4 \) → go **upper region**.
2. Reach a **leaf node**.
3. Check distances of those leaf points.
4. **Backtrack if necessary** to ensure no closer point exists in another branch.

### Note:
K-d Tree may require **backtracking**.

---

## 4. Ball Tree

### Motivation
K-d tree works well only when:
- Dimensionality is small
- Data splits cleanly along axes

When data is high-dimensional, K-d tree becomes less efficient.  
Ball Tree solves this.

---

### Construction of Ball Tree
1. **Group closest points together** into clusters (called **balls**).
2. Each group is represented by:
   - A **center point**
   - A **radius** covering all points in that cluster.

3. Small clusters → grouped into larger clusters → repeated until **one top-level cluster** remains.

This forms a **hierarchical tree of clusters**.

---

### Searching with Ball Tree
When a query arrives:
- Determine which **ball** (cluster) is likely to contain nearest neighbors.
- **Prune** entire balls that are too far away.
- Compute distances **only inside relevant clusters**.

### Key Advantage:
**No backtracking** is required (unlike K-d Tree).

---

## 5. Comparison Summary

| Feature | K-d Tree | Ball Tree |
|--------|---------|-----------|
| Splitting Method | Axis-based median splits | Distance-based cluster grouping |
| Best For | Low-dimensional continuous data | High-dimensional or irregular data |
| Search Strategy | Requires backtracking | Prunes aggressively without backtracking |
| Speed | Fast for structured data | Fast for complex/unstructured data |

---

## 6. Key Takeaways
- Standard KNN has time complexity \( O(n) \) per query.
- **K-d Tree** partitions data using axis-aligned splits and reduces unnecessary comparisons.
- **Ball Tree** groups nearby points into clusters (balls) and avoids backtracking.
- Both methods significantly improve KNN performance on large datasets.

---
