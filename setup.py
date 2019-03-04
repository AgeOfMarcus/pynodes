import setuptools
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name='pynodes',
	version='0.0.1',
	description='A python library to simplify nodes and finding peers on the same network.',
	long_description=read("README.md"),
	url='https://github.com/AgeOfMarcus/pynodes',
	author='Marcus Weinberger',
	author_email='marcus@marcusweinberger.com',
	license='GPL',
	packages=setuptools.find_packages(),
	zip_safe=False,
	install_requires=[])
