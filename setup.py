import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymetric",
    version="0.0.1",
    author="Clivern",
    author_email="hello@clivern.com",
    description="A Python Package to unify time series data sources.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gobadger/pymetric",
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)