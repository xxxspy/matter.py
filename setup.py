import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matter",
    version="0.0.1",
    author="Yadong Sun",
    author_email="xxxspy@126.com",
    description="A simple python wrapper for matter.js",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xxxspy/matter.py",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
)