# How I used AI to classify Biden and Trump tweets

## Results

![](https://raw.githubusercontent.com/Paulocochile/profilebreakdown/main/BidenR.PNG)
![](https://raw.githubusercontent.com/Paulocochile/profilebreakdown/main/TrumpR.PNG)

### Notes

- Trump Model average precision: 0.725
- Biden Model average precision: 0.807
- To train the model to recognize a label, you need a minimum of 10 labeled tweets. In the 200 tweets I labeled of Biden, I only found 8 for "Media & Entertainment," so I couldn't train that label.  

## Getting the Data

Doing a quick Google search, I found all the [Trump tweets](https://www.kaggle.com/austinreese/trump-tweets?select=realdonaldtrump.csv) and [Biden tweets](https://www.kaggle.com/rohanrao/joe-biden-tweets) I needed in Kaggle.


## Labels

### Choosing Labels

I started by brainstorming the labels that I thought would be relevant to get.
To get more inspiration, I went through clustering efforts made by others (i.e. [Trump Clustering](https://www.kaggle.com/wordcards/trump-tweets-clustering)) and then I complimented my initial labels with what I learned.
Ultimately, it was while labeling the data that I came to the final labels. I realized some labels they didn't really tweet about (i.e., "Institutions") and found others that came up a lot (i.e., "Criticizing").

### Labeling data to train the model

I manually went through [200 Trump tweets](https://raw.githubusercontent.com/Paulocochile/profilebreakdown/main/TrumpTrainingData.csv) and [200 Biden tweets](https://raw.githubusercontent.com/Paulocochile/profilebreakdown/main/BidenTrainingData.csv) and labeled them with the above to train the AI Model.

## Training the Model

Google has incredibly easy to use tools to train AI models. I specifically used "Multi-label text classification" in their AutoML product.
You can find instructions to do this [here.](https://medium.com/voice-tech-podcast/auto-text-classification-using-googles-automl-80f151ffa176)

## Using the Model to label all tweets

I had to set up a local environment and create a [python script](https://raw.githubusercontent.com/Paulocochile/profilebreakdown/main/predict.py) to use the Models I trained to label all the tweets. Some handy links I had to use:

- [Before you begin](https://cloud.google.com/natural-language/automl/docs/before-you-begin?_ga=2.117550720.-828033756.1603643984)
- [Set up your local environment](https://cloud.google.com/python/setup#linux)
- [A simple template to start the script](https://cloud.google.com/natural-language/automl/docs/predict)
- [Using a service account to give you access to the Model](https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-python)
- [Using a service account to give you access to the Model in video](https://www.youtube.com/watch?v=tSnzoW4RlaQ&ab_channel=GoogleCloudPlatform)
- [Changing the API endpoint to the EU if you're in the EU like me](https://cloud.google.com/natural-language/automl/docs/locations)

I then ran the script to get the [labeled Trump Tweets](https://raw.githubusercontent.com/Paulocochile/profilebreakdown/main/Trumpoutput.csv) and [labeled Biden Tweets](https://raw.githubusercontent.com/Paulocochile/profilebreakdown/main/Bidenoutput.csv).

## Visualizing the Results

The last step was to get all the data in a Google spreadsheet and choose the right chart type to showcase the results. I then used some design heuristics to make the two final images, and that's it!
