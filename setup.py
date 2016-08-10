# setup.py

from setuptools import setup, find_packages

setup(
    name='nmrstarlib',
    version='1.0.0',
    author='Andrey Smelter',
    author_email='andrey.smelter@gmail.com',
    description='Python library for parsing data from NMR-STAR format files',
    keywords='BMRB NMR-STAR parsing nmrstarlib',
    license='MIT',
    url='', # link pointing to github repo
    packages=find_packages(),
    platforms='any',
    long_description=open('README.rst').read(),
    data_files=[('', ['LICENSE', 'README.rst']), ('conf', ['conf/constants_nmrstar2.json', 'constants_nmrstar3.json'])],
    classifiers=[
        'Development Status :: 1.0.0',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: NMR-STAR Data Parsing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)