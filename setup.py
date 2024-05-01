""" Install script for pyShortUrl """

import os
import re

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSIONFILE = os.path.join(os.path.dirname(__file__), "_version.py")
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass  # Okay, there is no version file.
else:
    VSRE = r'^__version__ = [\'"]([\w\d\.]+)[\'"]'
    mo = re.search(VSRE, verstrline)
    if mo:
        verstr = mo.group(1)
    else:
        print("Unable to find version in {}".format(VERSIONFILE))
        raise RuntimeError(
            "if {}.py exists, it is required to be " "well-formed".format(VERSIONFILE)
        )

setup(
    name="smart-image-renamer",
    version=verstr,
    author="Ronak Gandhi",
    author_email="ronak.gandhi@ronakg.com",
    description=(
        "A script to intelligently bulk rename images using EXIF data contained within."
    ),
    license="GPLv2",
    keywords="image photo rename bulk smart exif",
    platforms=["Linux", "Max OS X", "Windows", "BSD", "Unix"],
    url="https://github.com/ronakg/smart-image-renamer",
    data_files=[
        (".", ["README.rst"]),
    ],
    packages=[],
    long_description=read("README.rst"),
    scripts=["smart-image-renamer.py"],
    install_requires=["pillow"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Graphics",
        "Topic :: System :: Filesystems",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
