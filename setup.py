import os

from setuptools import find_packages, setup


# Function to read the README file
def read_readme():
    with open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"),
        encoding="utf-8",
    ) as f:
        return f.read()


# Get package version (assuming you'll define it in pynolad/__init__.py)
# This is a common practice to have the version in one place
def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.0.1"
            return line.split('"')[1]
    raise RuntimeError("Unable to find version string.")


# Assuming you have a __version__ = "X.Y.Z" in pynolad/__init__.py
# Or you can hardcode the version here for simplicity initially
# version = "0.0.1" # Example hardcoded version


# This is a safer way to read from files within the package
def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


# --- Setup configuration ---
setup(
    name="pynolad",  # The name your package will be installed as (must be unique on PyPI)
    version=get_version("pynolad\__init__.py"),  # Or use the hardcoded version
    author="Ido Badash",  # Your name or your organization's name
    author_email="idoba12012011@gmail.com",
    description="A simple Pygame engine/framework for game development.",  # Short description
    long_description=read_readme(),  # Long description from README.md
    long_description_content_type="text/markdown",  # Specify content type if using Markdown
    url="https://github.com/Ido-Badash/pynolad",  # Link to your project's GitHub repo
    packages=find_packages(),  # Automatically finds your pynolad directory as a package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",  # Or 4 - Beta, 5 - Production/Stable
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.8",  # Minimum Python version required
    install_requires=[
        "pygame>=2.0.0",  # Specify dependencies
        # Add other dependencies here if your library uses them
    ],
    # If your package includes non-Python files (like images, sound, etc.)
    # package_data={
    #     'pynolad': ['assets/*.png'], # Example: include assets folder
    # },
    # include_package_data=True, # Set to True if you use package_data
)
