import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="td_install",
    version="0.0.2",
    author="Frederick Morlock",
    author_email="FrederickGeek8@gmail.com",
    description="Tokyo Dark macOS port creation tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['future', 'patch==1.*', 'progressbar2'],
    url="https://github.com/FrederickGeek8/td_install",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Environment :: MacOS X",
    ),
    entry_points={
        'console_scripts': [
            'td_install = td_install.__main__:main',
            'td_debug = td_install.__main__:debug'
        ]
    },
    platforms="MacOS X",
    license="MIT License",
    include_package_data=True
)
