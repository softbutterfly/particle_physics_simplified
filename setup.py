from setuptools import setup
import sys

requirements = ['h5py','h5hep']

if sys.version_info < (3, 3):
    sys.stdout.write("At least Python 3.3 is required.\n")
    sys.exit(1)
elif sys.version_info < (3, 6):
    # typing was added in 3.5, and we rely on critical features that were
    # introduced in 3.5.2+, so for versions older than 3.6 we rely on
    # a backport
    requirements.append('backports.typing')

#import versioneer

setup(
    name='particle_physics_simplified',
    version="0.9",
    #cmdclass="0.9", # Is this right???
    description='Simple tools for accessing particle physics data for outreach and education',
    url='https://github.com/mattbellis/particle_physics_simplified',
    author='Matt Bellis',
    author_email='mbellis@siena.edu',
    license='GNU General Public License v3.0',
    packages = ['pps_tools'],
    install_requires = ['numpy','h5py','h5hep'],
    #tests_require = ['pytest', 'pytest-cov'],
    classifiers=[ # HAVE TO FIX ALL THIS
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'License :: Public Domain',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
    ],
)
