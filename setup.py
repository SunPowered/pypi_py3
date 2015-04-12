""" A simple setuptools file """

from setuptools import setup

setup(
    name="PyPi_py3",
    version='0.1 dev',
    description='Ensure proper python3 adherence among pypi package maintainers',
    long_description="""Inspired by Guido's talk at PyCon2015, many packages on the pypi repository are still
                        not Python3 supported.  This project intends to inform these maintainers and provide
                        a mechanism for newer, fresher developer blood to contribute and push forward. """,
    url="https://github.com/SunPowered/pypi_py3",
    author="Tim van Boxtel",
    author_email="tim@vanboxtel.ca",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities"
    ],
    keywords=["python3", "pypi"],
    packages=["pypi_py3"]
)
