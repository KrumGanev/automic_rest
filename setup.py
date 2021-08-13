import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="automic_rest",
    version="0.0.5",
    author="ufopilot",
    author_email="xgadme2@gmail.com",
    description="Automic REST-API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ufopilot/automic_rest",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "automic_rest"},
    #packages=setuptools.find_packages(where="automic_rest"),
    packages=['automic_rest'],
    install_requires=['requests'],
    python_requires=">=3.6",
)