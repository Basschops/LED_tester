# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()
 
with open('LICENSE') as f:
    license = f.read()

setup(
    name='solved_led',
    version='0.1.0',
    description='Program to set up and test light grid',
    long_description=readme,
    author='Daragh OFarrell',
    author_email='daragh.ofarrell@ucdconnect.ie',
    url='https://github.com/Basschops/LED_tester.git',
    license=license,
    packages=find_packages(include=['LightUp','tests']),
    entry_points={
        'console_scripts': [
            'solved_led = LightUp.Lights:construct',
        ],
    },    
    
    #install_requires=requirements.txt,
    zip_safe=False,
    keywords='solved_led',
    #test_suite='tests',
#     tests_require=test_requirements,
#     setup_requires=setup_requirements,
    
    )