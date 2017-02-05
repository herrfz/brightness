from setuptools import setup


setup(
    name='Brightness',
    version='1.0',
    py_modules=['brightness'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        brightness=brightness:cli
    ''',
)
