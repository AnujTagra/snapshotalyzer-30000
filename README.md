# snapshotalyzer-30000
Demo project to manage AWS EC2 instances

# About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots

# Configuration

shotty uses configuration file created by the AWS cli. e.g. -

`aws configure --profile shotty`

# Running

Install pipenv -

`pip3 install pipenv`

Then..

`pipenv run "python shotty/shotty.py"`
