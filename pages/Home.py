import streamlit as st 
# Display the online image
# st.image('assets\jera.jpg')

# st.set_page_config(page_icon=None, page_title='Home')

st.markdown("""
Generation Model UI ⚡
Welcome to the Generation Model UI! 👋 This app enables the user to analyse results generated with the Generation Model, as well as to launch runs.
The app is divided into several sections, each of which focuses on a different aspect of the model:

Generation Model: This section allows the user to analyse results generated with the Generation Model and to launch runs.

Price and Fundamental Data: This page allows the user to analyse price and fundamental data.
Generation: This page allows the user to analyse generation data.
Load Factors: This page allows the user to analyse load factors.
Flows: This page allows the user to analyse flows.
Fuel Prices: This page allows the user to analyse fuel prices.
Submit runs: This page allows the user to submit runs to be solved by the Generation Model and using custom parameters. It also allows the user to control the progress of existing runs.
Weather Scenarios: This page allows the user to analyse and launch weather scenarios generation (Load, Solar, Wind,..).

Load Forecast - Calendar Creation: This page allows the user to create a calendar for a load forecast.
Load Forecast - Calibration: This page allows the user to change parameters and calibrate the load forecast model.
Load Forecast - Weather Paths: This page allows the user to execute a forecast for specified area. (Pages to be added: Solar and Wind scenarios)
Commodities scenarios: This page allows the user to analyse and launch commodities scenarios generation. This includes the fuel indexes prices to be used in the Generation Model. (Section to be impemented)

⏲️
Click here to add/modified scheduled jobs using Azure Logic Apps.

👾
Useful links for developers:

Generation model UI - repository (JapanGenerationModelUI) and app
Backend web app - repository (generation-model-backend-app) and app
Input generation app - repository (generation-model-inputs-app) and app (generation-model-inputs-app)
Generation model batch service - repository (JapanGenerationModelDocker) and app - generationmodelbatch
Input generation package - repository (GenerationModelInputs)
Supply and demand model package - repository (Japan_GenerationModel)
Generation Model - System Overview

""" )

