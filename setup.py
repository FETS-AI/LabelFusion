#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
  readme = readme_file.read()

requirements = [
  'numpy==1.19.4',
  'SimpleITK==2.0.2',
  'setuptools',
  'wheel',
  'twine',
  'keyring'
]

setup(
  name='LabelFusion',
  version='1.0.11', # dev: development release; this should be changed when tagging
  author="Megh Bhalerao, Sarthak Pati",
  author_email='software@cbica.upenn.edu',
  python_requires='>=3.6',
  packages=find_packages(),
  scripts=['fusion_run'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  description=(
    "Label fusion strategies for multi-class labels."
  ),
  url='https://github.com/FETS-AI/LabelFusion',
  install_requires=requirements,
  license="BSD-3-Clause License",
  long_description=readme,
  long_description_content_type='text/markdown',
  include_package_data=True,
  keywords='semantic, segmentation, label-fusion, fusion',
  zip_safe=False,
)
