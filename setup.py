## FILE: setup.py

from setuptools import setup, find_packages

setup(
    name='mtDNA-annotator',
    version='0.1',
    description='Batch mtDNA variant annotation tool using HmtVar, MITOMAP, gnomAD, and ClinVar.',
    author='Shasan',
    author_email='you@example.com',
    url='https://github.com/ngshasan/mtDNA-annotator',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'tqdm',
        'beautifulsoup4',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'mtdna-annotate=mtDNA_annotator.core:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.7',
)

