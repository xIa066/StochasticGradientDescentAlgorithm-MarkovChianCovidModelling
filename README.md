# StochasticGradientDescentAlgorithm - MarkovChianCovidModelling

COMP90005 Advanced Computing Study

# Motivation
This project considers the setting of a pandemic outbreak. During this outbreak, it is assumed there are a set of parameters, θ, that can be controlled by public policy. The vision of this project is to give the policymakers at any time, sets of optimal parameters θ<sup>*</sup>, so that the public health risks can be reduced as small as possible.

The question is hence raised to what extent should we mitigate the pandemics? Intuitively, we would like to give θ<sup>*</sup> such that it will achieve the virus-free outcome. However, under the assumptions, nudging θ towards such θ<sup>*</sup> by implementing policy has increasing cost, meaning that such θ<sup>*</sup> will potentially impose infeasible government expenses.

Due to this cost constraint, we introduce the hospital capacity as the mitigation threshold for
choosing such θ <sup>*</sup>. In contrast to the virus-free outcome, this not only makes sure the pandemics are well contained and managed under the healthcare capacity, but ultimately, as the motivation of this project, achieving the lowest government expenses.

We proposed two stochastic gradient descent algorithms as the solvers for our models and show the theoretical convergence, lastly, the experiment result shows that two methods of the algorithms with different initial conditions, the value of the optimal parameter were similar, with constructed CIs being relatively narrow, even for a small sample size. Although the differences were small, it is possible that in reality, these small differences could represent large differences in the costs incurred by implementing certain policy

# Report Outline
1. Introduction
2. Problem forumation
3. Methodology and Convergence Analysis
4. Other Discussion
5. Experimental Results
6. Conclusion
