---
title: "Machine Learning"
author: "Yuhan Zhou"
date: "2025-10-10"
---
# Machine Learning

## Supervised Learning (监督学习)

Supervised learning uses labeled data to train models. The algorithm learns from input-output pairs to predict outcomes for new, unseen data.

### Classification

Classification predicts discrete categorical labels (e.g., spam/not spam, cat/dog).

#### KNN (K-Nearest Neighbors)
- Uses distance metrics (usually Euclidean) to find nearest neighbors, prediction is made by majority voting among k neighbors

**Parameters:**
- `k`: Number of neighbors to consider
- Distance metric: Euclidean, Manhattan, Minkowski

#### Logistic Regression

**How it works:**
- Despite the name, used for classification
- Uses sigmoid function to map predictions to probability [0,1]
- Decision boundary: typically 0.5 threshold
- Formula: P(Y=1|X) = 1 / (1 + e^(-z)), where z = β₀ + β₁x₁ + ... + βₙxₙ

**Key Concepts:**
- **Binary classification**: Two classes (0/1)
- **Multiclass**: One-vs-Rest or Softmax regression
- **Cost function**: Log loss (cross-entropy)
- **Optimization**: Gradient descent

**Pros:**
- Provides probability scores
- Efficient to train
- Less prone to overfitting with regularization
- Interpretable coefficients

**Cons:**
- Assumes linear relationship between features and log-odds
- Limited to linear decision boundaries (unless feature engineering applied)

#### Decision Trees

##### Bagging vs. Boosting
**How it works:**
- Tree-like model where each node represents a feature test
- Splits data based on information gain or Gini impurity
- Leaf nodes represent class labels

**Key Parameters:**
- Max depth, min samples split, min samples leaf
- Splitting criterion: Gini, entropy

**Pros:**
- Easy to interpret and visualize
- Handles non-linear relationships
- No feature scaling needed

**Cons:**
- Prone to overfitting
- Unstable (small data changes cause different trees)

#### Random Forest

**How it works:**
- Ensemble of decision trees trained on random subsets
- Bootstrap aggregating (bagging)
- Final prediction: majority vote

**Pros:**
- Reduces overfitting compared to single tree
- Feature importance ranking
- Handles missing values well

**Industry Use Cases:**
- Fraud detection
- Credit scoring
- Stock market prediction

#### Boosting trees
##### XGBoost
##### light GBM

### Support Vector Machines (SVM)

**How it works:**
- Finds optimal hyperplane that maximizes margin between classes
- Uses kernel trick for non-linear boundaries
- Support vectors: data points closest to decision boundary

**Key Concepts:**
- **Kernels**: Linear, polynomial, RBF (radial basis function)
- **C parameter**: Regularization (tradeoff between margin and misclassification)
- **Gamma**: Kernel coefficient (how far influence of single training example reaches)

**Pros:**
- Effective in high-dimensional spaces
- Memory efficient (only uses support vectors)
- Versatile with different kernels

**Cons:**
- Slow for large datasets
- Sensitive to parameter tuning
- No probability estimates (without additional calibration)

**Industry Use Cases:**
- Text classification
- Image recognition
- Bioinformatics

### Evaluation Metrics

#### Confusion Matrix
```
                Predicted
              Positive | Negative
Actual  Pos      TP    |    FN
        Neg      FP    |    TN
```

#### Precision (精确率)

**Formula:** Precision = TP / (TP + FP)

**Meaning:** Of all positive predictions, how many were actually correct?

**When to use:** When false positives are costly (e.g., spam detection - don't want legitimate emails marked as spam)

#### Recall (召回率 / Sensitivity)

**Formula:** Recall = TP / (TP + FN)

**Meaning:** Of all actual positives, how many did we correctly identify?

**When to use:** When false negatives are costly (e.g., disease detection - don't want to miss actual cases)

#### F1 Score

**Unweighted (Standard) F1:**
- Formula: F1 = 2 × (Precision × Recall) / (Precision + Recall)
- Harmonic mean of precision and recall
- Use when you need balance between precision and recall

**Weighted F1 (Fβ Score):**
- Formula: Fβ = (1 + β²) × (Precision × Recall) / (β² × Precision + Recall)
- β > 1: Favors recall
- β < 1: Favors precision
- F2 score: Weights recall 2x more than precision

**Industry Application:**
- Imbalanced datasets
- When you need single metric to optimize

#### ROC Curve (Receiver Operating Characteristic)

**What it shows:**
- Plots True Positive Rate (Recall) vs False Positive Rate
- FPR = FP / (FP + TN)
- Each point represents different classification threshold

**AUC (Area Under Curve):**
- AUC = 1.0: Perfect classifier
- AUC = 0.5: Random guessing
- AUC < 0.5: Worse than random

**When to use:**
- Comparing multiple models
- Evaluating model across all thresholds
- When class distribution might change in production

**Industry Use:**
- Medical diagnostics (balancing sensitivity and specificity)
- Fraud detection (adjusting threshold based on risk tolerance)

#### Accuracy

**Formula:** Accuracy = (TP + TN) / Total

**Limitation:** Misleading for imbalanced datasets
- Example: 95% of emails are not spam; always predicting "not spam" gives 95% accuracy but is useless

#### Cross-Validation

**K-Fold Cross-Validation:**
- Split data into k folds
- Train on k-1 folds, validate on remaining fold
- Repeat k times, average results

**Stratified K-Fold:**
- Maintains class distribution in each fold
- Critical for imbalanced datasets

**Pros:**
- Better estimate of model performance
- Uses all data for training and validation
- Reduces overfitting to validation set

### Regression

Regression predicts continuous numerical values (e.g., house prices, temperature).

#### Linear Regression

**Formula:** y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε

**Key Concepts:**
- Minimizes sum of squared residuals (least squares)
- Assumptions: linearity, independence, homoscedasticity, normality of errors

**Evaluation Metrics:**
- **R² (R-squared)**: Proportion of variance explained (0-1, higher is better)
- **MSE (Mean Squared Error)**: Average squared difference
- **RMSE (Root Mean Squared Error)**: Square root of MSE (same units as target)
- **MAE (Mean Absolute Error)**: Average absolute difference (robust to outliers)

#### KNN for Regression

**How it works:**
- Same neighbor-finding as classification
- Prediction: average (or weighted average) of k nearest neighbors' values

**When to use:**
- Non-linear relationships
- Small to medium datasets
- When local patterns matter

**Example:** Predicting house prices based on similar houses in neighborhood

#### Polynomial Regression

**Concept:** Creates polynomial features to model non-linear relationships

**Example:** y = β₀ + β₁x + β₂x² + β₃x³

**Warning:** Higher degrees can lead to overfitting

#### Ridge Regression (L2 Regularization)

**Formula:** Cost = MSE + α × Σ(βᵢ²)

**Effect:** Shrinks coefficients, prevents large weights

**When to use:** Multicollinearity, many features

#### Lasso Regression (L1 Regularization)

**Formula:** Cost = MSE + α × Σ|βᵢ|

**Effect:** Can shrink coefficients to exactly zero (feature selection)

**When to use:** High-dimensional data, feature selection needed

## Unsupervised Learning (非监督学习)

Learning patterns from unlabeled data without predefined outcomes.

### Clustering

Grouping similar data points together.

#### K-Means Clustering

**Algorithm:**
1. Initialize k random centroids
2. Assign each point to nearest centroid
3. Recalculate centroids as mean of assigned points
4. Repeat until convergence

**Key Parameter:**
- k: Number of clusters (use elbow method or silhouette score to determine)

**Pros:**
- Simple and fast
- Scalable to large datasets

**Cons:**
- Must specify k beforehand
- Sensitive to initial centroid placement
- Assumes spherical clusters

**Industry Use Cases:**
- Customer segmentation
- Document clustering
- Image compression

#### Hierarchical Clustering

**Types:**
- **Agglomerative**: Bottom-up (merge clusters)
- **Divisive**: Top-down (split clusters)

**Linkage Methods:**
- Single: Minimum distance between points
- Complete: Maximum distance
- Average: Average distance
- Ward: Minimizes within-cluster variance

**Pros:**
- No need to specify k
- Produces dendrogram (visual hierarchy)

**Cons:**
- Computationally expensive for large datasets
- Difficult to reverse decisions

#### DBSCAN (Density-Based Clustering)

**How it works:**
- Groups points that are closely packed
- Marks outliers as noise

**Parameters:**
- eps: Maximum distance between points in same cluster
- min_samples: Minimum points to form dense region

**Pros:**
- Automatically determines number of clusters
- Can find arbitrarily shaped clusters
- Robust to outliers

**Industry Use Cases:**
- Anomaly detection
- Geospatial data analysis

#### Evaluation

##### Silhouette Score

**Formula:** s(i) = (b(i) - a(i)) / max(a(i), b(i))

- a(i): Average distance to points in same cluster
- b(i): Average distance to points in nearest other cluster
- Range: [-1, 1], higher is better
- > 0.5: Good clustering

**When to use:** Comparing different k values or algorithms

##### Elbow Method

**Process:**
- Plot within-cluster sum of squares (WCSS) vs k
- Look for "elbow" where improvement diminishes

**Limitation:** Elbow not always clear

##### Davies-Bouldin Index

- Lower is better
- Measures average similarity between clusters
- Good for comparing clustering algorithms

### Dimensionality Reduction

#### PCA (Principal Component Analysis)

**How it works:**
- Finds orthogonal directions of maximum variance
- Projects data onto lower-dimensional space
- Components are ranked by explained variance

**Key Concepts:**
- **Eigenvectors**: Directions of principal components
- **Eigenvalues**: Amount of variance along each component
- **Cumulative explained variance**: Choose components that explain 95%+ variance

**Pros:**
- Reduces computational cost
- Helps visualization (2D/3D)
- Removes noise and multicollinearity

**Cons:**
- Linear transformation only
- Components not always interpretable
- Sensitive to scaling (must standardize features)

**Industry Use Cases:**
- Image compression
- Feature extraction for deep learning
- Exploratory data analysis

#### t-SNE (t-Distributed Stochastic Neighbor Embedding)

**Purpose:** Visualization of high-dimensional data

**Pros:**
- Preserves local structure well
- Excellent for visualization

**Cons:**
- Computationally expensive
- Results vary with random seed
- Not for feature reduction (only visualization)

### Neural Networks

#### Basics

**Architecture:**
- **Input layer**: Receives features
- **Hidden layers**: Learn representations
- **Output layer**: Produces predictions

**Activation Functions:**
- **ReLU**: f(x) = max(0, x) - Most common for hidden layers
- **Sigmoid**: f(x) = 1/(1+e^(-x)) - Binary classification output
- **Softmax**: Multi-class classification output
- **Tanh**: f(x) = (e^x - e^(-x))/(e^x + e^(-x)) - Alternative to sigmoid

**Training:**
- **Forward propagation**: Calculate predictions
- **Loss function**: Measures error
- **Backpropagation**: Calculate gradients
- **Gradient descent**: Update weights

**Key Concepts:**
- **Learning rate**: Step size for weight updates
- **Batch size**: Number of samples per update
- **Epochs**: Full passes through training data

#### Convolutional Neural Networks (CNNs)

**Use case:** Image and spatial data

**Key layers:**
- Convolutional layers: Learn spatial features
- Pooling layers: Reduce dimensions
- Fully connected layers: Classification

#### Recurrent Neural Networks (RNNs)

**Use case:** Sequential data (text, time series)

**Variants:**
- **LSTM** (Long Short-Term Memory): Handles long-term dependencies
- **GRU** (Gated Recurrent Unit): Simpler than LSTM

## Overfitting (过拟合)

**Definition:** Model learns training data too well, including noise, and performs poorly on new data.

**Symptoms:**
- High training accuracy, low test accuracy
- Large gap between training and validation loss
- Model too complex for available data

**Causes:**
- Too many features/parameters
- Too little training data
- Training too long
- No regularization

**Solutions:**

1. **More Data**: Collect additional training samples
2. **Regularization**:
   - L1 (Lasso): Adds Σ|w| penalty
   - L2 (Ridge): Adds Σw² penalty
   - Dropout (Neural networks): Randomly disable neurons during training
3. **Cross-Validation**: Detect overfitting early
4. **Reduce Model Complexity**:
   - Fewer features
   - Shallower trees
   - Fewer layers/neurons
5. **Early Stopping**: Stop training when validation error increases
6. **Ensemble Methods**: Combine multiple models
7. **Data Augmentation**: Create variations of training data (images)

**Example:**
```
Training accuracy: 99%
Test accuracy: 65%
→ Overfitting!
```

## Underfitting (欠拟合)

**Definition:** Model is too simple to capture underlying patterns in data.

**Symptoms:**
- Low training accuracy
- Low test accuracy
- High bias

**Causes:**
- Model too simple
- Too few features
- Too much regularization
- Insufficient training

**Solutions:**

1. **Increase Model Complexity**:
   - Add more features
   - Use polynomial features
   - Deeper trees
   - More layers/neurons
2. **Reduce Regularization**: Lower α parameter
3. **Train Longer**: More epochs
4. **Feature Engineering**: Create meaningful derived features
5. **Try Different Algorithms**: Switch to more flexible model

**Example:**
```
Training accuracy: 60%
Test accuracy: 58%
→ Underfitting!
```

## Bias-Variance Tradeoff

**Bias:** Error from overly simplistic assumptions
- High bias → Underfitting

**Variance:** Error from sensitivity to training data fluctuations
- High variance → Overfitting

**Goal:** Find sweet spot where total error is minimized

```
Total Error = Bias² + Variance + Irreducible Error
```

**Typical Pattern:**
- Simple models: High bias, low variance
- Complex models: Low bias, high variance

## Feature Engineering

**Critical for Industry Success:**

1. **Feature Scaling**:
   - **Standardization**: (x - mean) / std (for algorithms sensitive to scale)
   - **Normalization**: (x - min) / (max - min) (scales to [0,1])

2. **Handling Missing Data**:
   - Remove rows/columns
   - Imputation (mean, median, mode, KNN)
   - Add indicator feature for missingness

3. **Encoding Categorical Variables**:
   - **One-Hot Encoding**: Create binary columns
   - **Label Encoding**: Assign integers (for ordinal data)
   - **Target Encoding**: Replace with target mean

4. **Feature Creation**:
   - Polynomial features
   - Interaction terms
   - Domain-specific features

5. **Feature Selection**:
   - **Filter methods**: Correlation, chi-square
   - **Wrapper methods**: Forward/backward selection
   - **Embedded methods**: Lasso, tree-based importance

## Model Selection & Deployment

**Train-Validation-Test Split:**
- Training: 60-70% (fit model)
- Validation: 15-20% (tune hyperparameters)
- Test: 15-20% (final evaluation, never touch until end)

**Hyperparameter Tuning:**
- **Grid Search**: Exhaustive search over parameter grid
- **Random Search**: Random sampling from parameter distributions
- **Bayesian Optimization**: Smart search based on previous results

**Industry Best Practices:**
1. Always use separate test set
2. Monitor model performance over time (drift detection)
3. A/B testing for new models
4. Version control for models and data
5. Document assumptions and limitations
6. Consider interpretability for stakeholder buy-in