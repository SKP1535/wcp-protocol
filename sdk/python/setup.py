from setuptools import setup, find_packages

setup(
    name="wcp",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    description="Python SDK for Work Coordination Protocol",
)