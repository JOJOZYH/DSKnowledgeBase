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
