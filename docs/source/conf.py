# Configuration file for the Sphinx documentation builder.

# -- Project information



project = 'Mero Lagani'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    # 'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
]

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
# intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML outputs

html_theme = 'sphinx-rtd-theme'
html_css_files = ["source/custom.css", "css/sphinx_prompt_css.css"]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# conf.py

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 7,
    'includehidden': True,
    'titles_only': False,

}
