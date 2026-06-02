# Data Science

[← Back to Main](../README.md)

## Overview

Data Science focuses on extracting insights from data through statistical analysis, visualization, and modeling. This section covers data manipulation techniques (dimensionality reduction, imputation, sampling, normalization, augmentation) and model analysis methods (fairness, complexity, explainability, metrics).

## End-to-End Data Science Workflow

Understanding how different techniques fit together is crucial. This flowchart shows the complete data science workflow from raw data to deployed model:

![Data Science Method Relationships](diagrams/method-relationships.png)

**Key Workflow Stages**:
1. **📊 Data Preprocessing**: Handle missing values, outliers, and scaling
2. **🔍 Exploratory Analysis**: Understand distributions, correlations, and patterns
3. **⚙️ Feature Engineering**: Dimensionality reduction, resampling, encoding
4. **🤖 Modeling**: Select and train appropriate algorithms
5. **📈 Evaluation**: Assess performance and iterate

Each stage connects to specific techniques detailed below. Use this workflow to understand when and why to apply each method.

## Data Techniques

### Dimensionality Reduction

![Data Science Workflow](diagrams/ds-workflow.png)

**Core Concept**: Reducing feature space while preserving information

**How PCA Works - Visual Explanation**:

![PCA Eigenvalues and Eigenvectors](https://miro.medium.com/v2/resize:fit:1400/1*QinDfRawRskupf4mU5bYSA.png)
*PCA finds the directions (eigenvectors) of maximum variance in the data. The first principal component captures the most variance, the second captures the next most, and so on. This allows dimensionality reduction while preserving the most important information.*
*Image source: [Eigenvalues and Eigenvectors Explained](https://medium.com/data-science/eigenvalues-and-eigenvectors-378e851bf372)*

**Approaches**: Matrix-based (linear algebra) vs Graph-based (manifold learning)

| Method | Type | Linear | Preserves | Speed | Best For | Limitations |
|--------|------|--------|-----------|-------|----------|-------------|
| **[PCA](pages/pca.md)** | Matrix | Yes | Global variance | Fast | High-dim data, preprocessing | Assumes linearity |
| **[t-SNE](pages/tsne.md)** | Graph | No | Local structure | Slow | Visualization (2D/3D) | Not for new data, slow |
| **[UMAP](pages/umap.md)** | Graph | No | Local + global | Fast | Large datasets, clustering | Hyperparameter sensitive |
| **[LDA](pages/lda.md)** | Matrix | Yes | Class separation | Fast | Supervised tasks | Requires labels |
| **[ICA](pages/ica.md)** | Matrix | Yes | Independence | Medium | Signal separation | Assumes independence |
| **[Isomap](pages/isomap.md)** | Graph | No | Geodesic distance | Medium | Non-linear manifolds | Sensitive to noise |
| **[LLE](pages/lle.md)** | Graph | No | Local geometry | Medium | Non-linear manifolds | Requires dense sampling |
| **[Autoencoder](pages/autoencoder-dr.md)** | Neural | No | Learned features | Medium | Complex patterns | Needs training data |

**Selection Guide**:
- **Visualization**: t-SNE, UMAP
- **Preprocessing**: PCA, ICA
- **Supervised**: LDA
- **Large datasets**: UMAP, PCA
- **Non-linear patterns**: UMAP, Autoencoder, Kernel PCA

### Data Imputation

**Core Concept**: Handling missing values

**Missing Data Patterns**:
- **MCAR** (Missing Completely At Random): Missingness independent of data
- **MAR** (Missing At Random): Missingness depends on observed data
- **MNAR** (Missing Not At Random): Missingness depends on unobserved data

| Method | Type | Complexity | Preserves Distribution | Best For | Limitations |
|--------|------|------------|----------------------|----------|-------------|
| **[Mean/Median/Mode](pages/simple-imputation.md)** | Simple | Low | No | Quick baseline, MCAR | Reduces variance |
| **[Forward/Backward Fill](pages/ffill-bfill.md)** | Simple | Low | Partial | Time series | Creates autocorrelation |
| **[Constant Value](pages/constant-imputation.md)** | Simple | Low | No | Domain knowledge | Arbitrary choice |
| **[Random Sampling](pages/random-imputation.md)** | Simple | Low | Yes | MCAR data | Ignores relationships |
| **[Regression](pages/regression-imputation.md)** | Statistical | Medium | Partial | MAR, relationships | Underestimates variance |
| **[Stochastic Regression](pages/stochastic-regression.md)** | Statistical | Medium | Yes | MAR, variance preservation | More complex |
| **[KNN](pages/knn-imputation.md)** | ML | Medium | Yes | Local patterns | Computationally expensive |
| **[MICE](pages/mice.md)** | ML | High | Yes | Multiple variables, MAR | Slow, requires iterations |
| **[Matrix Factorization](pages/matrix-factorization.md)** | ML | High | Yes | High-dimensional, patterns | Needs sufficient data |
| **[Deep Learning](pages/dl-imputation.md)** | ML | High | Yes | Complex patterns | Requires training data |

**Selection Guide**:
- **Quick analysis**: Mean/Median
- **Time series**: Forward/Backward fill
- **Preserve variance**: Stochastic regression, MICE
- **Complex patterns**: KNN, Deep Learning
- **Multiple variables**: MICE, Matrix Factorization

### Sampling Techniques

| Method | Type | Preserves Distribution | Complexity | Best For | Limitations |
|--------|------|----------------------|------------|----------|-------------|
| **[Simple Random](pages/simple-random.md)** | Probability | No | Low | Homogeneous population | May miss subgroups |
| **[Systematic](pages/systematic-sampling.md)** | Probability | No | Low | Ordered data | Periodic patterns risk |
| **[Stratified](pages/stratified-sampling.md)** | Probability | Yes | Medium | Heterogeneous population | Requires strata knowledge |
| **[Cluster](pages/cluster-sampling.md)** | Probability | Partial | Medium | Geographically dispersed | Higher variance |
| **[Bootstrap](pages/bootstrap.md)** | Resampling | Yes | Low | Confidence intervals | Assumes independence |
| **[Cross-Validation](pages/cross-validation.md)** | Resampling | Yes | Medium | Model evaluation | Computationally expensive |

**Imbalanced Data Sampling**:

| Technique | Approach | Data Size | Overfitting Risk | Best For | Avoid When |
|-----------|----------|-----------|-----------------|----------|------------|
| **[Random Oversampling](pages/random-oversample.md)** | Duplicate minority | Increases | High | Quick baseline | Exact duplicates |
| **[SMOTE](pages/smote.md)** | Synthetic minority | Increases | Medium | General purpose | High-dimensional |
| **[ADASYN](pages/adasyn.md)** | Adaptive synthetic | Increases | Medium | Varying density | Noisy data |
| **[Random Undersampling](pages/random-undersample.md)** | Remove majority | Decreases | Low | Large datasets | Information loss |
| **[Tomek Links](pages/tomek-links.md)** | Remove boundary | Decreases | Low | Clean boundaries | Aggressive removal |
| **[SMOTEENN](pages/smoteenn.md)** | SMOTE + ENN | Varies | Low | Noisy boundaries | Complex |
| **[SMOTETomek](pages/smotetomek.md)** | SMOTE + Tomek | Varies | Low | Clean synthetic | Two-step process |

### Normalization and Scaling

**Core Concept**: Bringing features to comparable scales

#### Feature Scaling Methods

| Method | Formula | Range | Robust to Outliers | Best For | Avoid When |
|--------|---------|-------|-------------------|----------|------------|
| **[Min-Max](pages/minmax-scaling.md)** | (x - min) / (max - min) | [0, 1] | No | Neural networks, bounded features | Outliers present |
| **[Standardization](pages/standardization.md)** | (x - μ) / σ | Unbounded | No | Linear models, PCA, clustering | Non-Gaussian data |
| **[Robust Scaling](pages/robust-scaling.md)** | (x - median) / IQR | Unbounded | Yes | Outliers present | Need specific range |
| **[MaxAbs](pages/maxabs-scaling.md)** | x / \|max\| | [-1, 1] | No | Sparse data | Dense data with outliers |
| **[L1 Normalization](pages/l1-norm.md)** | x / Σ\|x\| | Sum = 1 | No | Text data, sparse features | Need variance info |
| **[L2 Normalization](pages/l2-norm.md)** | x / √(Σx²) | Norm = 1 | No | Cosine similarity, embeddings | Need magnitude info |

#### Distribution Transformations

| Method | Purpose | Handles Negatives | Handles Zeros | Best For | Limitations |
|--------|---------|------------------|---------------|----------|-------------|
| **[Log](pages/log-transform.md)** | Reduce skewness | No | No | Right-skewed data | Requires x > 0 |
| **[Box-Cox](pages/box-cox.md)** | Normalize distribution | No | No | Positive data, find optimal λ | Requires x > 0 |
| **[Yeo-Johnson](pages/yeo-johnson.md)** | Normalize distribution | Yes | Yes | Any data, find optimal λ | More complex |
| **[Quantile](pages/quantile-transform.md)** | Match target distribution | Yes | Yes | Non-parametric, uniform/normal | Loses outlier info |
| **[Power](pages/power-transform.md)** | Reduce skewness | Depends | Yes | Flexible transformation | Parameter selection |

#### Categorical Encoding

| Method | Output | Cardinality | Preserves Order | Best For | Limitations |
|--------|--------|-------------|----------------|----------|-------------|
| **[One-Hot](pages/onehot-encoding.md)** | Binary columns | High-dim | No | Tree models, low cardinality | Curse of dimensionality |
| **[Label](pages/label-encoding.md)** | Integer | Low-dim | No | Tree models only | Implies ordering |
| **[Ordinal](pages/ordinal-encoding.md)** | Integer | Low-dim | Yes | Ordered categories | Requires order |
| **[Target](pages/target-encoding.md)** | Float | Low-dim | No | High cardinality | Overfitting risk |
| **[Binary](pages/binary-encoding.md)** | Binary | Medium-dim | No | High cardinality | Less interpretable |
| **[Frequency](pages/frequency-encoding.md)** | Float | Low-dim | No | Rare categories | Loses uniqueness |

**Selection Guide**:
- **Distance-based models** (KNN, SVM): Standardization or Min-Max
- **Tree-based models**: No scaling needed (but encoding required)
- **Neural networks**: Min-Max or Standardization
- **With outliers**: Robust Scaling
- **Sparse data**: MaxAbs, L1 normalization

### Data Augmentation

| Modality | Technique | Preserves Semantics | Complexity | Best For | Risk |
|----------|-----------|-------------------|------------|----------|------|
| **[Image](pages/image-augmentation.md)** | Geometric transforms | Yes | Low | CV, small datasets | Over-augmentation |
| **[Image](pages/image-augmentation.md)** | Color jittering | Yes | Low | Lighting variations | Unrealistic colors |
| **[Image](pages/image-augmentation.md)** | Mixup/CutMix | Partial | Medium | Regularization | Label noise |
| **[Image](pages/image-augmentation.md)** | AutoAugment | Yes | High | Optimal policy | Expensive search |
| **[Text](pages/text-augmentation.md)** | Synonym replacement | Yes | Low | Small datasets | Context loss |
| **[Text](pages/text-augmentation.md)** | Back-translation | Yes | High | Paraphrasing | Translation errors |
| **[Text](pages/text-augmentation.md)** | Contextual embeddings | Yes | Medium | Semantic variations | Requires LLM |
| **[Tabular](pages/tabular-augmentation.md)** | SMOTE | Partial | Medium | Imbalanced data | Unrealistic combinations |
| **[Tabular](pages/tabular-augmentation.md)** | Gaussian noise | Partial | Low | Continuous features | Distribution shift |
| **[Tabular](pages/tabular-augmentation.md)** | CTGAN | Yes | High | Complex distributions | Training required |
| **[Time Series](pages/time-series-augmentation.md)** | Window slicing | Yes | Low | More samples | Temporal correlation |
| **[Time Series](pages/time-series-augmentation.md)** | Jittering | Yes | Low | Noise robustness | Signal distortion |
| **[Time Series](pages/time-series-augmentation.md)** | Time warping | Yes | Medium | Temporal variations | Pattern distortion |

**Augmentation Strategy**:
- **Small datasets**: Aggressive augmentation
- **Large datasets**: Light augmentation for regularization
- **Imbalanced**: Focus on minority class
- **Production**: Test augmented data quality

## Model Analysis

### Model Complexity

**Core Concept**: Understanding model capacity and generalization

**Bias-Variance Tradeoff**:
- **High Bias (Underfitting)**: Model too simple, poor training performance
- **High Variance (Overfitting)**: Model too complex, poor generalization
- **Optimal Complexity**: Balance between bias and variance
- **Diagnosis**: Learning curves, validation curves

#### Regularization Techniques

| Technique | Effect | Sparsity | Complexity | Best For | Trade-off |
|-----------|--------|----------|------------|----------|-----------|
| **[L1 (Lasso)](pages/l1-regularization.md)** | Feature selection | Yes | O(n) | High-dimensional | May underfit |
| **[L2 (Ridge)](pages/l2-regularization.md)** | Weight shrinkage | No | O(n) | Multicollinearity | Keeps all features |
| **[Elastic Net](pages/elastic-net.md)** | L1 + L2 | Partial | O(n) | Correlated features | Two hyperparameters |
| **[Dropout](pages/dropout.md)** | Random deactivation | No | O(n) | Neural networks | Training time |
| **[Early Stopping](pages/early-stopping.md)** | Stop training | No | O(1) | Any iterative | Validation needed |

#### Model Selection Criteria

| Criterion | Formula | Penalty | Best For | Limitations |
|-----------|---------|---------|----------|-------------|
| **[AIC](pages/aic.md)** | 2k - 2ln(L) | 2k | Large samples | Overfits small data |
| **[BIC](pages/bic.md)** | k×ln(n) - 2ln(L) | k×ln(n) | Model selection | Penalizes complexity more |
| **[MDL](pages/mdl.md)** | L(model) + L(data\|model) | Description length | Compression | Computationally complex |
| **[Cross-Validation](pages/cv-selection.md)** | Empirical error | None | Robust estimate | Computationally expensive |

**Model Capacity Measures**:
- **VC Dimension**: Maximum points that can be shattered
- **Rademacher Complexity**: Expected supremum of empirical process
- **Parameter Count**: Number of learnable weights
- **Depth vs Width**: Network architecture trade-offs

### Model Explainability

| Method | Scope | Model-Agnostic | Complexity | Best For | Limitations |
|--------|-------|----------------|------------|----------|-------------|
| **[Permutation Importance](pages/permutation-importance.md)** | Global | Yes | O(n×m) | Any model | Correlated features |
| **[Tree Importance](pages/tree-importance.md)** | Global | No | O(1) | Tree models | Biased to high-cardinality |
| **[Coefficients](pages/coefficient-importance.md)** | Global | No | O(1) | Linear models | Requires scaling |
| **[SHAP](pages/shap.md)** | Local/Global | Yes | O(2^n) or O(n²) | Consistent values | Computationally expensive |
| **[LIME](pages/lime.md)** | Local | Yes | O(k×m) | Simple explanations | Unstable |
| **[PDP](pages/pdp.md)** | Global | Yes | O(n×m) | Feature effects | Assumes independence |
| **[ICE](pages/ice.md)** | Local | Yes | O(n×m) | Individual effects | Many plots |
| **[ALE](pages/ale.md)** | Global | Yes | O(n×m) | Correlated features | Complex interpretation |
| **[Counterfactuals](pages/counterfactuals.md)** | Local | Yes | O(optimization) | Actionable insights | May be unrealistic |

**Selection Guide**:
- **Global understanding**: SHAP summary, Permutation Importance, PDP
- **Local predictions**: SHAP force plots, LIME, Counterfactuals
- **Fast computation**: Tree importance, Coefficients
- **Correlated features**: ALE, SHAP

### Model Fairness

**Core Concept**: Ensuring equitable predictions across groups

#### Fairness Metrics

| Metric | Definition | Requires | Best For | Limitations |
|--------|------------|----------|----------|-------------|
| **[Demographic Parity](pages/demographic-parity.md)** | P(Ŷ=1\|A=0) = P(Ŷ=1\|A=1) | Predictions | Equal selection rates | Ignores ground truth |
| **[Equalized Odds](pages/equalized-odds.md)** | TPR & FPR equal across groups | Labels | Overall fairness | Strict requirement |
| **[Equal Opportunity](pages/equal-opportunity.md)** | TPR equal across groups | Labels | Positive outcomes | Ignores FPR |
| **[Predictive Parity](pages/predictive-parity.md)** | PPV equal across groups | Labels | Precision fairness | May allow different TPR |
| **[Individual Fairness](pages/individual-fairness.md)** | Similar individuals → similar predictions | Similarity metric | Case-by-case | Defining similarity |

#### Bias Mitigation Strategies

| Stage | Technique | Approach | Complexity | Best For | Limitations |
|-------|-----------|----------|------------|----------|-------------|
| **[Pre-processing](pages/preprocessing-fairness.md)** | Reweighting | Adjust sample weights | Low | Simple fix | Limited impact |
| **[Pre-processing](pages/preprocessing-fairness.md)** | Resampling | Balance groups | Low | Imbalanced data | Data loss/duplication |
| **[In-processing](pages/inprocessing-fairness.md)** | Fairness constraints | Regularization | Medium | During training | Model-specific |
| **[In-processing](pages/inprocessing-fairness.md)** | Adversarial debiasing | GAN-like training | High | Deep learning | Training complexity |
| **[Post-processing](pages/postprocessing-fairness.md)** | Threshold optimization | Adjust decision boundary | Low | Model-agnostic | May reduce accuracy |
| **[Post-processing](pages/postprocessing-fairness.md)** | Calibration | Adjust probabilities | Medium | Probabilistic models | Requires validation set |

**Fairness-Accuracy Trade-off**:
- No free lunch: improving fairness often reduces accuracy
- Context matters: legal, ethical, and domain considerations
- Multi-objective optimization: Pareto frontier analysis
- Stakeholder involvement: define acceptable trade-offs

### Evaluation Metrics

#### Classification Metrics

| Metric | Formula | Range | Balanced | Best For | Limitations |
|--------|---------|-------|----------|----------|-------------|
| **[Accuracy](pages/accuracy.md)** | (TP+TN)/(TP+TN+FP+FN) | [0, 1] | No | Balanced classes | Misleading with imbalance |
| **[Precision](pages/precision.md)** | TP/(TP+FP) | [0, 1] | No | Minimize false positives | Ignores false negatives |
| **[Recall](pages/recall.md)** | TP/(TP+FN) | [0, 1] | No | Minimize false negatives | Ignores false positives |
| **[F1-Score](pages/f1-score.md)** | 2×(P×R)/(P+R) | [0, 1] | Yes | Balance P and R | Equal weight to P/R |
| **[F-beta](pages/f-beta.md)** | (1+β²)×(P×R)/(β²P+R) | [0, 1] | Yes | Custom P/R weight | Parameter selection |
| **[ROC-AUC](pages/roc-auc.md)** | Area under ROC curve | [0, 1] | Yes | Threshold-independent | Optimistic with imbalance |
| **[PR-AUC](pages/pr-auc.md)** | Area under PR curve | [0, 1] | Yes | Imbalanced data | Less intuitive |
| **[MCC](pages/mcc.md)** | Correlation coefficient | [-1, 1] | Yes | Imbalanced data | Less known |
| **[Cohen's Kappa](pages/cohens-kappa.md)** | Agreement beyond chance | [-1, 1] | Yes | Inter-rater reliability | Requires interpretation |
| **[Log Loss](pages/log-loss.md)** | -Σ(y×log(p)) | [0, ∞] | Yes | Probability calibration | Sensitive to confidence |

**Multi-class Averaging**:
- **Macro**: Unweighted mean (treats all classes equally)
- **Micro**: Aggregate then compute (favors frequent classes)
- **Weighted**: Weighted by class frequency

#### Regression Metrics

| Metric | Formula | Units | Robust to Outliers | Interpretable | Best For |
|--------|---------|-------|-------------------|---------------|----------|
| **[MAE](pages/mae.md)** | Σ\|y-ŷ\|/n | Same as y | Yes | Yes | General purpose |
| **[MSE](pages/mse.md)** | Σ(y-ŷ)²/n | Squared | No | No | Penalize large errors |
| **[RMSE](pages/rmse.md)** | √(Σ(y-ŷ)²/n) | Same as y | No | Yes | Penalize large errors |
| **[MAPE](pages/mape.md)** | Σ\|y-ŷ\|/y×100 | Percentage | No | Yes | Relative errors |
| **[R²](pages/r-squared.md)** | 1 - SS_res/SS_tot | [0, 1] | No | Yes | Variance explained |
| **[Adjusted R²](pages/adj-r-squared.md)** | 1 - (1-R²)(n-1)/(n-p-1) | [0, 1] | No | Yes | Penalize complexity |
| **[Median AE](pages/median-ae.md)** | median(\|y-ŷ\|) | Same as y | Yes | Yes | Outliers present |
| **[Huber](pages/huber.md)** | Piecewise (L2/L1) | Same as y | Partial | No | Some outliers |
| **[Quantile](pages/quantile-loss.md)** | Asymmetric L1 | Same as y | Yes | No | Specific quantiles |

**Selection Guide**:
- **General**: RMSE, MAE
- **Outliers**: Median AE, Huber
- **Interpretability**: MAE, MAPE, R²
- **Large errors matter**: MSE, RMSE
- **Relative errors**: MAPE

#### Clustering Metrics

**Internal Metrics** (no ground truth needed):

| Metric | Range | Higher is Better | Measures | Best For | Limitations |
|--------|-------|-----------------|----------|----------|-------------|
| **[Silhouette](pages/silhouette.md)** | [-1, 1] | Yes | Cohesion & separation | General purpose | Convex clusters |
| **[Davies-Bouldin](pages/davies-bouldin.md)** | [0, ∞] | No | Cluster similarity | Compact clusters | Euclidean bias |
| **[Calinski-Harabasz](pages/calinski-harabasz.md)** | [0, ∞] | Yes | Between/within variance | Dense clusters | Convex clusters |
| **[Dunn Index](pages/dunn-index.md)** | [0, ∞] | Yes | Min separation/max diameter | Well-separated | Sensitive to outliers |

**External Metrics** (requires ground truth):

| Metric | Range | Higher is Better | Measures | Properties |
|--------|-------|-----------------|----------|------------|
| **[Adjusted Rand Index](pages/ari.md)** | [-1, 1] | Yes | Pair agreement | Chance-corrected |
| **[NMI](pages/nmi.md)** | [0, 1] | Yes | Mutual information | Normalized |
| **[Fowlkes-Mallows](pages/fowlkes-mallows.md)** | [0, 1] | Yes | Geometric mean of P/R | Symmetric |
| **[Homogeneity](pages/homogeneity.md)** | [0, 1] | Yes | Cluster purity | One-sided |
| **[Completeness](pages/completeness.md)** | [0, 1] | Yes | Class grouping | One-sided |
| **[V-measure](pages/v-measure.md)** | [0, 1] | Yes | Harmonic mean H/C | Balanced |

## Statistical Analysis

| Category | Method | Type | Key Techniques | Best For |
|----------|--------|------|----------------|----------|
| **Hypothesis Testing** | **[Parametric Tests](pages/parametric-tests.md)** | Distributional assumptions | t-test, ANOVA, F-test, Z-test | Normal distributions, known parameters |
| | **[Non-parametric Tests](pages/nonparametric-tests.md)** | Distribution-free | Mann-Whitney U, Wilcoxon, Kruskal-Wallis, Chi-square, KS test | Non-normal data, ordinal data |
| | **[Multiple Testing](pages/multiple-testing.md)** | Correction methods | Bonferroni, Holm-Bonferroni, Benjamini-Hochberg (FDR) | Multiple comparisons |
| **Correlation** | **[Correlation Analysis](pages/correlation-analysis.md)** | Relationships | Pearson, Spearman, Kendall's tau, Point-biserial, Partial | Measuring associations |
| **Causation** | **[Causal Inference](pages/causal-inference.md)** | Causality | RCT, Observational studies, Propensity score matching, IV, DiD | Establishing cause-effect |

## Data Visualization

| Category | Plot Type | Variables | Key Techniques | Best For |
|----------|-----------|-----------|----------------|----------|
| **Exploratory** | **[Univariate Plots](pages/univariate-plots.md)** | Single | Histograms, Box plots, Violin plots, Density plots, QQ plots | Distribution analysis |
| | **[Bivariate Plots](pages/bivariate-plots.md)** | Two | Scatter plots, Line plots, Heatmaps, Hexbin plots, Joint plots | Relationships between two variables |
| | **[Multivariate Plots](pages/multivariate-plots.md)** | Multiple | Pair plots, Parallel coordinates, Radar charts, 3D scatter, DR plots | Complex relationships |
| **Statistical** | **[Distribution Plots](pages/distribution-plots.md)** | Single/Multiple | Empirical CDF, Probability plots, Quantile plots, KDE | Distribution properties |
| | **[Comparison Plots](pages/comparison-plots.md)** | Groups | Bar charts, Grouped box plots, Strip plots, Swarm plots | Group comparisons |

## Best Practices

### Data Preparation
1. Understand data types and distributions
2. Handle missing values appropriately
3. Detect and treat outliers
4. Scale features when necessary
5. Create validation strategy early

### Model Evaluation
1. Use appropriate metrics for the problem
2. Employ cross-validation
3. Check for overfitting/underfitting
4. Analyze errors and residuals
5. Consider business metrics

### Fairness and Ethics
1. Identify protected attributes
2. Measure fairness metrics
3. Mitigate detected biases
4. Document limitations
5. Consider societal impact

## Related Topics

- [Machine Learning](../machine-learning/README.md) - ML models
- [Deep Learning](../deep-learning/README.md) - Neural networks
- [Tabular Data](../modalities/tabular/README.md) - Structured data techniques
- [MLOps](../mlops/README.md) - Production considerations

---

*Data Science provides the techniques and tools for extracting insights from data and ensuring models are robust, fair, and interpretable.*