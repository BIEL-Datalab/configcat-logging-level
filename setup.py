from setuptools import find_packages, setup

setup(
    name="biel_configcat_logging_level",
    description="Setting logging level dynamically with ConfigCat",
    author="biel-huangchunqi",
    author_email="huangcq1@bielcrystal.com",
    url="https://github.com/BIEL-Datalab/configcat-logging-level",
    packages=find_packages(),
    install_requires=[
        "certifi==2022.6.15",
        "charset-normalizer==2.1.0",
        "configcat-client==6.0.3",
        "enum-compat==0.0.3",
        "idna==3.3",
        "pydantic==1.9.1",
        "requests==2.28.1",
        "semver==2.13.0",
        "typing_extensions==4.3.0",
        "urllib3==1.26.10",
    ],
)
