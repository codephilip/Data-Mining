# CSCI-347-Data-Mining

## Philip Gehde, Moiyad Alfawwar
## Part 1: Introduction to Dataset
For our Project 1, we choose the Statlog data set, which is a database for heart disease. This dataset has been cited in several research papers in the datascience field including: Diversity in Neural Network Ensembles (Gavin Brown. The University of Birmingham. 2004.), Overcoming the Myopia of Inductive Learning Algorithms with RELIEFF (Igor Kononenko and Edvard Simec and Marko Robnik-Sikonja), Unanimous Voting using Support Vector Machines (Elena Smirnova and Ida G. Sprinkhuizen-Kuyper and I. Nalbantis and b. ERIM and Universiteit Rotterdam, IKAT, Universiteit Maastricht), Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften.

The dataset was uploaded by the University of California, Irvine, and is available at the UCI machine learning archive on their website for the Center for Machine Learning and Intelligent Systems at the following URL: https://archive.ics.uci.edu/ml/datasets/statlog+(heart)

The Statlog dataset has 270 instances, with no missing values and 13 different attributes. Due to the fact that there are no missing values, there is no need for a plot to summarize the proportion of missing data as this is non-applicable for all 13 attributes.

The 13 attributes (which have been extracted from a larger set of 75) include descriptive variables such as sex, and Chest pain type (4 values), however, these values were already label encoded. As such, we are left with the following attribute types: Real: 1,4,5,8,10,12 Ordered:11, Binary: 2,6,9 Nominal:7,3,13

Given that the categorical values were already label encoded, the choice (label-encoded vs one-hot-encoded) was made for us and we assume that the alphabetical ordering of label encoding will not prevent us from making medically relevant inferences from this data. In other words, we assume that the categorical value was ordered alphebetically as to represent the severity of the pain, for example, A-D. This assumption may give us trouble down the road, and should be further investigated.

If we were to work with categorical values for chest pain, one might suggest one-hot encoding as to prevent any issues that may arise if there is no obvious ordering, or ranking of our values, and rather solve this potential problem by represented each category as a binary vector. However, in order to avoid the pitfalls of multicollierity, it would be best to simply determine that categorical data is ranked appropriately and use label-encoding instead. Sex/Gender is binary, and so label-encoding can be considered appropriate.

This dataset is fascinating to work with because of the potential for machine learning and neural networks to be applied in medical diagnostic work. My father had some heart issues recently, that could have been avoided/treated appropriately if the data had been interpreted by a machine, and not a doctor who was later repeatedly sued succesfully for negligent practice. My girlfriend, who is a nurse, reports routinely on poor diagnostic work by colleagues (don't tell anybody). A large proportion of her work day is spent collecting and documenting data, and therein lies the real challenge. How do we gather the appropriate data for the correct diagnosis, to establish better preventative care, and better diagnostics in medicine with the help of machine learning? I believe this question to be a fundamental one in data mining. As good staticians, we have to evaluate the quality and potential biases of the data being used, determining what data is useful, how to gather it, and how to clean it.

Medical Diagnostic work is a highly complex analysis, because we are evaluating a system that is highly complex. It is difficult to establish causation in such systems but we are rather working in the realm of probabilities, where computers can shine. Our 13 attributes have been extracted from 75, which leads me to believe that we are working with a very clean data set. Given the complex nature of the human body I believe that none of them should be ommited. The attributes are listed below, and they all seem highly relevant to the diagnostic work ahead.

1. age
2. sex
3. chest pain type (4 values)
4. resting blood pressure
5. serum cholestoral in mg/dl
6. fasting blood sugar > 120 mg/dl
7. resting electrocardiographic results (values 0,1,2)
8. maximum heart rate achieved
9. exercise induced angina
10. oldpeak = ST depression induced by exercise relative to rest
11. the slope of the peak exercise ST segment
12. number of major vessels (0-3) colored by flourosopy
13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
