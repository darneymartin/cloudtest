from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cloudtest',
    version='0.1',
    author = 'darneymartin',
    author_email = 'darnellrmartin91@gmail.com',
    description = 'Tool that can be used to test AWS cloud infrastructure.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/darneymartin/cloudtest',
    license='GNU General Public License v3.0',
    classifiers = [
        "Environment :: Console",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers"
    ],
    packages=['cloudtest'],
    install_requires = ['boto3']
)
