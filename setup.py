import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="musicgen-Fisher60",
    version="0.0.1",
    author="Kyler Roloff",
    author_email="kyler.roloff@gmail.com",
    description="Tool for getting and parsing musical data such as Keys, Scales, Notes, etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fisher60/musicgen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
