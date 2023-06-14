from setuptools import setup

setup(
    name="fraggler",
    version="0.1.0",
    description="Fragment Analysis package in python!",
    url="https://github.com/willros/fraggler",
    author="William Rosenbaum and Pär Larsson",
    author_email="william.rosenbaum@umu.se",
    license="MIT",
    packages=setuptools.find_packages(),
    python_requires='>=3.10',
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "networkx",
        "lmfit",
        "scipy",
        "biopython",
        "panel==0.14.2",
        "fire",
        "openpyxl",
        "colorama",
        "setuptools",
    ],
    entry_points={"console_scripts": ["fraggler=fraggler.cli:run"]},
)
