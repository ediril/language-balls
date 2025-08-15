from setuptools import setup, find_packages

setup(
    name="language-balls",
    version="0.1.0",
    description="Animated language balls moving at different periods",
    author="Emrah Diril",
    author_email="emrah@diril.org",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[
        "dearpygui==1.11.1",
    ],
    entry_points={
        "console_scripts": [
            "language-balls=main:main",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)