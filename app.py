from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly
import json

app = Flask(__name__)

# Load data
df = pd.read_csv('Covid_clinical_trial_dataset_cleaned.csv')

# Clean and preprocess columns
df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
df['Country'] = df['Locations'].str.extract(r'(\b[A-Z][a-z]+(?: [A-Z][a-z]+)*$)').fillna('Unknown')
df['Sponsor'] = df['Sponsor/Collaborators'].str.strip()

# === Plotly Figures ===

# 1. Trials over time (monthly)
monthly_counts = df['Start Date'].dt.to_period('M').value_counts().sort_index()
monthly_counts.index = monthly_counts.index.to_timestamp()
fig_time = px.line(x=monthly_counts.index, y=monthly_counts.values,
                   labels={'x': 'Month', 'y': 'Number of Trials'},
                   title='Trials Started Over Time')

# 2. Top 10 countries
top_countries = df['Country'].value_counts().nlargest(10)
fig_country = px.bar(x=top_countries.values, y=top_countries.index,
                     orientation='h',
                     labels={'x': 'Trials', 'y': 'Country'},
                     title='Top 10 Countries')

# 3. Top 10 sponsors
top_sponsors = df['Sponsor'].value_counts().nlargest(10)
fig_sponsor = px.bar(x=top_sponsors.values, y=top_sponsors.index,
                     orientation='h',
                     labels={'x': 'Trials', 'y': 'Sponsor'},
                     title='Top 10 Sponsors')

# Convert figures to JSON for embedding
graphs = {
    'fig_time': json.dumps(fig_time, cls=plotly.utils.PlotlyJSONEncoder),
    'fig_country': json.dumps(fig_country, cls=plotly.utils.PlotlyJSONEncoder),
    'fig_sponsor': json.dumps(fig_sponsor, cls=plotly.utils.PlotlyJSONEncoder)
}

@app.route("/")
def dashboard():
    return render_template("dashboard.html", graphs=graphs)

if __name__ == "__main__":
    app.run(debug=True)