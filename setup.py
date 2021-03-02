import setuptools
from CONFIGURATIONS import *

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name=MODULE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email="dev@domcie.net",
    description="CLI tool to convert image folders to PDF files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DomCie/DIRtoPDF",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    install_requires=["PyMuPDF>=1.18"],
)
