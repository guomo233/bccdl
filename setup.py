import setuptools

setuptools.setup(
	name='bccdl',
	version='0.1.0',
	author='guomo233',
	author_email='gmlihanxi@gmail.com',
	url='https://github.com/guomo233/bccdl',
	description='bilibili CC subtitle downloader',
	packages=['bccdl', 'bin'],
	install_requires=['requests'],
	scripts=['bin/bccdl']
)