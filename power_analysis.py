from statsmodels.stats.power import FTestAnovaPower

power_analysis = FTestAnovaPower()
sample_size_per_group = power_analysis.solve_power(effect_size=0.2, alpha=0.05, power=0.8, k_groups=4)  # Calculate the required sample size per group using ANOVA power analysis
total_sample_size = sample_size_per_group * 4

print("Sample Size per Group:", sample_size_per_group)
print("Total Sample Size:", total_sample_size)