from setuptools import setup, find_packages

setup(
    name="wcp-cli",
    version="0.1",
    packages=find_packages(),
    install_requires=["click", "requests"],
    entry_points={
        "console_scripts": [
            "wcp=wcp_cli.main:cli",
        ]
    },
)