from setuptools import setup, find_packages
import os

version = '0.5'

setup(name='uwosh.emergency.client',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Nathan Van Gheem',
      author_email='vangheem@gmail.com',
      url='http://svn.plone.org/svn/plone/plone.example',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uwosh', 'uwosh.emergency'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'uwosh.simpleemergency>=1.1',
          'rsa'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [zc.buildout]
      default = uwosh.emergency.client.recipe:Recipe
      
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
