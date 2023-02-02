from setuptools import setup, find_packages
import os
import codecs

hs=os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(hs,'README.md'),encoding='utf-8') as fh:
    long_description = fh.read()

DS = 'Report Finance of Companies in Vietnamese and macro data - Lấy báo cáo tài chính của các công ty ở Việt Nam và số liệu vĩ mô'

#Setting
setup(
    name='RStockvn',
    version='1.0.3',
    author='NGUYEN PHUC BINH',
    author_email='nguyenphucbinh67@gmail.com',
    description=DS,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url="https://github.com/NPhucBinh/RStockvn",
    install_requires=['pandas','requests','jsonschema','bs4'],
    keywords=['RStockvn','rstockvn','report stock vn','báo cáo tài chính việt nam','lấy báo cáo tài chính việt nam bằng python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",]
)