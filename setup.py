from setuptools import setup, find_packages

with open('requirements.txt', 'r') as _f:
    requirements = [line for line in _f.read().split('\n')]

setup(
    name='summarize',
    description='demo python CLI tool to summarize text using HuggingFace',
    packages=find_packages(),
    author='Alfredo Deza',
    entry_points="""
    [console_scripts]
    summarize=summarize.main:main
    """,
    install_requires=requirements,
    version='0.0.1',
    url='https://github.com/alfredodeza/huggingface-summarization',
)
