# Sugar - Diabetic Risk Assessment and Diet Recommendation

## Problem Statement
Diabetes is a widespread health issue, affecting millions of people globally. We aim to address the growing concern of diabetes by creating a system that helps individuals assess their likelihood of developing diabetes and provides tailored diet recommendations. This tool focuses on both individuals who have already been diagnosed with diabetes and those at risk of developing the condition.

## Why We Developed It
The main motivation behind this project is to help people, especially those at risk or early-stage diabetics, by offering a system that can predict their chances of developing diabetes. This can be a crucial early intervention tool, offering suggestions to modify lifestyle habits, such as diet, to help prevent or manage diabetes effectively.

## What We Developed
We developed an application that
- Made a **small fun quiz** at the start to engage users.
  In order to educate the users, we provided two images and asked them to choose the healthier. After they pick the answer, we provide a description of the foods.
- Built a **machine learning model** which uses patient information to predict the risk of developing diabetes.
- Allow the user to **upload an image**.
- We used the:
  - probability of developing diabetes
  - the uploaded image
  - the goals given by the user
  for the **LLM**.
- The implemented LLM was used to provide insights, analyze the meal, and offer personalized diet recommendations

A flowchart design to explain what we have developed diagrammatically:

![Alt text](https://github.com/Aneeshie/sugar-app/blob/main/flowchart.png?raw=true)

### ML Model
This is the implemented **machine learning model**: https://colab.research.google.com/drive/1Q2fakKaOsunKjjsULb68jWuEP2HDHomv
Dataset used can be accessed using https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

### Large Language Models
We implemented the **LLM** in streamlit
We gave the prompts obtained from **input values** and the **probability that the user has diabetes** as prompts for the LLM

## Vision
Our vision is to make diabetes prevention and management accessible and engaging for everyone. We aim to empower individuals with the knowledge and tools to make informed decisions about their health.
We plan to:
 - Integrate this system with hospitals, enabling healthcare professionals to use the tool for early diagnosis and personalized patient care.
 - Create a full-fledged encryption system for individuals so that their personal assessments and health data are secured
 - Ensure that the LLM is capable of learning from multiple users instead of one user in order to perform recommendations based on similar users
and ensure more personalized recommendations

## Tech Stack Used
- **Python**: For implementing the **machine learning** models and handling data processing tasks.
  Python Version: 3.12.0
- **Gemini API**: For integrating the **LLM** (Large Language Model) to provide personalized diet recommendations and insights based on user data.
  
## Dependencies
- **streamlit**
- **pandas**
- **numpy**
- **pickle**
- **xgboost**
  
## Challenges
- **Handling LLM Responses**: Managing and generating meaningful responses from the LLMs was challenging, as we had to ensure the insights were relevant and accurate.
- **Dataset Limitations**: The available datasets did not contain all the required values or were missing important data points, making the training process more difficult and requiring data augmentation or preprocessing.
- **Displaying Meaningful Error Messages**: Ensuring that the system displays clear and helpful error messages when issues arise was a challenge, particularly when dealing with user input or backend processing errors.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Aneeshie/sugar-app.git
   cd sugar-app

2. Run app.py
  ```bash
  streamlit run app.js
