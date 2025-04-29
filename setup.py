from setuptools import setup, find_packages

setup(
    name="functional_music",
    version="0.1",
    packages=find_packages(),  # Finds everything under app/
    install_requires=[
        "music21",  # Add other dependencies here
    ],
)