# User Guide

## Overview:
The original goal was to create a tool that can analyze a users tweets are help identify individuals that might be at risk for depressive episodes. This was to be done using our own classiyers and regressors. The actual scope of the project is a data exploration process in which datapiplines were created and initial regressors were trained. The datasets were created by scraping tweets and then uploading them to googles sentiment api to create a labeled dataset. Then different supervised learning and preprocessing techniques were explored and applied

## Prerequisites
There's not much point to run these yourself as they are just dataset creation scripts and training notebooks. analyze.py would be of the most interst if anything
#### Python:
.py and ipynb must be able to run on your machine
Create a conda enviornment using the requirements.txt to have all necessary packages isntalled. 
#### APIs:
The twitter api key is not uploaded to this repo for privacy reasons, so to run the data scraping scripts a twitter developer account will be needed. The keys from this account must be put in a file in the parent directory called "twitter_config.py" with varibles named "API_KEY", "SECRET_KEY", "ACCESS_TOKEN", and "ACCESS_SECRET". Fill the variables with your accounts information.

## Bugs
There are no current known bug, but setting up the env and apis can get tricky. Contact Eli for help or if additional information is needed.

## Results
Since there are few runnable pieces of the project, I've linked our presentation from demo day. This includes the accuracy for the regressors created since those are really our final product. 
https://docs.google.com/presentation/d/1U5ETlTiSMczqjM9n6iyOMxC9ptXAdtvXXXErgCfKIiw/edit?usp=sharing

