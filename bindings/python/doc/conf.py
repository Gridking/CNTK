try:
    import cntk
except ImportError:
    raise ImportError("Unable to import cntk; the cntk module needs to be built "
                      "and importable to generate documentation")

from cntk.sample_installer import module_is_unreleased

try:
    import sphinx_rtd_theme
except ImportError:
    raise ImportError("Unable to import sphinx_rtd_theme, please install via "
                      "'pip install sphinx_rtd_theme'")

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

master_doc = 'index'

exclude_patterns = [
    '_build',
    'cntk_py',
    'tests',
    '**/tests/*',
    '*tests*'
]

needs_sphinx = '1.3'

# TODO nitpick_ignore

project = 'Python API for CNTK'
copyright = '2017, Microsoft'

version = cntk.__version__ # TODO consider shortening
release = cntk.__version__

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Do not prepend the current module to all description unit titles (such as ..
# function::).
add_module_names = False

# The theme to use for HTML and HTML Help pages.
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

source_prefix = 'https://github.com/Microsoft/CNTK/blob/'
if module_is_unreleased():
    # TODO temporary
    source_prefix += 'v%s' % (cntk.__version__[:-1].replace("rc", ".rc"))
else:
    source_prefix += 'master'

# sphinx.ext.extlinks options
extlinks = {
    'cntk': (source_prefix + '/%s', ''),
    'cntktut': (source_prefix + '/Tutorials/%s.ipynb', ''),
    'cntkwiki': ('https://github.com/Microsoft/CNTK/wiki/%s', 'CNTK Wiki - ')
}

# sphinx.ext.napoleon options
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# sphinx.ext.todo options
todo_include_todos = module_is_unreleased()
