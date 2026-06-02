# Data Science

[← Back to Main](../README.md)

## Overview


## Historical Timeline

The evolution of Data Science from statistical computing to AI-augmented analytics:

```mermaid
timeline
    title Evolution of Data Science
    
    1960s-1970s : Statistical Computing
                : SPSS (1968)
                : SAS (1976)
                : Exploratory Data Analysis
                : Box-Jenkins Methods
    
    1980s : Database Era
          : Relational Databases
          : SQL Standard (1986)
          : Data Warehousing Concepts
          : OLAP Systems
    
    1990s : Data Mining Emerges
          : KDD Process (1996)
          : CRISP-DM (1996)
          : Association Rules (Apriori)
          : Decision Trees Popular
          : R Language (1993)
    
    2000s : Big Data Revolution
          : Hadoop (2006)
          : MapReduce
          : NoSQL Databases
          : Python for Data Science
          : Pandas Library (2008)
    
    2010-2012 : Data Science Profession
              : "Data Scientist" Role Defined
              : Kaggle Founded (2010)
              : Scikit-learn Mature
              : IPython Notebook (2011)
              : Big Data Hype
    
    2013-2015 : Visualization & Tools
              : Jupyter Notebook (2014)
              : Tableau Popular
              : D3.js Adoption
              : Spark (2014)
              : Data Journalism
    
    2016-2018 : ML Integration
              : AutoML Emergence
              : Deep Learning Integration
              : Cloud Data Platforms
              : Streaming Analytics
              : DataOps Concepts
    
    2019-2020 : Modern Data Stack
              : dbt (Data Build Tool)
              : Snowflake IPO (2020)
              : Data Mesh Concept
              : Feature Stores
              : MLOps Integration
    
    2021-Present : AI-Augmented Analytics
                 : LLMs for Data Analysis
                 : Automated Insights
                 : Real-time Analytics
                 : Data Observability
                 : Ethical AI & Fairness
```

Data Science focuses on extracting insights from data through statistical analysis, visualization, and modeling. This section covers data manipulation techniques (dimensionality reduction, imputation, sampling, normalization, augmentation) and model analysis methods (fairness, complexity, explainability, metrics).

## End-to-End Data Science Workflow

Understanding how different techniques fit together is crucial. This flowchart shows the complete data science workflow from raw data to deployed model:

```mermaid
graph TB
    subgraph Input["📊 Raw Data"]
        RawData[Raw Dataset<br/>Missing values, outliers,<br/>mixed scales]
    end
    
    subgraph Preprocessing["🔧 Data Preprocessing"]
        Missing{Missing<br/>Values?}
        Outliers{Outliers?}
        Scale{Different<br/>Scales?}
        
        Missing -->|Yes| Imputation[Imputation<br/>KNN, MICE, Mean]
        Missing -->|No| Outliers
        Imputation --> Outliers
        
        Outliers -->|Yes| OutlierHandle[Handle Outliers<br/>Remove, Cap, Transform]
        Outliers -->|No| Scale
        OutlierHandle --> Scale
        
        Scale -->|Yes| Scaling[Scaling<br/>StandardScaler, MinMax]
        Scale -->|No| CleanData
        Scaling --> CleanData[Clean Data]
    end
    
    subgraph Analysis["🔍 Exploratory Analysis"]
        CleanData --> EDA{What to<br/>explore?}
        EDA -->|Distributions| Viz1[Distribution Plots<br/>Histograms, Box plots]
        EDA -->|Relationships| Viz2[Correlation Analysis<br/>Scatter, Heatmaps]
        EDA -->|Patterns| Viz3[Multivariate Plots<br/>Pair plots, PCA viz]
        
        Viz1 --> Insights
        Viz2 --> Insights
        Viz3 --> Insights[Insights & Hypotheses]
    end
    
    subgraph FeatureEng["⚙️ Feature Engineering"]
        Insights --> FeatQ{Feature<br/>Issues?}
        FeatQ -->|Too many features| DimRed[Dimensionality Reduction<br/>PCA, UMAP, t-SNE]
        FeatQ -->|Imbalanced classes| Sampling[Resampling<br/>SMOTE, Undersampling]
        FeatQ -->|Need encoding| Encoding[Encoding<br/>OneHot, Label, Target]
        
        DimRed --> ReadyData
        Sampling --> ReadyData
        Encoding --> ReadyData
        FeatQ -->|Ready| ReadyData[Model-Ready Data]
    end
    
    subgraph Modeling["🤖 Modeling"]
        ReadyData --> ModelChoice{Choose<br/>Algorithm}
        ModelChoice -->|Classification| MLClass[ML Classifiers<br/>See ML flowchart]
        ModelChoice -->|Regression| MLReg[ML Regressors<br/>See ML flowchart]
        ModelChoice -->|Clustering| MLClust[Clustering<br/>K-Means, DBSCAN]
        
        MLClass --> Eval
        MLReg --> Eval
        MLClust --> Eval[Model Evaluation]
    end
    
    subgraph Evaluation["📈 Evaluation & Iteration"]
        Eval --> Metrics{Check<br/>Metrics}
        Metrics -->|Classification| ClassMetrics[Accuracy, F1, ROC-AUC<br/>Confusion Matrix]
        Metrics -->|Regression| RegMetrics[MSE, MAE, R²<br/>Residual plots]
        Metrics -->|Clustering| ClustMetrics[Silhouette, Davies-Bouldin<br/>Calinski-Harabasz]
        
        ClassMetrics --> Good{Good<br/>enough?}
        RegMetrics --> Good
        ClustMetrics --> Good
        
        Good -->|No| Iterate[Iterate:<br/>• Try different algorithms<br/>• Tune hyperparameters<br/>• Engineer more features<br/>• Get more data]
        Good -->|Yes| Deploy[Deploy Model]
        
        Iterate -.->|Back to| FeatureEng
        Iterate -.->|Or back to| Modeling
    end
    
    RawData --> Missing
    
    style RawData fill:#ffcccc
    style CleanData fill:#ccffcc
    style ReadyData fill:#ccffcc
    style Insights fill:#ffffcc
    style Deploy fill:#90EE90
    style Iterate fill:#FFD700
```

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

**How UMAP Works - Visual Explanation**:

![UMAP Algorithm Process](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sZfKPLbFUhG_EfhXDggRBQ.png)
*UMAP (Uniform Manifold Approximation and Projection) constructs a high-dimensional graph representation of the data, then optimizes a low-dimensional graph to be as structurally similar as possible. Unlike t-SNE, UMAP preserves both local and global structure, making it faster and more suitable for general-purpose dimensionality reduction.*
*Image source: [Dimensionality Reduction using UMAP](https://adanayak.medium.com/dimensionality-reduction-using-uniform-manifold-approximation-and-projection-umap-4aa4cef43fed)*

**Approaches**: Matrix-based (linear algebra) vs Graph-based (manifold learning)

| Method | Type | Linear | Preserves | Speed | Best For | Limitations |
|--------|------|--------|-----------|-------|----------|-------------|
| **PCA** | Matrix | Yes | Global variance | Fast | High-dim data, preprocessing | Assumes linearity |
| **t-SNE** | Graph | No | Local structure | Slow | Visualization (2D/3D) | Not for new data, slow |
| **UMAP** | Graph | No | Local + global | Fast | Large datasets, clustering | Hyperparameter sensitive |
| **LDA** | Matrix | Yes | Class separation | Fast | Supervised tasks | Requires labels |
| **ICA** | Matrix | Yes | Independence | Medium | Signal separation | Assumes independence |
| **Isomap** | Graph | No | Geodesic distance | Medium | Non-linear manifolds | Sensitive to noise |
| **LLE** | Graph | No | Local geometry | Medium | Non-linear manifolds | Requires dense sampling |
| **Autoencoder** | Neural | No | Learned features | Medium | Complex patterns | Needs training data |

**Selection Guide**:
- **Visualization**: t-SNE (local focus), UMAP (balanced)
- **Preprocessing**: PCA, ICA
- **Supervised**: LDA
- **Large datasets**: UMAP, PCA
- **Non-linear patterns**: UMAP (fast), Autoencoder (flexible), Kernel PCA
- **Preserve global structure**: UMAP, PCA

### Data Imputation

**Core Concept**: Handling missing values

**Missing Data Patterns**:
- **MCAR** (Missing Completely At Random): Missingness independent of data
- **MAR** (Missing At Random): Missingness depends on observed data
- **MNAR** (Missing Not At Random): Missingness depends on unobserved data

| Method | Type | Complexity | Preserves Distribution | Best For | Limitations |
|--------|------|------------|----------------------|----------|-------------|
| **Mean/Median/Mode** | Simple | Low | No | Quick baseline, MCAR | Reduces variance |
| **Forward/Backward Fill** | Simple | Low | Partial | Time series | Creates autocorrelation |
| **Constant Value** | Simple | Low | No | Domain knowledge | Arbitrary choice |
| **Random Sampling** | Simple | Low | Yes | MCAR data | Ignores relationships |
| **Regression** | Statistical | Medium | Partial | MAR, relationships | Underestimates variance |
| **Stochastic Regression** | Statistical | Medium | Yes | MAR, variance preservation | More complex |
| **KNN** | ML | Medium | Yes | Local patterns | Computationally expensive |
| **MICE** | ML | High | Yes | Multiple variables, MAR | Slow, requires iterations |
| **Matrix Factorization** | ML | High | Yes | High-dimensional, patterns | Needs sufficient data |
| **Deep Learning** | ML | High | Yes | Complex patterns | Requires training data |

**Selection Guide**:
- **Quick analysis**: Mean/Median
- **Time series**: Forward/Backward fill
- **Preserve variance**: Stochastic regression, MICE
- **Complex patterns**: KNN, Deep Learning
- **Multiple variables**: MICE, Matrix Factorization

### Sampling Techniques

| Method | Type | Preserves Distribution | Complexity | Best For | Limitations |
|--------|------|----------------------|------------|----------|-------------|
| **Simple Random** | Probability | No | Low | Homogeneous population | May miss subgroups |
| **Systematic** | Probability | No | Low | Ordered data | Periodic patterns risk |
| **Stratified** | Probability | Yes | Medium | Heterogeneous population | Requires strata knowledge |
| **Cluster** | Probability | Partial | Medium | Geographically dispersed | Higher variance |
| **Bootstrap** | Resampling | Yes | Low | Confidence intervals | Assumes independence |
| **Cross-Validation** | Resampling | Yes | Medium | Model evaluation | Computationally expensive |

**Imbalanced Data Sampling**:

| Technique | Approach | Data Size | Overfitting Risk | Best For | Avoid When |
|-----------|----------|-----------|-----------------|----------|------------|
| **Random Oversampling** | Duplicate minority | Increases | High | Quick baseline | Exact duplicates |
| **SMOTE** | Synthetic minority | Increases | Medium | General purpose | High-dimensional |
| **ADASYN** | Adaptive synthetic | Increases | Medium | Varying density | Noisy data |
| **Random Undersampling** | Remove majority | Decreases | Low | Large datasets | Information loss |
| **Tomek Links** | Remove boundary | Decreases | Low | Clean boundaries | Aggressive removal |
| **SMOTEENN** | SMOTE + ENN | Varies | Low | Noisy boundaries | Complex |
| **SMOTETomek** | SMOTE + Tomek | Varies | Low | Clean synthetic | Two-step process |

### Normalization and Scaling

**Core Concept**: Bringing features to comparable scales

#### Feature Scaling Methods

| Method | Formula | Range | Robust to Outliers | Best For | Avoid When |
|--------|---------|-------|-------------------|----------|------------|
| **Min-Max** | (x - min) / (max - min) | [0, 1] | No | Neural networks, bounded features | Outliers present |
| **Standardization** | (x - μ) / σ | Unbounded | No | Linear models, PCA, clustering | Non-Gaussian data |
| **Robust Scaling** | (x - median) / IQR | Unbounded | Yes | Outliers present | Need specific range |
| **MaxAbs** | x / \|max\| | [-1, 1] | No | Sparse data | Dense data with outliers |
| **L1 Normalization** | x / Σ\|x\| | Sum = 1 | No | Text data, sparse features | Need variance info |
| **L2 Normalization** | x / √(Σx²) | Norm = 1 | No | Cosine similarity, embeddings | Need magnitude info |

#### Distribution Transformations

| Method | Purpose | Handles Negatives | Handles Zeros | Best For | Limitations |
|--------|---------|------------------|---------------|----------|-------------|
| **Log** | Reduce skewness | No | No | Right-skewed data | Requires x > 0 |
| **Box-Cox** | Normalize distribution | No | No | Positive data, find optimal λ | Requires x > 0 |
| **Yeo-Johnson** | Normalize distribution | Yes | Yes | Any data, find optimal λ | More complex |
| **Quantile** | Match target distribution | Yes | Yes | Non-parametric, uniform/normal | Loses outlier info |
| **Power** | Reduce skewness | Depends | Yes | Flexible transformation | Parameter selection |

#### Categorical Encoding

| Method | Output | Cardinality | Preserves Order | Best For | Limitations |
|--------|--------|-------------|----------------|----------|-------------|
| **One-Hot** | Binary columns | High-dim | No | Tree models, low cardinality | Curse of dimensionality |
| **Label** | Integer | Low-dim | No | Tree models only | Implies ordering |
| **Ordinal** | Integer | Low-dim | Yes | Ordered categories | Requires order |
| **Target** | Float | Low-dim | No | High cardinality | Overfitting risk |
| **Binary** | Binary | Medium-dim | No | High cardinality | Less interpretable |
| **Frequency** | Float | Low-dim | No | Rare categories | Loses uniqueness |

**Selection Guide**:
- **Distance-based models** (KNN, SVM): Standardization or Min-Max
- **Tree-based models**: No scaling needed (but encoding required)
- **Neural networks**: Min-Max or Standardization
- **With outliers**: Robust Scaling
- **Sparse data**: MaxAbs, L1 normalization

### Data Augmentation

| Modality | Technique | Preserves Semantics | Complexity | Best For | Risk |
|----------|-----------|-------------------|------------|----------|------|
| **Image** | Geometric transforms | Yes | Low | CV, small datasets | Over-augmentation |
| **Image** | Color jittering | Yes | Low | Lighting variations | Unrealistic colors |
| **Image** | Mixup/CutMix | Partial | Medium | Regularization | Label noise |
| **Image** | AutoAugment | Yes | High | Optimal policy | Expensive search |
| **Text** | Synonym replacement | Yes | Low | Small datasets | Context loss |
| **Text** | Back-translation | Yes | High | Paraphrasing | Translation errors |
| **Text** | Contextual embeddings | Yes | Medium | Semantic variations | Requires LLM |
| **Tabular** | SMOTE | Partial | Medium | Imbalanced data | Unrealistic combinations |
| **Tabular** | Gaussian noise | Partial | Low | Continuous features | Distribution shift |
| **Tabular** | CTGAN | Yes | High | Complex distributions | Training required |
| **Time Series** | Window slicing | Yes | Low | More samples | Temporal correlation |
| **Time Series** | Jittering | Yes | Low | Noise robustness | Signal distortion |
| **Time Series** | Time warping | Yes | Medium | Temporal variations | Pattern distortion |

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
| **L1 (Lasso)** | Feature selection | Yes | O(n) | High-dimensional | May underfit |
| **L2 (Ridge)** | Weight shrinkage | No | O(n) | Multicollinearity | Keeps all features |
| **Elastic Net** | L1 + L2 | Partial | O(n) | Correlated features | Two hyperparameters |
| **Dropout** | Random deactivation | No | O(n) | Neural networks | Training time |
| **Early Stopping** | Stop training | No | O(1) | Any iterative | Validation needed |

#### Model Selection Criteria

| Criterion | Formula | Penalty | Best For | Limitations |
|-----------|---------|---------|----------|-------------|
| **AIC** | 2k - 2ln(L) | 2k | Large samples | Overfits small data |
| **BIC** | k×ln(n) - 2ln(L) | k×ln(n) | Model selection | Penalizes complexity more |
| **MDL** | L(model) + L(data\|model) | Description length | Compression | Computationally complex |
| **Cross-Validation** | Empirical error | None | Robust estimate | Computationally expensive |

**Model Capacity Measures**:
- **VC Dimension**: Maximum points that can be shattered
- **Rademacher Complexity**: Expected supremum of empirical process
- **Parameter Count**: Number of learnable weights
- **Depth vs Width**: Network architecture trade-offs

### Model Explainability

| Method | Scope | Model-Agnostic | Complexity | Best For | Limitations |
|--------|-------|----------------|------------|----------|-------------|
| **Permutation Importance** | Global | Yes | O(n×m) | Any model | Correlated features |
| **Tree Importance** | Global | No | O(1) | Tree models | Biased to high-cardinality |
| **Coefficients** | Global | No | O(1) | Linear models | Requires scaling |
| **SHAP** | Local/Global | Yes | O(2^n) or O(n²) | Consistent values | Computationally expensive |
| **LIME** | Local | Yes | O(k×m) | Simple explanations | Unstable |
| **PDP** | Global | Yes | O(n×m) | Feature effects | Assumes independence |
| **ICE** | Local | Yes | O(n×m) | Individual effects | Many plots |
| **ALE** | Global | Yes | O(n×m) | Correlated features | Complex interpretation |
| **Counterfactuals** | Local | Yes | O(optimization) | Actionable insights | May be unrealistic |

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
| **Demographic Parity** | P(Ŷ=1\|A=0) = P(Ŷ=1\|A=1) | Predictions | Equal selection rates | Ignores ground truth |
| **Equalized Odds** | TPR & FPR equal across groups | Labels | Overall fairness | Strict requirement |
| **Equal Opportunity** | TPR equal across groups | Labels | Positive outcomes | Ignores FPR |
| **Predictive Parity** | PPV equal across groups | Labels | Precision fairness | May allow different TPR |
| **Individual Fairness** | Similar individuals → similar predictions | Similarity metric | Case-by-case | Defining similarity |

#### Bias Mitigation Strategies

| Stage | Technique | Approach | Complexity | Best For | Limitations |
|-------|-----------|----------|------------|----------|-------------|
| **Pre-processing** | Reweighting | Adjust sample weights | Low | Simple fix | Limited impact |
| **Pre-processing** | Resampling | Balance groups | Low | Imbalanced data | Data loss/duplication |
| **In-processing** | Fairness constraints | Regularization | Medium | During training | Model-specific |
| **In-processing** | Adversarial debiasing | GAN-like training | High | Deep learning | Training complexity |
| **Post-processing** | Threshold optimization | Adjust decision boundary | Low | Model-agnostic | May reduce accuracy |
| **Post-processing** | Calibration | Adjust probabilities | Medium | Probabilistic models | Requires validation set |

**Fairness-Accuracy Trade-off**:
- No free lunch: improving fairness often reduces accuracy
- Context matters: legal, ethical, and domain considerations
- Multi-objective optimization: Pareto frontier analysis
- Stakeholder involvement: define acceptable trade-offs

### Evaluation Metrics

#### Classification Metrics

| Metric | Formula | Range | Balanced | Best For | Limitations |
|--------|---------|-------|----------|----------|-------------|
| **Accuracy** | (TP+TN)/(TP+TN+FP+FN) | [0, 1] | No | Balanced classes | Misleading with imbalance |
| **Precision** | TP/(TP+FP) | [0, 1] | No | Minimize false positives | Ignores false negatives |
| **Recall** | TP/(TP+FN) | [0, 1] | No | Minimize false negatives | Ignores false positives |
| **F1-Score** | 2×(P×R)/(P+R) | [0, 1] | Yes | Balance P and R | Equal weight to P/R |
| **F-beta** | (1+β²)×(P×R)/(β²P+R) | [0, 1] | Yes | Custom P/R weight | Parameter selection |
| **ROC-AUC** | Area under ROC curve | [0, 1] | Yes | Threshold-independent | Optimistic with imbalance |
| **PR-AUC** | Area under PR curve | [0, 1] | Yes | Imbalanced data | Less intuitive |
| **MCC** | Correlation coefficient | [-1, 1] | Yes | Imbalanced data | Less known |
| **Cohen's Kappa** | Agreement beyond chance | [-1, 1] | Yes | Inter-rater reliability | Requires interpretation |
| **Log Loss** | -Σ(y×log(p)) | [0, ∞] | Yes | Probability calibration | Sensitive to confidence |

**Multi-class Averaging**:
- **Macro**: Unweighted mean (treats all classes equally)
- **Micro**: Aggregate then compute (favors frequent classes)
- **Weighted**: Weighted by class frequency

#### Regression Metrics

| Metric | Formula | Units | Robust to Outliers | Interpretable | Best For |
|--------|---------|-------|-------------------|---------------|----------|
| **MAE** | Σ\|y-ŷ\|/n | Same as y | Yes | Yes | General purpose |
| **MSE** | Σ(y-ŷ)²/n | Squared | No | No | Penalize large errors |
| **RMSE** | √(Σ(y-ŷ)²/n) | Same as y | No | Yes | Penalize large errors |
| **MAPE** | Σ\|y-ŷ\|/y×100 | Percentage | No | Yes | Relative errors |
| **R²** | 1 - SS_res/SS_tot | [0, 1] | No | Yes | Variance explained |
| **Adjusted R²** | 1 - (1-R²)(n-1)/(n-p-1) | [0, 1] | No | Yes | Penalize complexity |
| **Median AE** | median(\|y-ŷ\|) | Same as y | Yes | Yes | Outliers present |
| **Huber** | Piecewise (L2/L1) | Same as y | Partial | No | Some outliers |
| **Quantile** | Asymmetric L1 | Same as y | Yes | No | Specific quantiles |

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
| **Silhouette** | [-1, 1] | Yes | Cohesion & separation | General purpose | Convex clusters |
| **Davies-Bouldin** | [0, ∞] | No | Cluster similarity | Compact clusters | Euclidean bias |
| **Calinski-Harabasz** | [0, ∞] | Yes | Between/within variance | Dense clusters | Convex clusters |
| **Dunn Index** | [0, ∞] | Yes | Min separation/max diameter | Well-separated | Sensitive to outliers |

**External Metrics** (requires ground truth):

| Metric | Range | Higher is Better | Measures | Properties |
|--------|-------|-----------------|----------|------------|
| **Adjusted Rand Index** | [-1, 1] | Yes | Pair agreement | Chance-corrected |
| **NMI** | [0, 1] | Yes | Mutual information | Normalized |
| **Fowlkes-Mallows** | [0, 1] | Yes | Geometric mean of P/R | Symmetric |
| **Homogeneity** | [0, 1] | Yes | Cluster purity | One-sided |
| **Completeness** | [0, 1] | Yes | Class grouping | One-sided |
| **V-measure** | [0, 1] | Yes | Harmonic mean H/C | Balanced |

## Statistical Analysis

| Category | Method | Type | Key Techniques | Best For |
|----------|--------|------|----------------|----------|
| **Hypothesis Testing** | **Parametric Tests** | Distributional assumptions | t-test, ANOVA, F-test, Z-test | Normal distributions, known parameters |
| | **Non-parametric Tests** | Distribution-free | Mann-Whitney U, Wilcoxon, Kruskal-Wallis, Chi-square, KS test | Non-normal data, ordinal data |
| | **Multiple Testing** | Correction methods | Bonferroni, Holm-Bonferroni, Benjamini-Hochberg (FDR) | Multiple comparisons |
| **Correlation** | **Correlation Analysis** | Relationships | Pearson, Spearman, Kendall's tau, Point-biserial, Partial | Measuring associations |
| **Causation** | **Causal Inference** | Causality | RCT, Observational studies, Propensity score matching, IV, DiD | Establishing cause-effect |

## Data Visualization

| Category | Plot Type | Variables | Key Techniques | Best For |
|----------|-----------|-----------|----------------|----------|
| **Exploratory** | **Univariate Plots** | Single | Histograms, Box plots, Violin plots, Density plots, QQ plots | Distribution analysis |
| | **Bivariate Plots** | Two | Scatter plots, Line plots, Heatmaps, Hexbin plots, Joint plots | Relationships between two variables |
| | **Multivariate Plots** | Multiple | Pair plots, Parallel coordinates, Radar charts, 3D scatter, DR plots | Complex relationships |
| **Statistical** | **Distribution Plots** | Single/Multiple | Empirical CDF, Probability plots, Quantile plots, KDE | Distribution properties |
| | **Comparison Plots** | Groups | Bar charts, Grouped box plots, Strip plots, Swarm plots | Group comparisons |

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