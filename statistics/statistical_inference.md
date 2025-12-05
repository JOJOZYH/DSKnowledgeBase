---
title: Statistics
Author: Yuhan Zhou
Date: 10-09-2025
Purpose: To keep a record of my statistical knowledge
---
# Statistical Inference

## Frequentist vs. Bayesian

**Frequentist** and **Bayesian** are two fundamental paradigms in statistical inference, differing in how they treat parameters and interpret probability:

- **Frequentist Approach**: Treats parameters as **fixed but unknown constants**. Probability statements refer to the long-run frequency of data. Uses methods like MLE for estimation, confidence intervals for uncertainty quantification, and p-values for hypothesis testing. Interpretation: "In 95% of repeated experiments, the interval will contain the true parameter."

- **Bayesian Approach**: Treats parameters as **random variables** with probability distributions. Combines prior beliefs with observed data using Bayes' theorem to obtain posterior distributions. Uses MAP for point estimation, credible intervals for uncertainty, and Bayes factors for hypothesis testing. Interpretation: "There is a 95% probability that the parameter lies in this interval."

Both paradigms address the same statistical tasks (estimation, hypothesis testing, prediction) but through fundamentally different philosophical frameworks. Most classical methods in these notes follow the Frequentist approach.

---

## Estimation  

### MLE (Frequentist Estimation)

### MAP (Baysian Estimation)

---

## **Hypothesis Testing**

### Key Concepts

- **Definition**: Statistical method used to make inferences about a population based on sample data
  - 通过分析样本来推断总体(Population)效果的统计学方法
- **Null Hypothesis (零假设)**: Statement of no effect or no difference (status quo)
  - 没效果
  - $H_0$
- **Alternative Hypothesis (备择假设)**: Statement that contradicts H₀ 
  - 有效果
  - $H_1$ or $H_a$
- **Type I Error**: $\text{reject } H_0 \mid H_0 \text{ true}$
  - Rejecting $H_0$ when it's true (false positive) 
  - **Alpha**: $\alpha$ = $P(\text{Type I Error}) = P(\text{reject } H_0 \mid H_0 \text{ true})$ 
- **Level of Significance**
  - The threshold of the test, so we reject when we observe a test result more extreme than this threshold, in other words, determine what is considered 'rare' under the **null hypothesis**, and reject it when seeing a result that is rarer. which make this threshold equivalent to  **Type I Error**
- **Type II Error**: $\text{fail to reject } H_0 \mid H_0 \text{ false}$
  - Failing to reject $H_0$ when it's false (false negative)
  - **Beta**: $\beta = P(\text{Type II Error}) = P(\text{fail to reject } H_0 \mid H_0 \text{ false})$
- **Statistical Power(统计功效)**: probability of correctly rejecting false H₀ = $1-\beta$
  - Relating to ML concept Recall
    - Rejecting false $H₀$ $\equiv$ classifing true positives (TP)$\implies$ $P(\text{rejecting }H_0 \mid H_0 \text{ false}) \equiv \frac{\text{TP}}{\text{TP + FN}}$
- **Test Statistic (检验统计量)**: $T$
  - function of the data $T(X_1,\cdots,X_n) \in \mathbb{R}$ whose distribution under $H_0$ can be derived/known, is itself a **random variable (随机变量)**
- **Critical value (临界值)**: $c_\alpha$
  - The threshold dervied from the distribtution of $T$ under $H_0$ ($f_{T}$)
  - $$
    \text{Reject } H_0
    \begin{cases}
    \text{if } T > c_\alpha \quad & \text{(right-tailed)} \\
    \text{if } T < c_\alpha \quad & \text{(left-tailed)} \\
    \text{if } |T| > c_{\alpha/2} \quad & \text{(two-tailed)}
    \end{cases}
    $$
- **Observed test statistic: $t_{obs}$**
  - The observed T using the given data, this is a **constant**
- **p-value**: $p$
  - Probability of observing results at least as extreme as the test statistic under $H_0$
  - $$
    p =
    \begin{cases}
    P_{H_0}(T > t_{obs}) \quad \text{for right-tailed test} \\
    P_{H_0}(T < t_{obs}) \quad \text{for left-tailed test} \\
    P_{H_0}(|T| > {t_{obs}/2}) \quad \text{for two-tailed test} \\
    \end{cases}
    $$

### Testing Procedure

1. Define hypotheses (H₀ and H₁)
2. Choose significance level (α), typically 0.05
3. Select appropriate test statistic base on hypotheses
4. Collect data and calculate observed test statistic $t_{obs}$
5. Make decision
   - Critical Value Approach
     1. Calculate critical value $c_\alpha$ from $T$ under $H_0$ base on $\alpha$ and hypotheses
     2. Reject $H_0$ if $t_{obs}$ falls in the rejection region
     - **You don't calculate p-value**
   - P-value Approach
     1. Calculate p-val $p$ from $T$ under $H_0$ base on your hypotheses 
     2. Reject $H_0$ if $p \lt \alpha$
     - **You don't need critical values**

### Multiple Testing and Corrections
- blank

---

### Likelihood Ratio Tests (Frequentists' Hypothesis tests)

#### 1. Likelihood Explained

#### 2. LRT (Likelihood Ratio Test)

#### 3. GLRT (Generalized Likelihood Ratio Test)

- **Definition**: A general framework for constructing hypothesis tests by comparing likelihoods
- **Test Statistic**: $\Lambda = \frac{\max_{\theta \in \Theta_0} L(\theta | data)}{\max_{\theta \in \Theta} L(\theta | data)}$ or $-2\log(\Lambda)$
  - Numerator: Maximum likelihood under H₀ (restricted parameter space)
  - Denominator: Maximum likelihood under H₁ (unrestricted parameter space)
- **Decision Rule**: Reject H₀ if λ is too small (or -2log(λ) is too large)

Many classical tests are **special cases** of GLRT:

- **Z-test**: GLRT for normal distribution with known variance
- **t-test**: GLRT for normal distribution with unknown variance
- **F-test (ANOVA)**: GLRT for comparing variances or means across groups
- **Chi-Square test**: GLRT for categorical data (goodness-of-fit, independence)
- **Wald test**: Approximation to GLRT using Taylor expansion
- **Score test (Lagrange Multiplier)**: Alternative to GLRT, uses gradient of likelihood

**Key Properties:**
- Asymptotically optimal (most powerful for large samples)
- Test statistic -2log(λ) follows χ² distribution asymptotically
- Degrees of freedom = difference in number of parameters between H₁ and H₀

## Bayesian Inference

## Statistical Pitfalls & Biases

### Simpson's Paradox
- **Definition**: A phenomenon where a trend appears in several different groups of data but disappears or reverses when these groups are combined.

### Confounding Variables
- **Definition**: A confounding variable is an external influence that affects both the independent variable

### Multiple Testing problem
- **Definition**: When multiple hypotheses are tested simultaneously, the chance of incorrectly rejecting at least

