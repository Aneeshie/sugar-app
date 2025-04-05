# Sugar - Diabetic Risk Assessment and Diet Recommendation

## Problem Statement
Diabetes is a widespread health issue, affecting millions of people globally. We aim to address the growing concern of diabetes by creating a system that helps individuals assess their likelihood of developing diabetes and provides tailored diet recommendations. This tool focuses on both individuals who have already been diagnosed with diabetes and those at risk of developing the condition.

## Why We Developed It
The main motivation behind this project is to help people, especially those at risk or early-stage diabetics, by offering a system that can predict their chances of developing diabetes. This can be a crucial early intervention tool, offering suggestions to modify lifestyle habits, such as diet, to help prevent or manage diabetes effectively.

## What We Developed
We developed a machine learning-based application that:
- Made a small fun quiz at the start to engage users.
- Built a machine learning model which uses patient information to predict the risk of developing diabetes.
- Created an upload food image feature to analyze meals.
- Used LLMs to provide insights, analyze the meal, and offer personalized diet recommendations.

## Tech Stack Used
- **Streamlit**: For building the web interface to make the app user-friendly and interactive.
- **Python**: For implementing the machine learning models and handling data processing tasks.

## Dependencies
- **streamlit**
- **pandas**
- **numpy**
- **pickle**


## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Aneeshie/sugar-app.git
   cd sugar-app

2. Run app.py
  ```bash
  streamlit run app.js
