from setuptools import setup, find_packages
import io

with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="RBXWireNet",
    version="0.1.0",
    author="WiseDodge",
    author_email="",
    description="Modular Python client for Roblox Open Cloud APIs enabling correlational data extraction from groups, users, and games.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WiseDodge/RBXWireNet",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.28.0",
        "python-dotenv>=1.0.0"
    ],
    tests_require=[
        "pytest>=7.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
