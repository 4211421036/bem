from setuptools import setup, find_packages

setup(
    name="plasmonmode",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20.0',
        'scipy>=1.7.0',
    ],
    author="GALIH RIDHO UTOMO",
    author_email="g4lihru@students.unnes.ac.id",
    description="Python implementation of plasmon eigenmodes computation",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/4211421036/bem",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
