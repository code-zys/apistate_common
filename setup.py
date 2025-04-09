from setuptools import setup, find_packages

setup(
    name="apistate_common",
    version="0.1.24",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "pydantic>=1.8.2",
        "pydantic-settings>=2.0.0",
        "mongoengine>=0.24.0",
        "email-validator>=2.0.0",
        "passlib",
        "bcrypt==4.0.1",
        "python-jose[cryptography]>=3.3.0",
        "requests>=2.32.3"
    ],
    description="Common models and utilities for API State microservices",
    author="Codezys",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)