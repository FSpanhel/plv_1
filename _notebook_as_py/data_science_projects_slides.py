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
# **Anmerkungen zur Bedienung der interaktiven Präsentation**
#
# - Die Vortragspräsentation ist als interaktive [Rise](https://rise.readthedocs.io/en/latest/) Präsentation konzeptioniert.
#
# - Um die interaktive Präsentation zu starten, öffnen Sie bitte die URL https://tinyurl.com/fs-plv2 in ihrem Browser.
# <!-- oder scannen den QR Code -> kann ja das dann nicht bedienen? -->
# - Es kann ein wenig dauern, bis die Präsentation gestartet wird.
# - Falls die Präsentation nicht automatisch startet und Sie ein Jupyter notebook sehen, bitte laden Sie die Seite neu.
# - Die interaktive Präsentation kann mittels der Navigationspfeile oder wie folgt bedient werden:
#     - `Leertaste`: Eine Folie weiter.
#     - `Hochstelltaste + Leertaste`: Eine Folie zurück.
#     - `Strg + Enter`: Laden eines interaktiven Plots.
#     - `Alt + r`: Aktivieren bzw. Deaktivieren der Präsentation.
#     - Falls ein interaktive Plot bei Ausführung einer Code Zelle nicht richtig positioniert ist, deaktiviere und aktiviere Sie die Präsentation indem sie zwei Mal `Alt + r` drücken.

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
# 1. Welcome to my second presentation which is about data science projects.
# 2. Data science projects is a lecture that is targeted at master students who like to work in the data science domain.
# 3. This lecutre is the follow-up **to** the lecture Data Science Challenge / Projekt which I lecture at the moment for the bachelor students of Data Science and scientific computing.
# 4. Just like DVC this lecture emphasis is on practical skills, problem-solving, and the ability to use data science tools and methods in practical scenarios.
# 5. For this purpose, this course provides hands-on projects and case studies.

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

# %% [markdown] slideshow={"slide_type": "notes"}
# 1. What practical skills should students or graduates have these days?
# 2. Well, let's take a look back at the last seven years that have passed since I've been working in the industry.
# 3. First of all, the tools with which data scientist work have changed a lot. Ten years ago, it was like the wild west and there were few tools and standards available.
#     - Most importantly, analytics as well as development and management of ML models have largely shifted to the cloud for several reasons.
# 4. Relatively speaking, there are less POCs and more models are put into production and need to be managed. As a consequence, software engineering becomes more crucial.
# 5. Previously, a data scienctist was a unicorn, meaning they did all required tasks — from conceptualizing the use case, to 
# interfacing with business and technology stakeholders, to developing the algorithm and deploying it into production. 
# While this may still be true, there is a **continued differentiation of responsibilities**. Like **machine learning engineers**, **data engineers**, **advanced analytics**, and **data oriented product managers**.

# %% [markdown] slideshow={"slide_type": "fragment"}
# See also ["**Is Data Scientist Still the Sexiest Job of the 21st Century?**"](https://hbr.org/2022/07/is-data-scientist-still-the-sexiest-job-of-the-21st-century)
#
# **The goal of this course is to address the changes that have occurred in recent years and provide students with skills that might gain them a competitive advantage.**

# %% [markdown] slideshow={"slide_type": "slide"}
# **Data Science Project Workflow**
# <img src="./figures/ds_project_0.png" alt="Data Science Projects" style="width: 1600px;"/>

# %% [markdown] slideshow={"slide_type": "notes"}
# 1. In general, a data science project is often a cross-functional project that requires team to work together.
#     1. On the left hand side we have the business intelligence or analytics people, or people with a math/stats background (blue) and on the right we have people with an information science background or software engineers (green).
#     1. This color gradient should highlight that boundaries between these roles are not strict and evolving.

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Data Science Project Workflow**
# <img src="./figures/ds_project_1.png" alt="Data Science Projects" style="width: 1600px;"/>

# %% [markdown] slideshow={"slide_type": "notes"}
# 1. The center of a data science project is data.
# 1. This data is used to kick-off a POC or to do an ad hoc analysis.

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Data Science Project Workflow**
# <img src="./figures/ds_project_2.png" alt="Data Science Projects" style="width: 1600px;"/>

# %% [markdown] slideshow={"slide_type": "notes"}
# 1. The outcome of this POC or ad hoc analysis could be a report/app.
# 1. Or it could be deployment and management of a machine learning model.
#     1. This model could also then end in an app or dashboard.

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Data Science Project Workflow**
# <img src="./figures/ds_project_3.png" alt="Data Science Projects" style="width: 1600px;"/>

# %% [markdown] slideshow={"slide_type": "notes"}
#
#
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

# %% [markdown] slideshow={"slide_type": "slide"}
# **AWS Cloud services**
#
# - Interacting with cloud services is a demanded skill for Data Scientists and will become even more important.
#
# - We will cover the fundamental services of AWS in this course and learn how to
#     - Store and retrieve data, such as files and backups, using **S3**.
#     - Leverage scalable cloud-based compute capacity using **EC2**.
#     - To build, train, and deploy ML models with **Sagemaker**.
# - Optional: Glue & Athena, Lambda functions...
# - How to interact with various AWS services using Python and the **boto3** package.
#
# **We will be using AWS for the hands-on project in this course!**

# %% [markdown] slideshow={"slide_type": "slide"}
# **Methodology: Model tuning for time series** 
#
# - $K$-fold cross-validation is most commonly used to tune the hyperparameters of a model.
# - It is typically based on the assumption of iid data.
# - How to do cross-validation when we have temporal dependence?

# %% [markdown] slideshow={"slide_type": "fragment"}
# - $K$-fold cross-validation can be used in [special cases](https://www.sciencedirect.com/science/article/abs/pii/S0167947317302384).
# - In general, cross-validation must consider existing dependence of the data to prevent [data leakage](https://en.wikipedia.org/wiki/Leakage_(machine_learning).
# - Data leakage is a [serious problem in academica and industry](doi:10.1016/j.patter.2023.100804).
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Model tuning with time series cross-validation**
#
# - Model training: A predictive model is trained on training data of length $T_{train}$.
# - Validation: The model is scored on validation data of length $T_{val}$.
# - Shifting: The end of the new training data is increased to $T_{train} + T_{val}$.
# - Repeat Steps 1 - 3 until $T_{val} = 0$.
# - Performance evaluation: Aggregate validation scores.
#
# Questions:
# - How to specify ($T_{train}$, $T_{val}$) or the resulting folds?
# - How to optimize the training length? Use $(w_tY_t)_{t=1,\ldots T_{train}}$ as training data, where $(w_t)_{t=1}^{T}$ is increasing in $t$ and can be obtained via cross-validation?
# - Should the aggregation of validation scores be weighted equally, or should the results of validation sets closer to today be weighted more heavily?
# - How to actually split the data into folds?
#
# **These questions will be investigated with a hands-on project in this course!**

# %% [markdown] slideshow={"slide_type": "slide"}
# **MLOps: Managing the ML lifecycle with MLflow**
#

# %% [markdown] slideshow={"slide_type": "fragment"}
# [MLflow](https://mlflow.org/) is an open-source platform for managing the machine learning lifecycle with the following features
# 1. **Tracking**: MLflow tracks experiments, metrics, parameters, and artifacts for easy comparison and result reproducibility.
# 2. **Registry**: MLflow's model registry organizes and versions models for collaboration and governance.
# 3. **Models**: MLflow offers a model management component for packaging models in a standard format and deploying them to various platforms.
# 4. **UI and API**: MLflow offers a web-based UI and REST API for interactive exploration and programmatic access.
#
# Integrated in DataBricks and 15.5k stars on GitHub (October 2023)
#
# **We will use Mlflow for the project in this course to manage the machine learning lifecycle!**

# %% [markdown] slideshow={"slide_type": "notes"}
# Who knows MLflow?

# %% [markdown] slideshow={"slide_type": "slide"}
# **MLflow Demo**

# %% [markdown] slideshow={"slide_type": "fragment"}
# The following code snippet uses `mlflow.autolog` to automatically track the cross-validation of a `RandomForestRegressor` on a diabetes dataset.

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
#     - **Rapid Development**: Simplifies web app creation with minimal Python code, ideal for non-web developers.
#     - **Code reuse**: Seamlessly integrates with data science libraries (e.g., Pandas, Matplotlib) for code reuse.
#     - **Interactive Widgets & Real-time Updates**: Offers various widgets for easy data and model interaction and enables dynamic data visualization.
#
# - Trusted by over 80% of Fortune 50 companies and integrated in Snowflake. 27.8k stars on GitHub (October 2023).
# <!--- Not the right tool for complex interfaces and/or nested state.-->
# - Examples: [Analytics Dashoboard](https://shamiraty-streamlit-dashboard-descriptive-analytics-home-5ks7sm.streamlit.app/), [MathGPT](https://mathgpt.streamlit.app/).
#
# **We will be using Streamlit to build an App for the machine learning model of our project!**

# %% [markdown] slideshow={"slide_type": "notes"}
# Who knows Streamlit?

# %% [markdown] slideshow={"slide_type": "slide"}
# **Learning objectives** 
# <br>
#
# Students will experience the entire **Data Science workflow**, from defining the task to serving the model via an application or dashboard, through projects. 
#
# - Deal with common problems when working with **tabular data**.
#
# - Differentiate between **prediction** and **causal inference** tasks.
# - Utilize **cloud services** for model training.
# - Tackle model tuning in the presence of **temporal dependence** and perform multi-step forecasts.
# - **Track** models with MLflow.
# - **Deploy** machine learning models using Streamlit.
#
#

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
