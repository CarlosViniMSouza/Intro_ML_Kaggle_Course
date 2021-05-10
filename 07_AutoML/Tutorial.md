## Introduction
When applying machine learning to real-world data, there are a lot of steps involved in the process -- starting 
with collecting the data and ending with generating predictions. (We work with the seven steps of machine learning, 
as defined by [Yufeng Guo](https://towardsdatascience.com/the-7-steps-of-machine-learning-2877d7e5548e) here.)

![img1](https://i.imgur.com/mqTCqBR.png)

It all begins with Step 1: Gather the data. In industry, there are important considerations you need to take into 
account when building a dataset, such as [target leakage](https://www.kaggle.com/alexisbcook/data-leakage). When 
participating in a Kaggle competition, this step is already completed for you.

In the [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) and the [Intermediate 
Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) courses, you can learn how to:

**° Step 2:** Prepare the data - Deal with [missing values](https://www.kaggle.com/alexisbcook/missing-values) and 
[categorical data](https://www.kaggle.com/alexisbcook/categorical-variables).('Feature engineering' is covered in a 
separate course.)

**° Step 4:** Train the model - Fit [decision trees](https://www.kaggle.com/dansbecker/
your-first-machine-learning-model) and [random forests](https://www.kaggle.com/dansbecker/random-forests) to 
patterns in training data.

**° Step 5:** Evaluate the model - Use a [validation set](https://www.kaggle.com/dansbecker/model-validation) to 
assess how well a trained model performs on unseen data.

**° Step 6:** Tune parameters - Tune parameters to get better performance from [XGBoost models](https://www.kaggle.com/alexisbcook/xgboost).

**° Step 7:** Get predictions - Generate predictions with a trained model and [submit your results to a [Kaggle competition](https://www.kaggle.com/carlosvinimsouza/exercise-machine-learning-competitions/edit).

That leaves **Step 3: Select a model**. There are a lot of different types of models. Which one should you select 
for your problem? When you're just getting started, the best option is just to try everything and build your own 
intuition - there aren't any universally accepted rules. There are also many useful Kaggle notebooks (like this 
one) where you can see how and when other Kagglers used different models.

Mastering the machine learning process involves a lot of time and practice. While you're still learning, you can 
turn to **automated machine learning (AutoML) tools** to generate intelligent predictions. 

## Automated machine learning (AutoML)

In this notebook, you'll learn how to use [Google Cloud AutoML Tables](https://cloud.google.com/automl-tables/docs/beginners-guide) to automate the machine learning process. While Kaggle has already taken care of the data collection, AutoML Tables will take care of all remaining steps.

![img2](https://i.imgur.com/5SekA3O.png)

AutoML Tables is a *paid service*. In the exercise that follows this tutorial, we'll show you how to claim $300 of free credits that you can use to train your own models!

```
Note: This lesson is optional. It is not required to complete the Intro to Machine Learning course.
```

## Code
We'll work with data from the [New York City Taxi Fare Prediction competition](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction). In this competition, we want you to predict the fare amount (inclusive of tolls) for a taxi ride in New York City, given the pickup and dropoff locations, number of passengers, and the pickup date and time.

To do this, we'll use a [Python class](https://www.kaggle.com/alexisbcook/automl-tables-wrapper) that calls on AutoML Tables. To use this code, you need only define the following variables:

° ```PROJECT_ID``` - The name of your [Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects). All of the work that you'll do in Google Cloud is organized in "projects".

° ```BUCKET_NAME``` - The name of your [Google Cloud storage bucket](https://cloud.google.com/storage/docs/creating-buckets). In order to work with AutoML, we'll need to create a storage bucket, where we'll upload the Kaggle dataset.

° ```DATASET_DISPLAY_NAME``` - The name of your dataset.

° ```TRAIN_FILEPATH``` - The filepath for the training data (train.csv file) from the competition.

° ```TEST_FILEPATH``` - The filepath for the test data (test.csv file) from the competition.

° ```TARGET_COLUMN``` - The name of the column in your training data that contains the values you'd like to predict.

° ```ID_COLUMN``` - The name of the column containing IDs.

° ```MODEL_DISPLAY_NAME``` - The name of your model.

° ```TRAIN_BUDGET``` - How long you want your model to train (use 1000 for 1 hour, 2000 for 2 hours, and so on).

All of these variables will make more sense when you run your own code in the following exercise!