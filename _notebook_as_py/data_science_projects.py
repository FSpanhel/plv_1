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

# %% [markdown]
# # Why does this course exist?

# %% [markdown] slideshow={"slide_type": "slide"}
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

# %%
Personal motivation for DSC and also here (I have a mathematical background and took me some to grasp how to build a product, I would have highly appreciate it if this was clear)
There is a young difference between an ad hoc analysis or building a data product

# %% [markdown] slideshow={"slide_type": "slide"}
# ## In the last years: [Link to Still Sexy, 2 Min, evtl. aber auch verbal aufzählen bei Data Science Project Workflow] 
# - From On-premise to cloud
# - From POC to Production (much more Software Engineering) 
# - No Unicorns but specialized roles (given an Eindruck to these specialized roles)
#   - But it’s likely because the data science role is getting split into multiple different titles. And conveniently cheaper ones. 
#   - ML & Data Engineering role arises
# - Salaries have decreased (More people, and also shift to ML, reddit links, also influenced by recession, Downgrading data scientists to DA, DS -> ML, DS -> DE)
# - Very few junior roles, Demand for senior roles
# - LLMs… (Do we still need DA or people with DL Knowledge, or people how anbinden APIs from the Great Tech Giants?)
#

# %%
[ min]

# %% [markdown] slideshow={"slide_type": "slide"}
# # Data Science Project Workflow [5 Min]

# %%
No differently from any cross-functional project that requires teams to work together! 
Organizations need to determine boundaries between these roles in a way that works for everyone, so there can be clarity about responsibilities. 

- Important to understand how a project looks like
- Data
- Cross-functional team (Stakeholder, Data Sciencist, Sofware Enigeers)

- Nested cross validation (Students were not sicher)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Cloud: AWS [1 min]
# - Interacting with cloud services is a demanded skill for Data Scientist and will even become more important.
# - We will cover the fundamental services of AWS in this course and learn how to
#     - Store and retrieve data, such as files and backups, using **S3**.
#     - Leverage scalable cloud-based compute capacity using **EC2**.
#     - To build, train, and deploy ML models with **Sagemaker**.
# - Optional: Glue & Athena, Lambda functions...
# - How to interact with various AWS services using Python and the **boto3** package.

# %% slideshow={"slide_type": "notes"}
- - Fully managed machine learning service named Amazon SageMaker. It allows the data scientist to run it on EC2. Data scientists use this tool to build, train, deploy machine learning models, and scale business operations

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Time Series [6 Min]

# %% [markdown] slideshow={"slide_type": "notes"}
# - Let's just pick this/go into detail here because we have also spoken about this in the first lecture

# %% [markdown] slideshow={"slide_type": "fragment"}
# **Multi-step forecasts**
#
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
#     \text{Pred}_t[Y_{t+1}] & = a\text{Pred}_t[Y_{t}] + b\text{Pred}_t[X_{t}]\phantom{....}
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
# **These questions will be investigated with a hands-on project in this course.**

# %% [markdown] slideshow={"slide_type": "notes"}
# Certainly, here's a reformulation:
#
# "In practical scenarios, it's common to make predictions for a variable of interest over multiple future time steps. This means that instead of predicting just the next value, you are forecasting a sequence of future values for the variable."

# %% [markdown] slideshow={"slide_type": "slide"}
# **Model tuning** 
#
# - $K$-fold cross-validation is most commonly used to tune the hyperparameters of a model
# - It is typically based on the assumption of iid data.
# - How to do cross-validation when we have temporal dependence?

# %% [markdown] slideshow={"slide_type": "fragment"}
# - $K$-fold cross-validation can be used in [special cases](https://www.sciencedirect.com/science/article/abs/pii/S0167947317302384).
# - In general, cross-validation must consider existing dependence of the data to prevent [data leakage](https://en.wikipedia.org/wiki/Leakage_(machine_learning).
# - Data leakage is a serious problem ncern in academica and industry.
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Model tuning with time series cross-validation**
# 1. Model Training: A predictive model is trained on "in-sample" / training data of length $T_{is}$.
# 2. Validation: The model is scored on "out-of-sample" / validation data of length $T_{oos}$.
# 3. Shifting: The end of the "in-sample" data is increased to $T_{is} + T_{oos}$.
# 4. Repeat Steps 1 - 3 until $T_{oos} = 0$.
# 3. Performance Evaluation: Aggregate "out-of-sample" validation scores.
#
# Questions:
# - How to specify ($T_{is}$, $T_{oos}$) / the resulting folds?
# - How to optimize the training length? Use $(w_tY_t)_{t=1,\ldots T_{is}}$ as training data, where $(w_t)_{t=1}^{T}$ is increasing in $t$ and can be obtained via cross-validation?
# - Should the aggregation of out-of-sample validation scores be weighted equally, or should the results of validation sets closer to today be weighted more heavily?
# - How to actually split the data into folds? 
# <!-- To the best of my knowledge there is no package available that covers important practical cases 
# (split w.r.t. date, a set of time series, groups)
# -->
# **These questions will be investigated with a hands-on project in this course.**

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
# Bild time series cross-validation

# %% [markdown] slideshow={"slide_type": "slide"}
# ## MLflow [3 Min]
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

# %% [markdown] slideshow={"slide_type": "notes"}
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
# An open the [MLflow user interface](http://127.0.0.1:5000) (won't work if you are not executing this presentation on your local machine)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Streamlit [2 Min]
# - Streamlit turns data scripts into shareable web apps in minutes and exhibits the following features.
#     - Rapid Development: Streamlit simplifies web app creation with minimal Python code, ideal for non-web developers.
#     - Interactive Widgets & Real-time Updates: It offers various widgets for easy data and model interaction and enables dynamic data visualization.
#     - Code reuse: Seamlessly integrates with data science libraries (e.g., Pandas, Matplotlib) for code reuse.
# - Trusted by over 80% of Fortune 50 companies and integrated in Snowflake. 27.8k stars on GitHub (October 2023).
# - Not the right tool for complex interfaces and/or nested state.
# - Examples: [Analytics Dashoboard](https://shamiraty-streamlit-dashboard-descriptive-analytics-home-5ks7sm.streamlit.app/), [MathGPT](https://mathgpt.streamlit.app/).

# %% [markdown]
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

# %% [markdown]
# Streamlit is an open-source Python library that is used for creating web applications for data science and machine learning projects with minimal effort. It is designed to make it easy for data scientists and engineers to turn data scripts into shareable web apps quickly. Streamlit simplifies the process of creating interactive and data-driven web applications by providing a high-level API and handling many of the underlying web development tasks.
#
# Streamlit is commonly used by data scientists, analysts, and engineers to create data dashboards, interactive data exploration tools, machine learning model demos, and other web applications that showcase and share their data-related work. It has gained popularity due to its simplicity and rapid development capabilities, making it a valuable tool for data science projects and prototyping.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Learning objectives (oder am Ende?) [1 Min]
# - Hands-on Learning with procjets
# - Cloud
# - Time Series
# - Manage machine learning lifecycle with MLflow
# - Monitor & retrain (?)
# - Deploy a App with Streamlit

# %% [markdown] slideshow={"slide_type": "slide"}
# # References
# https://www.sciencedirect.com/science/article/abs/pii/S0167947317302384
#
# https://www.youtube.com/watch?v=dWhdWxgt5SU
#
#  Kapoor, Sayash; Narayanan, Arvind (August 2023). "Leakage and the reproducibility crisis in machine-learning-based science". Patterns: 100804. doi:10.1016/j.patter.2023.100804. ISSN 2666-3899.
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
