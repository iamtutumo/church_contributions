from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in church_contributions/__init__.py
from church_contributions import __version__ as version

setup(
    name="church_contributions",
    version='0.0.1',
    description="Church Contribution System for Anglican Church",
    author="Tutu Moses",
    author_email="etu.moses@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
