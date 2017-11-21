from setuptools import find_packages
from setuptools import setup

setup(name='GitImport',
      version="0.1",
      description="Import extension from github directly.",
      author='Pascal van Kooten',
      url='https://github.com/bennyelg/git_import',
      author_email='elgazarbenny@gmail.com',
      install_requires=[
          'gitpython'
      ],
      # entry_points={
      #     'console_scripts': ['just = just.__main__:main']
      # },
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
      ],
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      platforms='any')
