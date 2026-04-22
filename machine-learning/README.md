# Machine Learning

[← Back to Main](../README.md)

## Overview

Machine Learning encompasses classical algorithms that learn patterns from data without explicit programming. This section focuses on traditional ML models - the foundational algorithms that preceded deep learning and remain highly effective for many tasks, especially with structured/tabular data.

## Classical ML Models

![ML Paradigms](diagrams/ml-paradigms.png)

### Linear Models

**Core Concept**: Model relationships as linear combinations of features

| Model | Task | Regularization | Interpretability | Speed | Best For |
|-------|------|----------------|------------------|-------|----------|
| **[Linear Regression](linear-regression.md)** | Regression | None (OLS) | High | Very Fast | Baseline, linear relationships |
| **[Ridge](ridge-regression.md)** | Regression | L2 (shrinkage) | High | Very Fast | Multicollinearity, many features |
| **[Lasso](lasso-regression.md)** | Regression | L1 (sparsity) | High | Fast | Feature selection, sparse models |
| **[Elastic Net](elastic-net.md)** | Regression | L1 + L2 | High | Fast | Grouped features, balance |
| **[Logistic Regression](logistic-regression.md)** | Classification | Optional L1/L2 | High | Very Fast | Binary/multi-class, baseline |
| **[Linear SVM](linear-svm.md)** | Classification | L2 (margin) | Medium | Fast | Large datasets, linear separation |
| **[Kernel SVM](kernel-svm.md)** | Classification | L2 (margin) | Low | Slow | Non-linear, small-medium data |
| **[SVR](svr.md)** | Regression | Epsilon-insensitive | Medium | Medium | Non-linear regression |

**Regularization Comparison**:
- **L1 (Lasso)**: Sparse solutions, feature selection, some coefficients → 0
- **L2 (Ridge)**: Shrinks all coefficients, handles multicollinearity, no feature selection
- **Elastic Net**: Combines L1 + L2, best of both worlds

### Distance-Based Models

**Core Concept**: Predictions based on similarity/distance metrics

- **[K-Nearest Neighbors (KNN)](knn.md)** - Instance-based learning
  - Classification (majority vote)
  - Regression (average)
  - Distance metrics (Euclidean, Manhattan, Minkowski)
  - Weighted KNN

- **[K-Means Clustering](k-means.md)** - Centroid-based clustering
  - Standard K-means
  - K-means++
  - Mini-batch K-means
  - Elbow method for K selection

- **[KD-Tree](kd-tree.md)** - Space-partitioning data structure
  - Efficient nearest neighbor search
  - Range queries
  - Construction and traversal
  - Ball trees as alternative

### Tree-Based Models

![Tree Models](diagrams/tree-models.png)

**Core Concept**: Hierarchical decision rules

| Model | Type | Ensemble | Speed | Overfitting Risk | Handles Categorical | Best For |
|-------|------|----------|-------|-----------------|---------------------|----------|
| **[Decision Tree](decision-trees.md)** | Single | No | Fast | High | Yes | Interpretability, baseline |
| **[Random Forest](random-forests.md)** | Bagging | Yes (parallel) | Medium | Low | Yes | General purpose, robust |
| **[XGBoost](xgboost.md)** | Boosting | Yes (sequential) | Fast | Medium | With encoding | Competitions, performance |
| **[LightGBM](lightgbm.md)** | Boosting | Yes (sequential) | Very Fast | Medium | With encoding | Large datasets, speed |
| **[CatBoost](catboost.md)** | Boosting | Yes (sequential) | Medium | Low | Native support | Categorical features |
| **[AdaBoost](adaboost.md)** | Boosting | Yes (sequential) | Medium | Medium | Yes | Weak learners, simple |

**Gradient Boosting Comparison**:

| Feature | XGBoost | LightGBM | CatBoost |
|---------|---------|----------|----------|
| **Speed** | Fast | Fastest | Medium |
| **Memory** | Medium | Low | Medium |
| **Categorical** | Manual encoding | Manual encoding | Native |
| **Overfitting** | Moderate | Higher risk | Lower risk |
| **GPU Support** | Yes | Yes | Yes |
| **Best For** | Balanced performance | Large data, speed | Categorical data |
| **Hyperparameters** | Many | Many | Fewer (auto-tuned) |

### Probabilistic Models

**Core Concept**: Modeling probability distributions

- **[Naive Bayes](naive-bayes.md)** - Probabilistic classifier
  - Gaussian Naive Bayes
  - Multinomial Naive Bayes
  - Bernoulli Naive Bayes
  - Feature independence assumption

- **[Gaussian Mixture Models (GMM)](gmm.md)** - Soft clustering
  - Expectation-Maximization (EM) algorithm
  - Covariance types (full, tied, diagonal, spherical)
  - Model selection (BIC, AIC)

- **[Hidden Markov Models (HMM)](hmm.md)** - Sequential probabilistic models
  - Forward-backward algorithm
  - Viterbi algorithm
  - Baum-Welch training

### Clustering Models

![Clustering Methods](diagrams/clustering-methods.png)

| Model | Shape Flexibility | Needs K | Handles Noise | Speed | Scalability | Best For |
|-------|------------------|---------|---------------|-------|-------------|----------|
| **[K-Means](k-means.md)** | Spherical only | Yes | No | Very Fast | Excellent | Large data, spherical clusters |
| **[Hierarchical](hierarchical-clustering.md)** | Any | No | No | Slow | Poor | Small data, dendrogram |
| **[DBSCAN](dbscan.md)** | Arbitrary | No | Yes | Medium | Good | Arbitrary shapes, noise |
| **[HDBSCAN](hdbscan.md)** | Arbitrary | No | Yes | Medium | Good | Varying density, noise |
| **[Mean Shift](mean-shift.md)** | Arbitrary | No | Partial | Slow | Poor | Mode finding, few clusters |
| **[Spectral](spectral-clustering.md)** | Non-convex | Yes | No | Slow | Poor | Graph data, non-convex |
| **[GMM](gmm.md)** | Elliptical | Yes | Partial | Medium | Good | Soft clustering, probabilistic |
| **[OPTICS](optics.md)** | Arbitrary | No | Yes | Slow | Medium | Varying density |

**Linkage Methods** (Hierarchical):
- **Single**: Minimum distance between clusters (chaining effect)
- **Complete**: Maximum distance (compact clusters)
- **Average**: Mean distance (balanced)
- **Ward**: Minimizes within-cluster variance (most popular)

## Model Comparison

### Model Characteristics

| Model Family | Interpretability | Training Speed | Prediction Speed | Memory | Handles Non-linear | Handles Mixed Types | Robust to Outliers |
|--------------|-----------------|----------------|------------------|--------|-------------------|--------------------|--------------------|
| **Linear** | High | Fast | Fast | Low | No | With encoding | No |
| **Tree-based** | Medium | Medium-Slow | Fast | Medium | Yes | Yes | Yes |
| **Distance-based** | Low | None/Fast | Slow | High | Yes | With encoding | No |
| **Probabilistic** | High | Fast | Fast | Low | Limited | Yes | No |

### Model Selection by Dataset

| Dataset Size | Recommended Models | Avoid |
|--------------|-------------------|-------|
| **Small (<1K)** | Naive Bayes, KNN, Linear models, Decision Trees | Deep ensembles, complex models |
| **Medium (1K-100K)** | Random Forest, SVM, XGBoost, LightGBM | KNN (slow prediction) |
| **Large (>100K)** | LightGBM, XGBoost, Linear models, SGD | KNN, Standard SVM |

### Model Selection by Feature Type

| Feature Type | Best Models | Notes |
|--------------|-------------|-------|
| **Numerical only** | Any model | Consider scaling for distance/linear models |
| **Categorical heavy** | Tree-based (CatBoost), Naive Bayes | CatBoost handles categories natively |
| **Mixed** | Tree-based, Linear (with encoding) | Encode categoricals for linear models |
| **High-dimensional** | Linear (L1/L2), Random Forest | L1 for feature selection |
| **Sparse** | Linear models, Naive Bayes | Efficient with sparse matrices |

### Model Selection by Problem Type

| Problem | Top Choices | Fast Baseline | Interpretable Option |
|---------|-------------|---------------|---------------------|
| **Binary Classification** | XGBoost, LightGBM, SVM | Logistic Regression | Logistic Regression, Decision Tree |
| **Multi-class** | XGBoost, Random Forest | Naive Bayes | Decision Tree |
| **Regression** | XGBoost, LightGBM, Random Forest | Linear Regression | Linear Regression, Decision Tree |
| **Clustering** | K-means, DBSCAN | K-means | Hierarchical (with dendrogram) |
| **Anomaly Detection** | Isolation Forest, One-class SVM | Z-score | Isolation Forest |

### Performance Characteristics

| Model | Training | Prediction | Memory | Scales to Large Data |
|-------|----------|------------|--------|---------------------|
| **Naive Bayes** | Very Fast | Very Fast | Very Low | Yes |
| **Linear Models** | Fast | Very Fast | Very Low | Yes (SGD) |
| **Decision Tree** | Fast | Fast | Low | No |
| **KNN** | None | Very Slow | Very High | No |
| **SVM** | Slow | Medium | Medium | No (kernel) |
| **Random Forest** | Medium | Fast | Medium | Partial |
| **XGBoost** | Medium | Fast | Medium | Yes |
| **LightGBM** | Fast | Fast | Low | Yes |
| **CatBoost** | Slow | Fast | Medium | Yes |

## Hyperparameter Tuning

### Key Hyperparameters by Model

**Random Forest**
- `n_estimators`: Number of trees (100-1000)
- `max_depth`: Tree depth (None, 10-50)
- `min_samples_split`: Minimum samples to split (2-20)
- `max_features`: Features per split ('sqrt', 'log2', None)

**XGBoost/LightGBM**
- `learning_rate`: Step size (0.01-0.3)
- `n_estimators`: Number of boosting rounds (100-1000)
- `max_depth`: Tree depth (3-10)
- `subsample`: Row sampling (0.5-1.0)
- `colsample_bytree`: Column sampling (0.5-1.0)

**SVM**
- `C`: Regularization (0.1-100)
- `kernel`: Kernel type ('linear', 'rbf', 'poly')
- `gamma`: Kernel coefficient (0.001-1)

**KNN**
- `n_neighbors`: Number of neighbors (3-20)
- `weights`: Weighting scheme ('uniform', 'distance')
- `metric`: Distance metric ('euclidean', 'manhattan')

## Implementation Libraries

<div style="color: green;">

### Python Libraries
- **scikit-learn** - Comprehensive ML library
- **XGBoost** - Optimized gradient boosting
- **LightGBM** - Fast gradient boosting
- **CatBoost** - Categorical feature handling
- **statsmodels** - Statistical modeling

### R Libraries
- **caret** - Unified ML interface
- **randomForest** - Random forest implementation
- **xgboost** - XGBoost for R
- **e1071** - SVM and other algorithms

</div>

## Best Practices

### Model Development
1. Start with simple baselines (logistic regression, decision tree)
2. Try ensemble methods (Random Forest, XGBoost)
3. Tune hyperparameters systematically
4. Use cross-validation for robust evaluation
5. Consider model interpretability requirements

### Feature Engineering
- Handle missing values appropriately
- Scale features for distance-based models
- Encode categorical variables
- Create interaction features for linear models
- Use domain knowledge

### Avoiding Overfitting
- Use regularization (L1/L2)
- Limit model complexity (tree depth, number of features)
- Employ cross-validation
- Use ensemble methods
- Gather more training data

## Related Topics

- [Deep Learning](../deep-learning/README.md) - Neural network models
- [Data Science](../data-science/README.md) - Data preparation and analysis
- [MLOps](../mlops/README.md) - Model deployment and monitoring
- [Tabular Data](../modalities/tabular/README.md) - Techniques for structured data

## Further Learning

<div style="color: green;">

### Books
- "Hands-On Machine Learning" by Aurélien Géron
- "The Elements of Statistical Learning" by Hastie, Tibshirani, Friedman
- "Pattern Recognition and Machine Learning" by Christopher Bishop
- "Introduction to Statistical Learning" by James, Witten, Hastie, Tibshirani

### Courses
- Andrew Ng's Machine Learning (Coursera)
- Fast.ai Machine Learning Course
- Stanford CS229
- Applied Machine Learning (Columbia)

### Documentation
- scikit-learn User Guide
- XGBoost Documentation
- LightGBM Documentation
- CatBoost Documentation

</div>

---

*Classical ML models remain the workhorses for structured data problems, offering excellent performance, interpretability, and efficiency.*