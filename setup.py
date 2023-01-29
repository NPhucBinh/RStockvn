from setuptools import setup, find_packages
import os
import codecs

hs=os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(hs,'README.md'),encoding='utf-8') as fh:
    long_description = fh.read()

DS = 'Report Finance of Companies in Vietnamese'

#Setting
setup(
    name='RStockvn',
    version='0.1.2',
    author='NGUYEN PHUC BINH',
    author_email='nguyenphucbinh67@gmail.com',
    description=DS,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url="https://github.com/NPhucBinh/RStockvn",
    install_requires=['pandas','requests','json'],
    keywords=['RStockvn','rstockvn','report stock vn'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",]
)