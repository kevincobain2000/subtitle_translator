import os
from setuptools import setup, find_packages
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name = 'subtitle_translator',
    version='0.1',
    author='KATHURIA Pulkit',
    author_email='pulkit@jaist.ac.jp',
    packages= find_packages('src'),
    scripts = ['scripts/translate_subs'],
    install_requires = ['mygengo'],
    package_dir = {'':'src'},
    #package_data = {'': ['data/*.*'],
    #},
    include_package_data = True,
    url='http://www.jaist.ac.jp/~s1010205/',
    license='LICENSE.txt',
    description='Subtitle Translator',
    long_description=open('README').read(),
    classifiers=['Development Status :: 2 - Pre-Alpha','Natural Language :: Japanese',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Programming Language :: Python :: 2.6'],
)

