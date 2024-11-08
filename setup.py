#//=============================================================
#//Copyright 2024 City of Hope.  
#//All rights reserved – no licenses granted by this publication.
#//=============================================================

from setuptools import setup, find_packages

setup(
    name='bandyt',                   # Your module's name
    version='0.24',                      # Initial release version
    packages=['bandyt'],           # Automatically find packages in your project
    install_requires=[                  # Dependencies
        'numpy',
        'pandas',
        'seaborn',
        'matplotlib',
        'pydot',
        'igraph'
    ],
    description='Bayesian Network Analysis of Dynamic Trajectories',
    long_description=open('README.md').read(),  # Optional: Content of your README file
    long_description_content_type='text/markdown',  # Optional: README file type
    package_data={
        'bandyt': ['ofext.so'],  # Include the precompiled .so file
    },
    include_package_data=True,
    url='https://github.com/bandyt-group/bandyt',  # URL to your GitHub repository
    author='Elizaveta Mukhaleva, Babgen Manookian, Konstancja Urbaniak, Grigoriy Gogoshin, Nagarajan Vaidehi, Andrei Rodin, Sergio Branciamore',
    author_email='bandyt-group@gmail.com',
    classifiers=[                       # Optional metadata
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',            # Minimum Python version requirement
)
