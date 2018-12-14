from setuptools import setup

setup(
    name = 'snapshotalyzer-30000',
    version='0.1',
    author="Anuj",
    author_email="anuj@gmail.com",
    desc="Tool to manage aws ec2 instances snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/AnujTagra/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
        '''
)
