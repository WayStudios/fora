import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'lingua',
    'hashids',
    ]

setup(name='fora',
      version='0.0',
      description='fora',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Xu',
      author_email='xw901103@gmail.com',
      url='https://github.com/WayStudios/fora',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='fora',
      install_requires=requires,
      entry_points="""\
      [fora.scaffold]
      generic = fora.scaffolds:GenericInstanceTemplate
      [paste.app_factory]
      main = fora:main
      [console_scripts]
      initialize_fora_db = fora.scripts.initializedb:main
      create_fora_instance = fora.scripts.createinstance:main
      """,
      )
