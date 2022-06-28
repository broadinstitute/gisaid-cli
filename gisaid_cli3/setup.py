#!/usr/bin/env python3

"""
    Upload consensus sequences and metadata to GISAID's EpiCoV
    Copyright (C) 2021 Freunde von GISAID e.V.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages
import cli3

LONG_DESCRIPTION = open("README.md").read()

setup(

    name=cli3.__name__,
    version=cli3.__version__,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cli3 = cli3.__main__:main"
        ]
    },

    description=cli3.__description__,
    long_description=LONG_DESCRIPTION,
    classifiers=["Development Status :: 3 - Alpha",
                 "License :: OSI Approved :: GNU Affero General " +
                 "Public License v3 or later (AGPLv3+)",
                 "Programming Language :: Python :: 3.9",
                 "Topic :: Scientific/Engineering :: Bio-Informatics",
                 "Topic :: Scientific/Engineering :: Medical Science Apps.",
                 "Intended Audience :: Science/Research/Public_Health"],
    keywords=["GISAID",
              "upload",
              "consensus",
              "metadata",
              "hCoV-19",
              "SARS-CoV-2",
              "cli3"],
    author=cli3.__author__,
    author_email=cli3.__author_email__,
    license=cli3.__license__,
    package_data={"": ["*.fa*",
                       "*.csv"]},
    install_requires=["requests==2.27.1",
                      "pandas==1.3.5"],
)

# if __name__ == "__main__":
#     setup()
