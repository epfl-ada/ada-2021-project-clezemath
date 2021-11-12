# Firearms Debate in the US and its Relation to Mass Shootings

### Abstract:
Gun control is one of the most controversial political topics in the United States. America being one of the world’s most liberal countries in the world, freedom is central amongst its values. But some could say: “My freedom stops when that of others begins”. And indeed, the United States are torn apart by relatively frequent occurrences of mass shootings. The right to own a gun therefore clashes with a need of more regulation to prevent a downward spiral of violence. But precisely how is this political debate about firearms linked to the occurrences of mass shootings? This is what we intend to find out by analyzing quotes emanating from American newspapers provided by the Quotebank dataset. Using this dataset combined with another one containing information about the all the mass shootings in the US in our studied timeframe, we aim to study how these tragic events influence the media coverage – and therefore also the political debate – about firearms and gun control. This could help us understand the underlying mechanisms of this societal problem, and provide us with tools to help predict future controversy on the matter.

### Research Questions: 
- How do the occurences of mass shootings in the US influence the debate over firearms? 
- What features of the shootings (location, number of fatalities, weapon type/legality...) influence most the size of the following media coverage? For example, are shootings in more democrat states creating a larger media coverage and outrage afterwards? We would like to rank the features by influence on this matter.
- What are the words that are most correlated to the occurences of mass shootings? This would give us insight on how people are talking on the topic (is it more about dwelling on the victims or questionning the right to own a gun?).

### Proposed additional dataset:
For the project, in addition to the Quotebank dataset, we will use the "Mother Jone's" dataset on US Mass Shootings, that we got from 
https://data.world/awram/us-mass-shootings. Finding such a dataset was necessary for our project to be feasible. Indeed, it gives us basic information (e.g. date, number of fatalities) about each shooting that occured in the USA between 2015 and 2020, adding also some interesting features such as location, age and gender of the shooter, etc.

### Methods : 
For our analysis, we first selected a subset of three words : "gun", "shooting", "firearm" (because those words are necessary for any talk about gun control/firearm violence). We then created a subset of the Quotebank dataset containing all the quotes where at leat one of these words occurs. This allowed us to plot the distribution of this selected subset over time. Subsequently, we peformed some descriptive analysis of the Mother Jones dataset. 
In order to link the two datasets and to show that our word subset is relevant, we performed a Pearson correlation test between the number of quotations in our subset at a given date and the number of days since the last shooting.
The _seaborn_ and _matplotlib_ were used for data vizualisation, while the _stats_ and _statsmodels_ libraries were used for statistical inferences. 

### Proposed timeline : 

1. Mass shootings and quotes: Analyse the correlation between quotes in our subest and occurences of mass shootings
a. Words set defined a-priori (done)
b. Correlation-based word set selection, and analysis (19 Nov 2021)

2. Underlying predictors : Determine features of the shootings correlated to the importance of the media coverage (03 Dec 2021)

4. Additional : use Neural Networks (RNNs?) to predict the link of quotes with mass shootings (supervised learning on a manually annotated subset) (10 Dec 2021)

5. Report finalisation (last week --> 17 Dec 2021)

#### Questions for TAs : 
