from setuptools import setup, find_packages

setup(
    #  name of your project.
    name='owis',
    # Versions
    version='0.1',
    packages=find_packages(include=['owis', 'core','example','tests']),
    #  project's main homepage.
    url='https://github.com/aasyria/owis',
    license='me an leni',
    author='almosaiki - leni',
    author_email='almokhtar.wap@gmail.com',
    # This is a one-line description
    description='local network scanner',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': ['owis = owis.core.app:scan']
    }
)
