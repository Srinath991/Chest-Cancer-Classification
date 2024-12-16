from setuptools import find_packages, setup

# Read the long description from the README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Metadata
__version__ = "0.0.0"
URI = 'https://github.com'
GITHUB_USERNAME = 'Srinath991'
REPO = 'Chest-Cancer-Classification'
AUTHOR = 'Srinath V'
SRC_REPO = 'CNNClassifier'
AUTHOR_EMAIL = 'srinathvsrinatv863@gmail.com'
DESCRIPTION = "A small package for CNN app"
CONTENT_TYPE = 'text/markdown'

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type=CONTENT_TYPE,
    url=f"{URI}/{GITHUB_USERNAME}/{REPO}",
    project_urls={
        'Bug Tracker': f"{URI}/{GITHUB_USERNAME}/{REPO}/issues"
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)
