### Election Prediction Hackathon Project
McKenzie Skrastins, Kristina Donders, & Batia Rabin

A presentation outlining our approach can be found here: https://docs.google.com/presentation/d/1c9dIvLE3F2Mx3Tn9X3jVn3NBVLQeT1evCX8y_jj8QjI/edit?slide=id.g3a3b4775ea9_0_0#slide=id.g3a3b4775ea9_0_0

This project was awarded Best Data Project at the hackathon!

Overview:
This repository contains the code and materials for a project developed during the Binghamton Codes! X DiDa Mini Hackathon. The goal was to answer the question:
Can we predict which candidate received the majority of votes in each U.S. county for the 2024 election using county-level election data from 2000–2020?

### Approach
1. Data Cleaning & Preprocessing
Compiled and cleaned county-level election returns from 2000–2024
Applied one-hot encoding to prepare categorical variables for modeling
Performed dimensionality reduction using PCA to remove redundant features

2. Modeling
We trained and evaluated two machine learning models:
Logistic Regression
Random Forest Classifier

3. Evaluation Metrics
Model performance was assessed using:
- Accuracy
- Precision–Recall Curve
- ROC Curve

### Results
Our models successfully predicted which candidate received the majority vote in 2024 counties.

### Acknowledgments
Special thanks to: Gregory Hallenbeck, Melissa Haller, Chelsea Gibson, and Maxim Pekarsky for their guidance and support.
