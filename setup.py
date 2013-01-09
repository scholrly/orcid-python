from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='orcid-python',
      version='0.1',
      description='A simple wrapper around the ORCID.org API.',
      long_description=readme(),
      classifiers=[
                  'Development Status :: 3 - Alpha',
                  'License :: OSI Approved :: MIT License',
                  ],
      url='https://github.com/scholrly/orcid-python',
      author='Matt Luongo',
      author_email='mhluongo@gmail.com',
      license='MIT',
      packages=['orcid'],
      install_requires=[
                      'requests>=1.0.4',
                      'lucene-querybuilder>=0.1.6',
                  ]
     )
