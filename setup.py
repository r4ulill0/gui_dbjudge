import os
import setuptools

setuptools.setup(
    name="sql_judge_gui",
    version="1.1.1a0",
    author="Raúl Medina",
    author_email="raulmgcontact@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=[
        'pyqt5',
        'dbjudge'
    ],
    package_data={
        '': ['*.ini']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
