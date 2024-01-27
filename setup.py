from setuptools import setup, find_packages

with open('README.md') as description:
    long_description = description.read()

with open('requirements.txt') as requirements:
    install_requires = requirements.read().splitlines()

setup(
    name="pyspark-utilities-pkg",
    version="1.0.0",
    license="MIT",
    author="Adriano M. La Selva",
    author_email="adrianolaselva@gmail.com",
    description="Library responsible for providing additional functions when working with pyspark",
    long_description_content_type='text/markdown',
    long_description=long_description,
    keywords="pyspark, utilities, tests, library",
    url="https://github.com/adrianolaselva/pyspark-utilities-pkg",
    packages=find_packages(where="src", exclude=("tests", "test")),
    package_dir={'': 'src'},
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.8",
    install_requires=install_requires,
)
