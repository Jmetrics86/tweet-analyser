# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tweet analytics utility',
    version='0.1.0',
    description='',
    long_description=readme,
    author='Joel Lutman',
    author_email='joellutman@gmail.com',
    url='https://github.com/jhole89/tweet-analyser',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
