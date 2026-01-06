# ci-github-actions-demo
for ci lesson


# the workflow “Merge pull request #1 from Leoultimo” runs on push to main branch,
 uses Ubuntu latest image. The first step is check out the code, the second – rubs the message.
The job runs correct


# the workflow “Refactor Python testing workflow to use a matrix strategy” uses a simple Python
code for tests from test_main.py
The workflow runs on Ubuntu latest image and tries the Python version: 3.7, 3.8, 3.9, 3.10
The test fails on version 3.7

# the workflow    “Scheduled Workflow” uses Ubuntu latest image
 Runs daily at midnight and put the log message. The test runs successfully 
