# Decision Trees

[← Back to Machine Learning](../README.md)

## Overview

Decision Trees are hierarchical models that make predictions by learning simple decision rules from data features. They partition the feature space into regions and assign predictions based on the majority class (classification) or average value (regression) in each region.

## How Decision Trees Work

Decision trees recursively split the data based on feature values that best separate the target variable. Each internal node represents a test on a feature, each branch represents the outcome of the test, and each leaf node represents a class label or continuous value.

### Visual Tutorial

For an excellent visual explanation of how decision trees work, see this comprehensive tutorial:

**[Decision Trees Tutorial - AlgoBeans](https://algobeans.com/2016/07/27/decision-trees-tutorial/)**

This tutorial provides:
- Intuitive visualizations of tree construction
- Step-by-step splitting process
- Examples of decision boundaries
- Comparison with other algorithms

## Key Concepts

### Splitting Criteria

**Classification Trees**:
- **Gini Impurity**: Measures probability of incorrect classification
  - Formula: `Gini = 1 - Σ(p_i)²`
  - Lower is better (0 = pure node)
- **Entropy (Information Gain)**: Measures disorder/uncertainty
  - Formula: `Entropy = -Σ(p_i * log₂(p_i))`
  - Information Gain = Entropy(parent) - Weighted Entropy(children)

**Regression Trees**:
- **Mean Squared Error (MSE)**: Variance reduction
- **Mean Absolute Error (MAE)**: Robust to outliers

### Tree Construction

1. **Start** with all data at root node
2. **Find best split**: Test all features and thresholds
3. **Split** data into child nodes
4. **Recurse** on each child node
5. **Stop** when stopping criterion met

### Stopping Criteria

- Maximum depth reached
- Minimum samples per leaf
- Minimum impurity decrease
- All samples in node have same label

## Advantages

✅ **Interpretable**: Easy to visualize and explain
✅ **No preprocessing**: Handles mixed data types, no scaling needed
✅ **Non-linear**: Captures complex relationships
✅ **Feature importance**: Automatically ranks features
✅ **Fast prediction**: O(log n) for balanced trees

## Disadvantages

❌ **Overfitting**: High variance, sensitive to data changes
❌ **Instability**: Small data changes → different tree
❌ **Biased**: Favors features with more levels
❌ **Not optimal**: Greedy algorithm, locally optimal splits
❌ **Poor extrapolation**: Cannot predict beyond training range

## Hyperparameters

| Parameter | Description | Typical Values | Effect |
|-----------|-------------|----------------|--------|
| `max_depth` | Maximum tree depth | 3-10 | Controls overfitting |
| `min_samples_split` | Min samples to split node | 2-20 | Prevents overfitting |
| `min_samples_leaf` | Min samples in leaf | 1-10 | Smooths predictions |
| `max_features` | Features to consider per split | sqrt(n), log2(n), None | Reduces correlation |
| `criterion` | Split quality measure | gini, entropy | Splitting strategy |

## Best Practices

1. **Start simple**: Use default parameters first
2. **Prune**: Limit depth or use min_samples_leaf
3. **Ensemble**: Use Random Forest or Gradient Boosting
4. **Visualize**: Plot tree to understand decisions
5. **Feature engineering**: Create meaningful features

## Use Cases

- **Interpretability required**: Medical diagnosis, credit scoring
- **Mixed data types**: Categorical + numerical features
- **Baseline model**: Quick first model
- **Feature selection**: Identify important features
- **Rule extraction**: Convert to if-then rules

## Implementation

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Create and train
clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5)
clf.fit(X_train, y_train)

# Visualize
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=feature_names, class_names=class_names, filled=True)
plt.show()

# Feature importance
importances = clf.feature_importances_
```

## Related Topics

- [Random Forests](random-forests.md) - Ensemble of decision trees
- [Gradient Boosting](gradient-boosting.md) - Sequential tree ensemble
- [XGBoost](xgboost.md) - Optimized gradient boosting
- [Back to Machine Learning](../README.md)

## External Resources

- 📚 [Decision Trees Tutorial - AlgoBeans](https://algobeans.com/2016/07/27/decision-trees-tutorial/) - Visual explanation
- 📖 [Scikit-learn Documentation](https://scikit-learn.org/stable/modules/tree.html)
- 📊 [Visualizing Decision Trees](https://explained.ai/decision-tree-viz/)

---

*Decision trees are the building blocks of powerful ensemble methods like Random Forests and Gradient Boosting.*
