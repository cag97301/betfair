from betfairlightweight.__init__ import __version__
from distutils.core import setup, Extension


setup(
        name='betfairlightweight',
        version=__version__,
        packages=['betfairlightweight', 'betfairlightweight.errors', 'betfairlightweight.parse'],
        package_dir={'betfairlightweight': 'betfairlightweight'},
        requires=['requests'],
        url='https://github.com/LiamPa/betfairlightweight',
        license='',
        author='liampauling',
        author_email='',
        description='Lightweight python wrapper for Betfair API-NG'
)
