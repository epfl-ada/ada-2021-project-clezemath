# Firearms Debate in the US and its Relation to Mass Shootings


 ## Data Story 
 
 Link to our data story : https://margauxlep.github.io/project-clezemath/

### Abstract:
Gun control is one of the most controversial political topics in the United States. America being one of the world’s most liberal countries in the world, freedom is central amongst its values. But some could say: “My freedom stops when that of others begins”. And indeed, the US are regularly torn apart by mass shootings. Gun ownership and the need for regulation can seem incompatible at times. But precisely how is this political debate linked to the occurrences of mass shootings? This is what we intend to find out. Analyzing quotes emanating from American newspapers in the Quotebank dataset combined with additional data will help us study how these tragic events influence the media coverage – and therefore also the political debate – about gun control. This could help us understand the underlying mechanisms of this societal problem, and provide us with tools to help predict future controversy on the matter.

### Research Questions: 
- How do the occurences of mass shootings in the US influence the debate over firearms? 
- What features of the shootings (location, number of fatalities, weapon type/legality...) influence most the size of the following media coverage? For example, are shootings in more democrat states creating a larger media coverage and outrage afterwards? We would like to rank the features by influence on this matter.
- What are the words that are most correlated to the occurences of mass shootings? This would give us insight on how people are talking on the topic (is it more about dwelling on the victims or questionning the right to own a gun?).

### Proposed additional dataset:
For the project, in addition to the Quotebank dataset, we will use the **"Mother Jone's" dataset** on US Mass Shootings, that we got from 
https://data.world/awram/us-mass-shootings. Finding such a dataset was necessary for our project to be feasible. Indeed, it gives us basic information (e.g. date, number of fatalities) about each shooting that occured in the USA between 2015 and 2020, adding also some interesting features such as location, age and gender of the shooter, etc.

### Methods : 
- **Managing the size of the data**:<br> The Quotebank dataset's size does not let us work with it as a whole in a reasonnable way. Using Google Colab, we were able to link the dataset to Google Drive storage. We ran a code that would select only the quotes related to firearms and shootings, and save the corresponding rows to a new file. This way, we would get rid of the unecessary rows containing quotes who had no direct link to our study. 


- **Checking the relevance of the study**:<br> Plotting the distribution of the selected subset of quotes over time, and adding the occurences of shootings (from the Mother Jone's dataset), it seemed likely that there was some correlation, since we could see some peaks in quotes following the shootings. In order to check our intuition, we performed a Pearson correlation test between the number of quotes at a given date and the number of days since the last shooting.

- **Ranking features by influence on the media coverage**:<br> We plan on evaluating this by generating a "reaction score" for each shooting event. We can then perform linear regression with predictions X_i being the features of the shooting (number of fatalities, age of shooter, location, etc.), and the outcome y_i being the reaction score of event i. If we standardize the predictors using z-scores, we will then be able to compare the coefficients: the largest coefficients would correspond to the most influencial features. We simply need to quantify reaction using a "reaction score", computed with a relative increase in quotes before and after the shooting.

- **Reaction score and features analysis** : <br> We performed a regression analysis to try and predict the reaction score of a shooting based on the features of the shootings. Then, in order to get a sense of the correlations between the features we performed a principal component analysis (PCA).

- **Machine learning approach for word selection**: <br> We tried a machine learning approach to identify words that are correlated with the occurences of mass shootings. For this matter, we performed random forests classification on quotes that were previously labelled 'after' (if they occured after a shooting) or 'baseline'. Then we used the feature_importance function in order the get the words that were the most pertinent for the classification. 

## Team 

**CLE**ment Rio, 
**ZE**wei Xu, 
**MA**rgaux L'Eplattenier, 
**TH**omas Defauw <br>
a.k.a. **Clezemath**
