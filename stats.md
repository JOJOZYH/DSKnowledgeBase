# Probability Theory

## Combinatorial Analysis (组合分析)

### Permutations (排列):

Order does matter

- how many ways can we permute(排列) $k$ items from a set of $n$ items (**Order does matter**)? e.g.: choosing 2 items from $\{a, b, c\} \implies \{(ab), (ac), (ba), (bc), (ca), (cb)\}$

- $\frac{n!}{(n-k)!}$

- $\text{If } n=k,\ \text{then }(n-k)! = 0! = 1 \implies \frac{n!}{(n-k)!} = n!$
  
  ### Combinations (组合)
  
  Order doesn't matter

- **binomial coefficient**: How many ways can we choose $k$ items from a set of $n$ items (**order doesn't matter**)?
  
  - $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ $k <= n$

- **multinomial coefficient**: How many ways can we arrange $n$ items into $m$ groups of sizes $k_1, k_2, k_3, \cdots$ and $k_m$?
  
  - $\binom{n}{k_1, k_2, ..., k_m} = \frac{n!}{k_1! \times k_2! \times ... \times k_m!}$ where $k_1 + k_2 + ... + k_m = n$
  - **Example**: Arranging 6 letters {a, b, c, d, e, f} into groups of sizes 2, 3, and 1:
    - $\binom{6}{2, 3, 1} = \frac{6!}{2! \times 3! \times 1!} = \frac{720}{12} = 60$ ways

## Axioms of probability

The **axioms of probability** (Kolmogorov axioms) are three fundamental rules that define a valid probability measure:

1. **Non-negativity**: For any event $A$, $P(A) \geq 0$
2. **Normalization**: The probability of the entire sample space $S$ is $P(S) = 1$
3. **Additivity**: For mutually exclusive events $A$ and $B$ (i.e., $A \cap B = \emptyset$), $P(A \cup B) = P(A) + P(B)$
   - Extended: if $A_1, A_2, \ldots$ are pairwise disjoint, then $P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$

## Conditional Probability & Independence

## Chebyshev's Inequality

## Weak law of Large Numbers

## Central Limit Theorem

## Transformation

# Statistical Inference
## **Hypothesis Testing**
### Key Concepts

- Definition: Statistical method used to make inferences about a population based on sample data
  - 通过分析样本来推断总体(Population)效果的统计学方法
- Null Hypothesis (零假设): Statement of no effect or no difference (status quo)
  - 没效果
  - $H_0$
- Alternative Hypothesis (备择假设): Statement that contradicts H₀ 
  - 有效果
  - $H_1$ or $H_a$
- Type I Error ($\alpha$): Rejecting $H_0$ when it's true (false positive) 
  - $P(\text{reject } H_0 \mid H_0 \text{ true})$
- Type II Error ($\beta$): Failing to reject $H_0$ when it's false (false negative)
  - $P(\text{doesn't reject } H_0 \mid H_0 \text{ false})$
- Statistical Power(统计功效): 1-β, probability of correctly rejecting false H₀
  - Relation to ML concept Recall
    - Assume rejecting false $H₀$ $\equiv$ classifing true positives (TP) rejecting true  $\implies$ $P(\text{correctly rejecting false }H_0)$$\iff$ $\frac{\text{TP}}{\text{TP + FN}}$
- p-value: Probability of observing results at least as extreme as the test statistic under H₀

### Testing Procedure

- Define hypotheses (H₀ and H₁)
- Choose significance level (α), typically 0.05
- Select appropriate test statistic (检验统计量)
- Collect data and calculate test statistic
- Determine p-value
- Make decision: reject H₀ if p-value < α

### GLRT (Generalized Likelihood Ratio Test)

- **Definition**: A general framework for constructing hypothesis tests by comparing likelihoods
- **Test Statistic**: $\Lambda = \frac{\max_{\theta \in \Theta_0} L(\theta | data)}{\max_{\theta \in \Theta} L(\theta | data)}$ or $-2\log(\Lambda)$
  - Numerator: Maximum likelihood under H₀ (restricted parameter space)
  - Denominator: Maximum likelihood under H₁ (unrestricted parameter space)
- **Decision Rule**: Reject H₀ if λ is too small (or -2log(λ) is too large)

#### Common Tests

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

## **A/B Test**

- **Definition**: Experiment comparing two versions (A=control, B=variant) to determine which performs better
- **Applications**: Website design, marketing campaigns, product features, pricing strategies

#### A/B Test Process

### Core Components
1. Distribution Assumptions 
2. Hypotheses (假设)

3. **Formulation**:
   - Define clear metric(s) of success (conversion rate, click-through rate, etc.)
   - H₀: No difference between variants (μA = μB)
   - H₁: There is a difference (μA ≠ μB) or directional (μA < μB)

4. **Design**:
   - Determine required sample size based on:
     - Minimum detectable effect (MDE)
     - Statistical power (typically 0.8)
     - Significance level (typically 0.05)
   - Random assignment of users/subjects to groups

5. **Execution**:
   - Run test until required sample size is reached
   - Ensure no interference between groups (A/B isolation)

6. **Analysis**:
   - Calculate test statistic (typically z-test or t-test)
   - Check for statistical significance
   - Consider practical significance (effect size)

#### Common Pitfalls

- Stopping test too early ("peeking")
- Multiple testing problem
- Insufficient sample size
- Seasonality effects
- Improper randomization
- Simpson's paradox

#### Advanced Techniques

- Multivariate testing (A/B/n tests)
- Bayesian A/B testing
- Multi-armed bandit algorithms
- Sequential testing

# Baysian Inference

Statistical Inference
├── Frequentist Inference
│   ├── Hypothesis Testing (includes GLRT, t-test, etc.)
│   ├── Confidence Intervals
│   └── Point Estimation (MLE, etc.)
└── Bayesian Inference
    ├── Posterior Distributions
    ├── Credible Intervals
    └── Bayesian Decision Theory
