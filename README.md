**Project Description with Goals**
-- Construct an ML Regression model that predicts propery tax assessed values of **Single Family Properties** properties.
-- Find the key drivers of property value for single family properties.
-- Deliver a report that the data science team can read through and replicate, understand what steps were taken, why and what the outcome was.
-- Make recommendations on what works or doesn't work in predicting these homes' values.

**Project Planning**
-- set up README.md file
-- SQL query to filter data
-- write functions to acquire and prepare data in acquire_zillow.py file
-- develop hypothesis
-- visalize univariate data
-- stats testing to calculate correlation coefficients and p-values
-- scale data
-- feature ranking
-- establish baseline for regression modeling
-- fit regression models (OLS, LassoLars)
-- plot residuals for each model
-- choose best-performing regression model
   
**Initial Hypothesis**
-- The number of bathrooms and bedrooms and square footage can be used to create a regression model that outperforms the
    baseline model.

**Key Questions:**
-- Which feature(s) have the strongest impact -- (e.g. square footage, number of bedrooms or number of bathrooms)?
-- Which regression model(s) can be deployed to improve predictive accuracy over the baseline?

**Key Findings** 
-- Square feet has the highest correlation to home value. It also has a stronger correlation to other home features (i.e. number of bedrooms and bathrooms) than they do to each other.
-- Ordinary Least Squares (OLS) performs better than both Baseline and LassoLars regression models for predicting property tax assessed values.

**Next Steps**
-- Additional modeling (TweedieRegression, Polynomial Regression) to test for further predictive improvements.

**Recommendations**
-- Deploy OLS regression model to predict property tax assessed values.
