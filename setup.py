from setuptools import setup, find_packages

setup(
    name="mock_echo_pwned",
    version="0.1",         
    packages=find_packages(),    # Automatically find packages in the directory
    description="A simple package for echoing",
    url="https://github.com/yourusername/myrepo",  # Repository URL if hosted (e.g., GitHub)
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)

