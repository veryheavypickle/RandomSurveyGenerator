import pandas as pd
import numpy as np
import math

willingnessToBuy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

biasedBool = [True,
              False,
              False,
              False,
              False]

biasedBool2 = [True,
               False,
               False,
               False]

genders = ["Non Binary",
           "Male",
           "Female",
           "Female",
           "Female",
           "Male",
           "Male",
           "Prefer not to say"]

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

professions = ["Pharmaceuticals",
               "Teachers Assistant",
               "Delivery",
               "Student",
               "Student",
               "Student",
               "Software Engineer/Developer",
               "Cashier"]


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

    # What is your gender?
    # produce random gender
    gender = genders[rdBellCurveNum(len(genders))]
    data.append(gender)

    # What is your profession?
    profession = professions[rdBellCurveNum(len(professions))]
    data.append(profession)

    # Are you currently participating in a sport professionally?
    boolSports = biasedBool2[rdBellCurveNum(len(biasedBool2))]
    data.append(boolSports)

    # If so what sport would that be?
    sport = sports[rdBellCurveNum(len(sports))]
    # if the previous answer was yes, this gets an answer, else no answer
    if data[3]:
        data.append(sport)
    else:
        data.append("I don't play sport professionally")

    # Do you think information is displayed in a easy to understand and useful way?
    yesno = not biasedBool[rdBellCurveNum(len(biasedBool))]
    data.append(yesno)

    # Do you have any remarks for us about this?
    data.append("No, i am bot, i can't think")

    # Was the UI (User Interface) easy to understand?
    yesno = not biasedBool[rdBellCurveNum(len(biasedBool))]
    data.append(yesno)

    # Do you have any further suggestions for the UI?
    data.append("No, i am still bot, i still don't know what i am doing")

    # What feature was most valuable to you?
    feature = featureList[rdBellCurveNum(len(featureList))]
    data.append(feature)

    # What is the most important feature to you we are missing?
    missingFeature = missingFeatures[rdBellCurveNum(len(missingFeatures))]
    data.append(missingFeature)

    # Would you buy our product if it were to come out today?
    yesno = biasedBool[rdBellCurveNum(len(biasedBool))]
    data.append(yesno)

    # Would you buy our product if in the future when there are more features?
    yesnolist = [False, True, False, False]
    yesno = yesnolist[rdBellCurveNum(len(yesnolist))]
    data.append(yesno)

    assert len(data) == len(questions)

    return data


def main():
    dataSamples = 18
    producedData = []
    for i in range(dataSamples):
        producedData.append(answerQuestion())
    # save output file
    df = pd.DataFrame(columns=questions, data=producedData)  # create dataframe with questions as the columns
    df.to_csv("Output.csv")


# Main
# Lists that data is randomly picked from should be in order of most common answer in the middle

questions = ["What is your age?",
             "What is your gender?",
             "What is your profession?",
             "Are you currently participating in a sport professionally?",
             "If so what sport would that be?",
             "Do you think information is displayed in a easy to understand and useful way?",
             "Do you have any remarks for us about this?",
             "Was the UI (User Interface) easy to understand?",
             "Do you have any further suggestions for the UI?",
             "What feature was most valuable to you?",
             "What is the most important feature to you we are missing?",
             "Would you buy our product if it were to come out today?",
             "Would you buy our product if in the future when there are more features?"]

main()
