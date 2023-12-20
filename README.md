# MEDITAZONE-ML

## Description

Meditazone, was inspired by Generation Z Indonesians with mental health issues, such as anxiety, stress, and depression. The app helps individuals recognize and manage mental disorders in an innovative way using machine learning, cloud computing, and mobile development.

## Machine Learning Platform

This repository contains 2 machine learning models to predict user-given vent sentences with 3 intended labels, namely Anxiety, Stress, and Depression. We use 2 techniques namely with RNN and transfer learning with fine-tuning using BERT architecture in TensorFlow framework. In this application, we implemented the RNN model because it has a fairly high level of accuracy where in this RNN model there is an Embedding Layer, Bidirectional LSTM (Long Short-Term Memory), Batch Normalization, and Dense Layers.

## Feeling Condition Prediction Models

Feeling condition prediction models are machine learning models that can be used to predict a person's condition based on the text they write. The model is useful for mental disorder detection and behavior prediction, using Natural Language Processing (NLP) techniques to process text. NLP is a field of computer science that examines the interaction between humans and computers with natural language.

## System Recommendation

Once the mental disorder prediction model detects the type of mental disorder the user is experiencing, the Meditazone recommendation system will recommend appropriate meditations, articles, and quotes. These recommendations will consider the following factors:

1. The type of mental disorder the user is experiencing
2. User needs and preferences

The meditation recommendations will recommend meditations that can help users to manage and overcome their mental disorders. We will also recommend articles that can provide useful information and insights to the user. These articles can help the user to understand his/her mental disorder, how to overcome it, and improve his/her overall mental health. Also, Recommended quotes will recommend quotes that can provide motivation and inspiration to the user.

## Step To get started with the mental disorder detection prediction model

1.  Clone this repository: https://github.com/meditazone/MEDITAZONE-ML/
2.  Install the required framework:

    ```py
    pip install python pickle tensorflow transformers scikit-learn
    ```

3.  Download the trained model and processed dataset from the following links:

    - Detection without BERT Transfer Learning:
      js
      https://github.com/meditazone/MEDITAZONE-ML/blob/main/Build_Model_Machine_Learning_for_NLP_Without_Using_BERT.ipynb
    - Detection with BERT Transfer Learning:
      js
      https://github.com/meditazone/MEDITAZONE-ML/blob/main/Model_Machine_Learning
