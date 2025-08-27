from setuptools import setup

setup(name='TopTrumps',
      version='0.0.1',
      description='Application to play Top Trumps base deck + mods',
      author='CoderDojo Portarlington 2022',
      packages=['toptrumps', 'toptrumps.base_decks', 'toptrumps.config'],
      install_requires=[
          "pyyaml"
      ],
      entry_points={
          'console_scripts': ['app=toptrumps.app:main', ]
      },
      include_package_data=True,
      )
