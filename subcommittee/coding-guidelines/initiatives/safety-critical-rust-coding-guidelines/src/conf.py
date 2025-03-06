# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Safety-Critical Rust Coding Guidelines'
copyright = '2025, Contributors to Coding Guidelines Subcommittee'
author = 'Contributors to Coding Guidelines Subcommittee'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add sphinx-needs to extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_needs'
]

# Basic needs configuration
needs_id_regex = "^[A-Z0-9_]+"
needs_build_json = True

# Define the part types
needs_part_types = [
    {
        "name": "recommendation",
        "title": "Recommendation",
        "color": "#FEDCD2",
        "prefix": "REC_"
    },
    {
        "name": "rationale",
        "title": "Rationale",
        "color": "#DF744A", 
        "prefix": "RAT_"
    },
    {
        "name": "example",
        "title": "Example",
        "color": "#BFD8D2",
        "prefix": "EX_"
    }
]

# Configure sphinx-needs
needs_types = [
    {
        "directive": "guideline",
        "title": "Guideline",
        "prefix": "G_",
        "color": "#BFD8D2", 
        "style": "node"
    },
    {
        "directive": "recommendation",
        "title": "Recommendation",
        "prefix": "REC_",
        "color": "#FEDCD2", 
        "style": "node"
    },
    {
        "directive": "rationale",
        "title": "Rationale",
        "prefix": "RAT_",
        "color": "#DF744A", 
        "style": "node"
    },
    {
        "directive": "example",
        "title": "Example",
        "prefix": "EX_",
        "color": "#729FCF", 
        "style": "node"
    }
]

needs_statuses = [
    dict(name="draft", description="This guideline is in draft stage", color="#999999"),
    dict(name="proposed", description="This guideline is proposed for review", color="#FFCC00"),
    dict(name="approved", description="This guideline has been approved", color="#00FF00"),
    dict(name="deprecated", description="This guideline is deprecated", color="#FF0000"),
]

needs_tags = [
    dict(name="security", description="Security-related guideline"),
    dict(name="performance", description="Performance-related guideline"),
    dict(name="readability", description="Readability-related guideline"),
    dict(name="human-error", description="Reducing human error guideline"),
]

needs_recommendations = [
    dict(name="encouraged", description="This guideline is encouraged", color="#999999"),
    dict(name="required", description="This guideline is required", color="#FFCC00"),
]

# Enable needs export
needs_extra_options = ["category", "recommendation"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Configure the theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
