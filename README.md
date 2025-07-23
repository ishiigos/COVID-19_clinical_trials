# 🧪 Covid-19 Clinical Trials Analysis

This is a data analytics project on Covid-19 clinical trials! This repository explores the global research response to the pandemic by analyzing trials data sourced from [clinicaltrials.gov](https://clinicaltrials.gov/). Using Python and Tableau, the project uncovers trends in trial phases, intervention types, and sponsoring organizations.

---

## 🎯 Project Goals

- Clean and preprocess real-world Covid-19 clinical trial datasets
- Perform exploratory data analysis (EDA) with statistical and visual insights
- Build a Tableau dashboard for interactive trend exploration
- Identify patterns in trial status, timeline, sponsor landscape, and more
- Set the foundation for future ML and NLP enhancements

---

## 🛠️ Technologies Used

- **Python:** Pandas, NumPy, Seaborn, Matplotlib
- **Jupyter Notebook:** Interactive coding environment
- **Tableau Public:** [Interactive Dashboard](https://public.tableau.com/app/profile/ishita.goswami/viz/Covid-19-clinical-trial-analysis/Dashboard1))
- **Git & GitHub:** Version control and collaboration

---

## 📦 Dataset

The dataset contains detailed information about Covid-19 trials:
- Trial status, country, sponsor, enrollment size
- Study start/end dates, intervention type, and study phase

📥 [Download Dataset on Kaggle](https://www.kaggle.com/datasets/ishiigoswami/covid-19-clinical-trials-data)

> *Note: Raw data not included in the repo due to size and licensing.*

---

## 🛜 Render Live App

- [COVID-19 Clinical Trials Interactive Plots](https://covid-19-clinical-trials.onrender.com)

---

## 📊 Analysis Highlights

- **Trial Status Distribution**: Completed, Recruiting, Withdrawn, etc.
- **Phase-Wise Trends**: Phases I–IV across different regions
- **Intervention Types**: Therapeutics, vaccines, and more
- **Geographical Insights**: Country-wise contributions
- **Sponsor Analysis**: Academic, government, and pharmaceutical players

📂 Visuals include:
- Bar & Line Charts
- Funnel & Choropleth Maps
- Interactive Tableau Filters

---

## 🔍 Key Insights

- 2020–2021 saw the highest spike in clinical trial activity.
- U.S., China, and India led the trial counts globally.
- Many trials remain incomplete or in uncertain statuses.
- Major sponsors include NIH, Pfizer, and academic institutions.
- Most studies focus on respiratory, antiviral, and immune therapies.

---

## 🚀 Future Enhancements

- Predict trial outcomes using machine learning
- NLP analysis of trial descriptions and keywords
- Real-time updates via ClinicalTrials.gov API
- Flask/Streamlit web app for public access and research use

---

## 🧱 Repository Structure
<pre>
COVID-19_clinical_trials/
│
├── app.py
├── Covid_clinical_trial_dataset_cleaned.csv
├── COVID_clinical_trials.csv
├── covid_clinical_trials.ipynb
│
├── plots/
│   ├── Bivariate_Analysis/
│   ├── Country_Distribution/
│   ├── Time_Series_Analysis/
│   ├── Univariate_Analysis/
│   └── wordclouds/
│
├── README.md
├── render.yaml
├── requirements.txt
│
├── tableau_data/
│
└── templates/
    ├── dashboard.html
    ├── wordcloud_conditions.csv
    └── wordcloud_outcomes.csv
</pre>

## 🙏 Credits

- **Dataset**: [ClinicalTrials.gov](https://clinicaltrials.gov/)
- **Dashboard Hosting**: Tableau Public
- Developed as part of a 12-week data analytics internship sprint.

Special thanks to the healthcare professionals, researchers, and open-source contributors who made this possible.

---
