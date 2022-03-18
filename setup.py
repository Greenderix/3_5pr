import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='3_5pr',
    version='0.1',
    scripts=[],
    author="Grinderix",
    author_email="grinderix@yandex.ru",
    description="3_5practice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Greenderix/3_5pr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)
