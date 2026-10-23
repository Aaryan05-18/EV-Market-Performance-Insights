"""
Electric Vehicle Market Performance & Insights - Flask app.

Flask only serves the page. All interactive charts come from the
Tableau Public dashboard embedded in templates/index.html.
"""
import os

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------
# EASY-TO-EDIT SETTINGS
# ---------------------------------------------------------------

# Published Tableau Public dashboard. You can also override it without editing
# code by setting the TABLEAU_URL environment variable.
TABLEAU_URL = os.environ.get(
    "TABLEAU_URL",
    "https://public.tableau.com/app/profile/aaryan.chauhan2168/viz/Project1_17927337476780/Dashboard3",
)
TABLEAU_PROFILE_URL = "https://public.tableau.com/app/profile/aaryan.chauhan2168/vizzes"

PROJECT = {
    "title": "Electric Vehicle Market Performance & Insights",
    "author": "Aaryan Chauhan",
}

# Dataset summary values (taken from your dataset, NOT verified real-world totals).
# To update a KPI, change "value" or "unit" here and refresh the page.
KPIS = [
    {"label": "EV models in dataset", "value": "199,999", "unit": ""},
    {"label": "Manufacturers in dataset", "value": "200", "unit": ""},
    {"label": "Average driving range", "value": "324.5", "unit": "km"},
    {"label": "Average customer rating", "value": "4.089", "unit": "/ 5"},
    {"label": "Average battery capacity", "value": "78.24", "unit": "kWh"},
]

OBJECTIVES = [
    "Understand how EV models are distributed across categories, manufacturers, battery types and manufacturing countries.",
    "Explore how customer ratings and annual sales vary across the dataset.",
    "Examine how price, battery capacity and driving range relate to one another.",
    "Compare efficiency across EV categories.",
]

QUESTIONS = [
    "Which EV categories and manufacturers have the most models in the dataset?",
    "How do customer ratings differ between categories or manufacturers?",
    "How do annual sales change by model year?",
    "Does a higher price go with a longer driving range?",
    "Does a larger battery capacity go with a longer driving range?",
    "Which categories are the most efficient?",
]

GUIDE = [
    ("EV category distribution", "How the models split across vehicle categories."),
    ("Manufacturer model counts", "How many models each manufacturer has in the dataset."),
    ("Customer ratings", "How ratings are spread across models, categories or makers."),
    ("Annual sales by model year", "Sales totals grouped by model year."),
    ("Battery-type distribution", "Which battery types appear and how often."),
    ("Manufacturing-country distribution", "Where the models in the dataset are made."),
    ("Price vs. range", "The relationship between price and driving range."),
    ("Battery capacity vs. range", "The relationship between battery size and driving range."),
    ("Efficiency by category", "How efficiency compares across categories."),
]

TECH_STACK = [
    ("Tableau Public", "Data visualisation and the interactive dashboard"),
    ("Tableau Embedding API v3", "Shows the published dashboard on this page"),
    ("Python and Flask", "Serves the web page"),
    ("HTML5, CSS3, JavaScript", "Layout, styling and the dashboard loading state"),
]

LIMITATIONS = [
    "Model counts describe this dataset only. They are not automatically real-world market share.",
    "Correlation does not prove causation. A pattern between price, battery and range does not show that one causes the other.",
    "Averages can hide differences between categories, manufacturers and years.",
    "Summary values on this page are copied from the dataset and may differ from official industry figures.",
]


@app.route("/")
def index():
    """Render the single-page project site."""
    return render_template(
        "index.html",
        project=PROJECT,
        kpis=KPIS,
        objectives=OBJECTIVES,
        questions=QUESTIONS,
        guide=GUIDE,
        tech_stack=TECH_STACK,
        limitations=LIMITATIONS,
        tableau_url=TABLEAU_URL,
        profile_url=TABLEAU_PROFILE_URL,
    )


@app.errorhandler(404)
def not_found(_error):
    """Friendly 404 page that sends visitors back home."""
    return (
        "<h1>Page not found</h1><p><a href='/'>Back to the project</a></p>",
        404,
    )


@app.errorhandler(500)
def server_error(_error):
    """Safe 500 message: never show internal details to visitors."""
    return "<h1>Something went wrong</h1><p><a href='/'>Try again</a></p>", 500


if __name__ == "__main__":
    # debug=True is for local learning only. Turn it off before any public deployment.
    app.run(host="127.0.0.1", port=5000, debug=True)