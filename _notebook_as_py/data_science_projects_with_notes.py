# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div align="center" style="font-size:60px;">
# Probelehrveranstaltung für die Professur für Angewandte Mathematik mit Schwerpunkt Statistical Learning
# <br><br>
# Data Science Projects
# <br><br>
# Dr. Fabian Spanhel
# <div/>
#     
# <div align="left" style="font-size:16px;">
# <div/>

# %% [markdown] slideshow={"slide_type": "notes"}
# 1 Min]
# 1. Welcome to my second presentation which is about data science projects.
# 2. Data science projects is a course that is targeted at master students who like to work in the data science domain.
# 3. This course is the follow-up course **to** the course Data Science Challenge / Projekt which I lecture at the moment for the bachelor students of Data Science and scientific computing.
# 4. This courses emphasis is on practical skills, problem-solving, and the ability to use data science tools and methods in practical scenarios, such as those encountered in industry work situations.
# 5. For this purpose, this course provides hands-on projects and case studies (to highlight and reinforce the practical aspects of data science.)
#
# Basically, this is the course I would like to have before I graduate
#

# %% [markdown] slideshow={"slide_type": "skip"}
# ## Recap Data Science Projekt / Challenge
#
# Bachelor Course in the 5th semester
#
# - Learn some basics of **writing good code which is suitable for production** and usable by ML engineers.
# - Learn tools and methods to **conduct reproducible data science experiments and to collaborate in a team**.
# - Consolidate what you have learned through a **collaborative practice project**.
#
# Topics:
#   - Source code and data version control.
#   - Setting up and implementing a Python project (Virtual environments, project structure, creating a pip-installable package).
#   - Good coding habits (Style, type hints, documentation, Git hooks).
#   - Project management and collaborative coding using Git and GitLab.

# %% [markdown] slideshow={"slide_type": "skip"}
# Personal motivation for DSC and also here (I have a mathematical background and took me some to grasp how to build a product, I would have highly appreciate it if this was clear)
# There is a young difference between an ad hoc analysis or building a data product
#
#
# or program is geared toward hands-on, real-world application and implementation of data science concepts and techniques. It implies that the emphasis is on practical skills, problem-solving, and the ability to use data science tools and methods in practical scenarios, such as those encountered in industry or everyday work situations.
# In essence, a "Data Science Practical" course or program is one that aims to equip students or participants with the skills and knowledge needed to effectively apply data science in practical, professional settings. It often includes hands-on exercises, projects, or case studies to reinforce the practical aspects of data science.
#
# Aim: Connect the dots and fill some holes
# Practice focus, give the students a cutting edge
# Give students an edge in an increasingly competitive marketplace
# Gutes Feedback von den Studierenden, dass das gebraucht wird, Zitat Student „“ und ich habe selber auch die Erfahrung gemacht, dass die Studierenden nicht „business-ready“ sind (nicht so negativ formulieren, eher mehr business ready)
# Ich bringen in den Kurs mein Wissen aus vielen Praxisprojekten ein
#

# %% [markdown] slideshow={"slide_type": "skip"}
# ## How data science has changed into the last years
# - From on-premise to cloud.
# - From POC to production --> More Software Engineering. MLOps has emerged.
#     - MLOps which should facilitate development and operationalization of AI has become more important -> More Software Engineering.
# - No unicorns anymore but the data science role is getting split into multiple specialized roles -> ML & Data Engineering roles have emerged.
# - In general, sofware engineering skills and MLOps become more important
# - Before specializing in the job market, I think it is good to get an impression of these specialized roles and learn more software engineering -> Objective of this course -> Oder DSC wollte software engineering Konzepte beibringen, das wird hier fortgeführt und aber auch Einblick in die Rollen
# - ...
#
# See also ["**Is Data Scientist Still the Sexiest Job of the 21st Century?**"](https://hbr.org/2022/07/is-data-scientist-still-the-sexiest-job-of-the-21st-century)
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# **How has data science changed in the last years?**
# - From on-premise to cloud.
#
# - From POC to production.
# - No unicorns anymore but the data science role is getting split into multiple specialized roles 
#
#     -> ML & Data Engineering roles have emerged.
# - In general, sofware engineering skills and MLOps have become more important.
# - ...
#
#
#
#
#

# %% [markdown] slideshow={"slide_type": "fragment"}
# See also ["**Is Data Scientist Still the Sexiest Job of the 21st Century?**"](https://hbr.org/2022/07/is-data-scientist-still-the-sexiest-job-of-the-21st-century)
#
# **The goal of this course is to address the changes that have occurred in recent years and provide students with skills that might gain them a competitive advantage.**

# %% [markdown] slideshow={"slide_type": "notes"}
# [2 Min]
#
# 1. What practical skills should students or graduates have these days?
# 2. Well, let's take a look back at the last seven years that have passed since I've been working in the industry.
# 3. First of all, the tools with which data scientist work have changed a lot. Ten years ago, it was like the wild west and there were few tools and standards available.
#     - Most importantly, analytics as well as development and management of ML models have largely shifted to the cloud for several reasons.
# 4. Moreover, the phase of POCs everywhere has passed and more models are put into production and need to be managed. As a consequence, software engineering becomes more crucial.
# 5. Previously, a data scienctist was a unicorn, meaning they did all required tasks — from conceptualizing the use case, to 
# interfacing with business and technology stakeholders, to developing the algorithm and deploying it into production. While this may still be true, there is a continued differentiation of responsibilities. Like **machine learning engineers**, **data engineers**, **advanced analytics**, and **data oriented product managers**. 
#
#
#
# - Specialization may be key.
# - Before specializing in the job market, I think it is good to get an impression of these specialized roles and learn more software engineering -> Objective of this course -> Oder DSC wollte software engineering Konzepte beibringen, das wird hier fortgeführt und aber auch Einblick in die Rollen
#

# %% [markdown] slideshow={"slide_type": "slide"}
# **Data Science Project Workflow**
# <img src="./figures/ds_project_0.png" alt="Data Science Projects" style="width: 1600px;"/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Data Science Project Workflow**
# <img src="./figures/ds_project_1.png" alt="Data Science Projects" style="width: 1600px;"/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Data Science Project Workflow**
# <img src="./figures/ds_project_2.png" alt="Data Science Projects" style="width: 1600px;"/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Data Science Project Workflow**
# <img src="./figures/ds_project_3.png" alt="Data Science Projects" style="width: 1600px;"/>

# %% [markdown] slideshow={"slide_type": "notes"}
# [6 Min]
# 1. In general, a data science project is often a cross-functional project that requires team to work together.
#     1. On the left hand side we have the business intelligence or analytics people, or people with a math/stats background (blue) and on the right we have people with an information science background or software engineers (green).
#     1. This color gradient should highlight that boundaries between these roles are not strict and evolving.
# 1. The center of a data science project is data.
# 1. This data is used to kick-off a POC or to do an ad hoc analysis.
#     1. This is a one shot analysis or model building.
# 1. The outcome of this POC or ad hoc analysis could be a report/app.
# 1. Or it could be deployment and management of a machine learning model.
#     1. This model could also then end in an app or dashboard.
#
# 1. So what skills are needed in this data science project workflow?
# 1. Regarding POC/ad hoch analyses
#     - Communication is very important. But this best learned in the industry. (viele Fehler)
#     - Dev:
#         - local / cloud + Metaflow
#         - 
#     - Sensibilisieren Kausalität, Trade-off Prediction und Causal Inference.
# 1. Depending on the organization a data scientist might involved or not involved in MLOps. Irrespective of that, there are skills that a data scientist can process to support the interaction with ML or software engineers. -> passt nicht, hier eher sagen dass da auch stats skills gebraucht werden
#     - MLOps
#         - Model, Feature & Target drift
# 1. Regarding Apps/Dashboard.
#     - Especially for POCs the ability to provide an application is crucial. It is important that a DS can present his results. Früher war das schwierig, weil man einen FrontEnd Entwickler brauchte. Heute ist das spielend einfach mit Streamlit. man muss nur wissen dass es das gibt.
#     
# For this presentation, I pick some skills/tools and give a short introduction so that it's possible to get an impression of what to expect from this course.

# %% [markdown] slideshow={"slide_type": "skip"}
# No differently from any cross-functional project that requires teams to work together! 
# Organizations need to determine boundaries between these roles in a way that works for everyone, so there can be clarity about responsibilities. 
#
# - Important to understand how a project looks like
# - Data
# - Cross-functional team (Stakeholder, Data Sciencist, Sofware Enigeers)
#
# - Nested cross validation (Students were not sicher)

# %% [markdown] slideshow={"slide_type": "slide"}
# **AWS Cloud services**
#
# - Interacting with cloud services is a demanded skill for Data Scientist and will become even more important.
#
# - We will cover the fundamental services of AWS in this course and learn how to
#     - Store and retrieve data, such as files and backups, using **S3**.
#     - Leverage scalable cloud-based compute capacity using **EC2**.
#     - To build, train, and deploy ML models with **Sagemaker**.
# - Optional: Glue & Athena, Lambda functions...
# - How to interact with various AWS services using Python and the **boto3** package.
#
# **We will be using AWS for the hands-on project in this course!**

# %% [markdown] slideshow={"slide_type": "notes"}
#  [1 min]
# - Fully managed machine learning service named Amazon SageMaker. It allows the data scientist to run it on EC2. Data scientists use this tool to build, train, deploy machine learning models, and scale business operations

# %% [markdown] slideshow={"slide_type": "slide"}
# **Methodology: Multi-step forecasts**

# %% [markdown] slideshow={"slide_type": "notes"}
# [6 Min]
# - Let's just pick this/go into detail here because we have also spoken about this in the first lecture

# %% [markdown] slideshow={"slide_type": "fragment"}
# - In practice, one often has to provide multi-step forecasts $\big(\text{Pred}_t[Y_{t+h}]\big)_{h=1, \ldots, H}$.
# - How can we obtain this sequence of forecasts?
#

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Recall: If $Y_t = aY_{t-1} + U_t$ then $\text{Pred}_t[Y_{t+h}] = a\text{Pred}_t[Y_{t+h-1}]$.
#

# %% [markdown] slideshow={"slide_type": "fragment"}
# - What if $Y_t = f(Y_{t-1}) + U_t$?

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Can we use $\text{Pred}_t[Y_{t+h}] = f\left(\text{Pred}_t[Y_{t+h-1}]\right)$?

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Multi-step forecasts with features**
#
#
# - What if $Y_t = f(Y_{t-1}, X_{t-1}) + U_t$ and we don't know $(X_{t})_{h=t+1,\ldots, t+H}$? 
# - If $Y_t = aY_{t-1} + bX_{t-1} + U_t$, we have that
#
#     $
#     \begin{align}
#     \text{Pred}_t[Y_{t+1}] & = aY_{t} + bX_{t}\phantom{....}
#     \end{align}
#     $
#
#     but because we don't know $\text{Pred}_t[X_{t+1}]$ we cannot compute
#
#     $
#     \begin{align}
#     & \text{Pred}_t[Y_{t+2}] = a\text{Pred}_t[Y_{t+1}] + b\text{Pred}_t[X_{t+1}]
#     \end{align}
#     $

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Possible solutions:
#     1. Set up a model for $X_t$, e.g., $X_t = r(X_{t-1}, Y_{t-1}) + V_t$, to get the **indirect forecast**
#     
#         $\text{Pred}_t[Y_{t+h}] = f(\text{Pred}_t[Y_{t+h-1}], \text{Pred}_t[X_{t+h-1}])$
#     2. For each forecast horizon $h$, set up a model $Y_{t+h} = f_h(Y_{t-1}, X_{t-1}) + U_{t,h}$ to get the **direct forecast** 
#     
#         $\text{Pred}_t[Y_{t+h}] = f_h(Y_{t-1}, X_{t-1})$

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Multi-step forecasts with features: Possible solutions**
#
# 1. Get the **indirect forecast**
#
#     $\text{Pred}_t[Y_{t+h}] = f(\text{Pred}_t[Y_{t+h-1}], \text{Pred}_t[X_{t+h-1}])$
# 2. Get the **direct forecast**
#
#     $\text{Pred}_t[Y_{t+h}] = f_h(Y_{t-1}, X_{t-1})$
# - Note that 1. increases in the number of features, whereas 2. increases in the number of forecast horizons $h$.
# - How to tune the corresponding models of 1. and 2.?
# - How can we handle the data to do direct and indirect forecasts?
# - Which approach is better?

# %% [markdown] slideshow={"slide_type": "fragment"}
# **These questions will be investigated with a hands-on project in this course!**

# %% [markdown] slideshow={"slide_type": "skip"}
# **Methodology: Model tuning for time series** 
#
# - $K$-fold cross-validation is most commonly used to tune the hyperparameters of a model.
# - It is typically based on the assumption of iid data.
# - How to do cross-validation when we have temporal dependence?

# %% [markdown] slideshow={"slide_type": "skip"}
# - $K$-fold cross-validation can be used in [special cases](https://www.sciencedirect.com/science/article/abs/pii/S0167947317302384).
# - In general, cross-validation must consider existing dependence of the data to prevent [data leakage](https://en.wikipedia.org/wiki/Leakage_(machine_learning).
# - Data leakage is a [serious problem in academica and industry](doi:10.1016/j.patter.2023.100804).
#

# %% [markdown] slideshow={"slide_type": "skip"}
# **Model tuning with time series cross-validation**
# <div style="display: flex; align-items: left;">
#   <div style="flex: 1; padding: 30px; font-size: 25px;">
#     <ol style="margin: 200; padding: 0">
#       <li>Model training: A predictive model is trained on training data of length $T_{train}$.</li>
#       <li>Validation: The model is scored on validation data of length $T_{val}$.</li>
#       <li>Shifting: The end of the new training data is increased to $T_{train} + T_{val}$.</li>
#       <li>Repeat Steps 1 - 3 until $T_{val} = 0$.</li>
#       <li>Performance evaluation: Aggregate validation scores.</li>
#     </ol>
#   </div>
#   <div style="flex: 2; padding: 0px;">
#       <img src="./figures/ts_split.png" alt="Time Series Cross Validation" style="width: 700px;"/>
#   </div>
# </div>
#
# Questions:
# <ul style="margin: 200; padding: 0; font-size: 25px; margin-top: -20px">
#   <li>How to specify ($T_{train}$, $T_{val}$) or the resulting folds?</li>
#   <li>How to optimize the training length? Use $(w_tY_t)_{t=1,\ldots T_{train}}$ as training data, where $(w_t)_{t=1}^{T}$ is increasing in $t$ and can be obtained via cross-validation?</li>
#   <li>Should the aggregation of validation scores be weighted equally, or should the results of validation sets closer to today be weighted more heavily?</li>
#   <li>How to actually split the data into folds? </li>
# </ul>
#  
# <!-- To the best of my knowledge there is no package available that covers important practical cases 
# (split w.r.t. date, a set of time series, groups)
# -->
# <span style="font-size: 30px; margin-top: -20px">**These questions will be investigated with a hands-on project in this course!**</span>

# %% [markdown] slideshow={"slide_type": "notes"}
# Certainly, here's a reformulation:
#
# "In practical scenarios, it's common to make predictions for a variable of interest over multiple future time steps. This means that instead of predicting just the next value, you are forecasting a sequence of future values for the variable."

# %% [markdown] slideshow={"slide_type": "notes"}
#  - to mimic the real-world forecasting scenario -> want to forecast six weeks -> out-of-sample six weeks
# - these two questions have an enormous practical relevance in my work
#
# Time series CV:
# The dataset is divided into time periods (e.g., months or years).
#
# The model is trained on the historical data up to a certain point in time (training set), and then it is validated or tested on the data in the subsequent time period (validation or test set).
#
# This process is repeated iteratively by shifting the training and validation periods forward in time until all data points have been considered.
#
# The performance of the model is evaluated at each step, and the results are typically aggregated to assess the model's overall predictive performance.

# %% [markdown] slideshow={"slide_type": "slide"}
# **MLOps: Managing the ML lifecycle with MLflow**
#

# %% [markdown] slideshow={"slide_type": "notes"}
# Who has heard of MLflow? How have used it?

# %% [markdown] slideshow={"slide_type": "fragment"}
# [MLflow](https://mlflow.org/) is an open-source platform for managing the machine learning lifecycle with the following features
# 1. Tracking: MLflow tracks experiments, metrics, parameters, and artifacts for easy comparison and result reproducibility.
# 2. Registry: MLflow's model registry organizes and versions models for collaboration and governance.
# 3. Models: MLflow offers a model management component for packaging models in a standard format and deploying them to various platforms,
# 4. UI and API: MLflow offers a web-based UI and REST API for interactive exploration and programmatic access.
#
# Integrated in DataBricks and 15.5k stars on GitHub (October 2023)
#
# **We will use Mlflow for the project in this course to manage the machine learning lifecycle!**

# %% [markdown] slideshow={"slide_type": "notes"}
# [3 Min]
#
# https://mlflow.org/docs/latest/what-is-mlflow.html
#
# - [MLflow](https://mlflow.org/) is an open-source platform for managing the end-to-end machine learning lifecycle.
# - Developed by DataBrics
# - to provide a consistent way to manage machine learning projects, from data preparation and experimentation to model deployment and monitoring. 
# MLflow offers several key components and features: (Ausschnitt)
# Overall, MLflow is designed to help data scientists and machine learning engineers with tasks such as tracking experiments, sharing code, managing models, and deploying them into production. It provides a unified and agnostic approach to managing the machine learning lifecycle, making it easier to transition from experimentation to production deployment.
# - 

# %% [markdown] slideshow={"slide_type": "slide"}
# **MLflow Demo**

# %% [markdown] slideshow={"slide_type": "fragment"}
# The following code snippet uses `mlflow.autlog` to automatically track the cross-validation of a `RandomForestRegressor` on a diabetes dataset.

# %% slideshow={"slide_type": "-"} code_folding=[]
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

mlflow.autolog()
db = load_diabetes()

def run(): 
    X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)
    rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
    rf.fit(X_train, y_train)
    predictions = rf.predict(X_test)
    
run()

# %% [markdown] slideshow={"slide_type": "subslide"}
# We now start the MLflow tracking server.

# %% slideshow={"slide_type": "-"}
!mlflow ui 

# %% [markdown] slideshow={"slide_type": "-"}
# And open the [MLflow user interface](http://127.0.0.1:5000) (won't work if you are not executing this presentation on your local machine)

# %% [markdown] slideshow={"slide_type": "slide"}
# **Building Apps with Streamlit**
# - Streamlit turns data scripts into shareable web apps in minutes and exhibits the following features.
#     - Rapid Development: Streamlit simplifies web app creation with minimal Python code, ideal for non-web developers.
#     - Interactive Widgets & Real-time Updates: It offers various widgets for easy data and model interaction and enables dynamic data visualization.
#     - Code reuse: Seamlessly integrates with data science libraries (e.g., Pandas, Matplotlib) for code reuse.
# - Trusted by over 80% of Fortune 50 companies and integrated in Snowflake. 27.8k stars on GitHub (October 2023).
# <!--- Not the right tool for complex interfaces and/or nested state.-->
# - Examples: [Analytics Dashoboard](https://shamiraty-streamlit-dashboard-descriptive-analytics-home-5ks7sm.streamlit.app/), [MathGPT](https://mathgpt.streamlit.app/).
#
# **We will be using Streamlit to build an App for the machine learning model of our project!**

# %% [markdown] slideshow={"slide_type": "notes"}
# [2 Min]
# -> Who knows it? Who was worked with it?
#
# Pandas has 40k stars
#
# (we also used streamlit to provide LLMs in our company)
#
# All in pure Python. No front‑end experience required.
#
# Creating web apps entirely in Python is an enticing idea. Setting up a web app requires both frontend and backend skills such as HTML, CSS, JavaScript (and the numerous frameworks) together with Python or some other server-side language on the backend. It’s a lot of work!
#
# If instead everything could be handled entirely in Python, potentially in a single file, the speed of development would increase dramatically. Today, there are several libraries that attempt to deliver this experience. The most popular based on stars on GitHub is Streamlit, with 24.9k stars at the time of writing this.
#
# While Streamlit is incredibly succinct, enabling the creation of web apps in impressively few lines of code, it is not without drawbacks. It has a very limited ability to make customized interfaces, and it has a rather odd mechanism where everything is rerun every time a state is changed

# %% [markdown] slideshow={"slide_type": "notes"}
# Streamlit is an open-source Python library that is used for creating web applications for data science and machine learning projects with minimal effort. It is designed to make it easy for data scientists and engineers to turn data scripts into shareable web apps quickly. Streamlit simplifies the process of creating interactive and data-driven web applications by providing a high-level API and handling many of the underlying web development tasks.
#
# Streamlit is commonly used by data scientists, analysts, and engineers to create data dashboards, interactive data exploration tools, machine learning model demos, and other web applications that showcase and share their data-related work. It has gained popularity due to its simplicity and rapid development capabilities, making it a valuable tool for data science projects and prototyping.

# %% [markdown] slideshow={"slide_type": "slide"}
# **Learning objectives** 
# <br><br>
#
#
# Students will experience the entire Data Science workflow, from defining the task to serving the model via an application or dashboard, through projects. Specifically, students will be able to
#
# - Use cloud services to train a machine learning model.
#
# - Deal with common problems commonly encountered when working with tabular data in practical settings.
# - Recognize the difference between a prediction and a causal inference task and the resulting implications for model building and evaluation.
# - Correctly perform model tuning under temporal dependence and how to do multi-step forecasts.
# - Deploy machine learning models via Streamlit.
#

# %% slideshow={"slide_type": "notes"}

- It focuses on hands-on learning with projects.
- Cloud
- Time Series
- Students learn the fundamentals of manage the machine learning lifecycle with MLflow and AWS Sagemaker.
- Monitor & retrain (?)
- Deploy a App with Streamlit
- Ein Praxisprojekt dass entweder POC -> App oder sogar POC -> Deploy macht.

# %% [markdown] slideshow={"slide_type": "notes"}
# - The data sciene project course deepens and extends
# - - The data science projects course aims to equip students with the skills and knowledge needed to effectively apply data science problemos commonly encountered in practical, professional settings.

# %% slideshow={"slide_type": "notes"}
Bringe mein Praxiswissen ein

# %% [markdown] slideshow={"slide_type": "notes"}
# s is on practical skills, problem-solving, and the ability to use data science tools and methods in practical scenarios, such as those encountered in industry or everyday work situations.
# In essence, a "Data Science Practical" course or program is one that aims to equip students or participants with the skills and knowledge needed to effectively apply data science in practical, professional settings. It often includes hands-on exercises, projects, or case studies to reinforce the practical aspects of data science.

# %% slideshow={"slide_type": "notes"}
This hands-on 


Das Projektstudium zielt darauf ab, die für den beruflichen Alltag als Data Scientist benötigten instrumentalen, systemischen und kommunikativen Kompetenzen zu fördern.

Die Studierenden beherrschen den kompletten Data Science Workflow von der Datensammlung bis zur Modellevaluation. Insbesondere sind die Studierenden in der Lage

ihr Wissen auf auf eine typische Aufgabe aus ihrem Beruf anzuwenden,
im Projekt relevante Informationen zu sammeln, zu bewerten und wissenschaftlich zu reflektieren,
Werkzeuge aus dem Studium einzusetzen, um die Projektziele zu erreichen,
kompetent zu kommunizieren,
fachbezogen zu argumentieren,
sich über Ideen und Lösungen auszutauschen,
sich selbst - allein und im Team - zu organisieren und
Verantwortung im Team zu übernehmen.

# %% slideshow={"slide_type": "notes"}
[1 Min]
or program is geared toward hands-on, real-world application and implementation of data science concepts and techniques. It implies that the emphasis is on practical skills, problem-solving, and the ability to use data science tools and methods in practical scenarios, such as those encountered in industry or everyday work situations.
In essence, a "Data Science Practical" course or program is one that aims to equip students or participants with the skills and knowledge needed to effectively apply data science in practical, professional settings. It often includes hands-on exercises, projects, or case studies to reinforce the practical aspects of data science.

Aim: Connect the dots and fill some holes
Practice focus, give the students a cutting edge
Give students an edge in an increasingly competitive marketplace
Gutes Feedback von den Studierenden, dass das gebraucht wird, Zitat Student „“ und ich habe selber auch die Erfahrung gemacht, dass die Studierenden nicht „business-ready“ sind (nicht so negativ formulieren, eher mehr business ready)
Ich bringen in den Kurs mein Wissen aus vielen Praxisprojekten ein

# %% [markdown] slideshow={"slide_type": "slide"}
# **References**
#
# Bergmeir C., Hyndman R. J., Koo B. "A note on the validity of cross-validation for evaluating autoregressive time series prediction". Computational Statistics & Data Analysis, Volume 120, 2018, Pages 70-83.
# https://doi.org/10.1016/j.csda.2017.11.003.
#
# Guts Y. "Target Leaking in Machine Learning". AI Ukraine Conference 2018. https://www.youtube.com/watch?v=dWhdWxgt5SU
#
# Kapoor, S., Narayanan, A. "Leakage and the reproducibility crisis in machine-learning-based science". Patterns, 100804, August 2023. https://doi:10.1016/j.patter.2023.100804.
#

# %% [markdown] slideshow={"slide_type": "skip"}
# # Obsolete

# %% [markdown] slideshow={"slide_type": "skip"}
# ## Vision/Language/Audio vs. Tabular Data [5 Min] --> Vll. weg

# %% [markdown] slideshow={"slide_type": "skip"}
# ## Causal AI [2 Min] (Bilder von Martin Spindler)
# -> eher nicht, da Inferenz
# Aber vll. Beispiel mit Performance Spielfilm (Kontextwissen)
# oder Effekt Anzahl Runs (Censoring) -> dauert zu lange und schwer zu erklären

# %% [markdown] slideshow={"slide_type": "skip"}
# ## Censoring [2 min] -> vll. weg
