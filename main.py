import pandas as pd
import numpy as np
import math

# Lists that data is randomly picked from should be in order of most common answer in the middle

questions = ["What is your age?",
             "What is your profession?",
             "What is your gender?",
             "Which sport do you spend most of your time participating in?",
             "Which feature is the most valuable to you?",
             "What important features are we missing?",
             "What are you trying to solve by using our product?",
             "How easy is it to use our product?",
             "How likely are you to recommend this product to others?",
             "How could we improve our product to better meet your needs?",
             "What part of using our product was the most troublesome",
             "If our product worked how you want, would you use it?"]

featureList = ["Provides feedback on performance",
               "Is very durable.",
               "Is programmable with different patterns, or even random patterns, to be used during training.",
               "Easy to use.",
               "Analyses and gives vital information on which areas of the body need to be worked on.",
               "Provides on site data visualization and basic data interpretation.",
               "Can tell the difference between hard and soft punches.",
               ]

missingFeatures = ["High level of precision.",
                   "Good graphing ability",
                   "A simple to use GUI/GUI is confusing",
                   "Not battery powered",
                   "Steep learning curve"]

# This list is in order
professions = ["Pharmaceuticals",
               "Prefer not to say",
               "Financial Analyst",
               "Tutor",
               "Delivery",
               "Software Engineer/Developer",
               "Student",
               "Engineer",
               "Teaching Assistant",
               "Lab Technician",
               "Marketing",
               "None",
               "Call Center"]

# In order
sports = ["Cricket",
          "Table Tennis",
          "Wrestling",
          "Martial Arts",
          "Basketball",
          "Swimming",
          "Cycling",
          "Football",
          "Tennis",
          "Boxing",
          "Golf",
          "Gymnastics",
          "Track",
          "Volleyball"]

# in order
genders = ["Non binary",
           "Male",
           "Male",
           "Male",
           "Female",
           "Female",
           "Female",
           "Prefer not to say"]

# biased true false list
boolList = [True,
            True,
            True,
            False]


def rdBellCurveNum(num):
    # returns random number 100% in-between 0 and num
    # mean is num/2
    randomNormal = np.random.normal(0.5, 1)
    # using sigmoid probably distorts the outlying data by quite a bit but I can't be bothered to fix it anyway
    return int(sigmoid(randomNormal) * num)


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def answerQuestion():
    # What is your age?
    # average age should be 20 with 15 and 25 as highest,
    # function uses standard dev of 3, with mean of 5 added to 15
    data = []
    uniqueAge = int(np.random.normal(5, 3)) + 15
    data.append(uniqueAge)

    # What is your profession?
    # produce random profession
    # produces a random number between 0 and length of professions list
    profession = professions[rdBellCurveNum(len(professions))]
    data.append(profession)

    # What is your gender?
    # produce random gender
    gender = genders[rdBellCurveNum(len(genders))]
    data.append(gender)

    # Which sport do you spend most of your time participating in?
    # random sport
    sport = sports[rdBellCurveNum(len(sports))]
    data.append(sport)

    # Which feature is the most valuable to you?
    # random important feature
    feature = featureList[rdBellCurveNum(len(featureList))]
    data.append(feature)

    # What important features are we missing?
    mFeature = missingFeatures[rdBellCurveNum(len(missingFeatures))]
    data.append(mFeature)

    # What are you trying to solve by using our product?
    data.append("")

    # How easy is it to use our product?
    easeOfUse = -1
    while easeOfUse < 0 or easeOfUse > 5:
        easeOfUse = int(np.random.normal(4, 0.5))  # we want ease of use to be high
    data.append(easeOfUse)

    # How likely are you to recommend this product to others?
    recommendation = -1
    while recommendation < 0 or recommendation > 10:
        recommendation = int(np.random.normal(6, 2))
    data.append(recommendation)

    # How could we improve our product to better meet your needs?
    data.append("")

    # What part of using our product was the most troublesome
    feature = featureList[rdBellCurveNum(len(featureList))]
    data.append(feature)

    # If our product worked how you want, would you use it?
    wouldUse = boolList[rdBellCurveNum(len(boolList))]
    data.append(wouldUse)

    assert len(data) == len(questions)

    return data


def main():
    dataSamples = 134
    producedData = []
    for i in range(dataSamples):
        producedData.append(answerQuestion())
    # save output file
    df = pd.DataFrame(columns=questions, data=producedData)  # create dataframe with questions as the columns
    df.to_csv("Output.csv")


main()
