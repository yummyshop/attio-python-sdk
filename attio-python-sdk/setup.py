from setuptools import setup, find_packages

setup(
    name='attio-python-sdk',
    version='0.1',
    author='Yummy OÜ',
    author_email='martin@yummy.eu',
    description='Python SDK for interacting with the Attio API generated with Fern',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-github/attio-python-sdk',
    packages=find_packages(),
    install_requires=[
        'httpx>=0.26.0',  # Specify the correct version based on your SDK's requirements
        'pydantic>=2.5.3',  # Specify the correct version based on your SDK's requirements
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)