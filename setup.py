from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        lines: list = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if len(line) > 0]
        return lines


setup(
    name="useful_utility",
    version="0.1.2",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="SirMrManuel",
    description="Some useful classes and methods",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
