# Estimation
- Sampling Error
 - Error due to measuring only part of the population.  
 - Sampling distribution account for sampling error.  
 - `Confidence intervals(CI)` and `Standards Errors(SE)` quantify sampling error.
- Sampling Bias
- Measurement Error
# Hypothesis
## Test Proportions (frequencies)
### Basic
Determine whether there is a significant difference between the expected frequencies and the observed frequencies in one or more categories.  
### Test statistic  
total deviation
```python
test_stat = sum(abs(observed - expected))
```
chi-squared statistic
```python
test_stat = sum((observed - expected)**2 / expected)
```