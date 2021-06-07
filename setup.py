import setuptools

setuptools.setup(
    name="PyTab", # Replace with your own username
    version="0.57721",
    author="Katharine Long",
    author_email="katharine.long@ttu.edu",
    description="Tabbing output",
    long_description="Tabbing output in deeply nested code.",
    long_description_content_type="text/markdown",
    url="https://github.com/krlong014/PyTab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: LGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
