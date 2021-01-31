import setuptools
from N4Tools import __version__

with open('README.md', 'r') as fh:
    long_description = fh.read()
with open('requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setuptools.setup(
    name='N4Tools',
    version=__version__,
    author='Mohamed Al-Kainai',
    author_email='mohamedalkainai@gmail.com',
    description='Style for linux tools.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/No-Name-404/N4Tools',
    packages=['N4Tools'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License'],
    install_requires=requires,
)