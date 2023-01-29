from setuptools import setup, find_packages
import os
import codecs

hs=os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(hs,'README.md'),encoding='utf-8') as fh:
    long_description = "\n" + fh.read()

DS = 'Report Finance of Companies in Vietnamese'

#Setting
setup(
    name='RStock',
    version='0.1.0',
    author='NGUYEN PHUC BINH',
    author_email='nguyenphucbinh67@gmail.com',
    description=DS,
    packages=find_packages(),
    install_requires=['pandas','requests','json'],
    keywords=['RStockvn','rstockvn','report stock vn'],
    url='https://github.com/NPhucBinh/RStockvn',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",]
)