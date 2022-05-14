import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fivesimapi",
    version="0.1.3",
    author="Subrata",
    author_email="",
    description="Five sim api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Subrata2402/fivesimapi",
    #entry_points={'console_scripts': ['HQApi = HQApi.hq_api_cli:main']},
    install_requires=['aiohttp'],
    packages=["FiveSimApi"],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
