from setuptools import setup, find_packages

setup(
    name="customer-segmentation-mlops",
    version="1.0.0",
    description="Customer Segmentation MLOps Platform",
    author="Blandine JATSA NGUETSE",
    author_email="blandinenguetse@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.3.1",
        "numpy>=2.3.2",
        "scikit-learn>=1.6.1",
        "mlflow>=3.1.4",
        "fastapi>=0.116.1",
        "streamlit>=1.47.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
