# Logs Analysis
Project 3/3 of udacity fsnd - Task is to create three queries on newsdata.sql on vagrant vm to answer three questions: 
- What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted    list with the most popular article at the top.
- Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which        authors get the most page views? Present this as a sorted list with the most popular author at the top.
- On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code    that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

## Getting Started
- Run vagrant up command to setup vagrant vm when inside FSND-Virtual Machine/Vagrant directory 
- To start vagrant vm enter vagrant up on bash or shell 
- Load the tables by using command psql -d news -f newsdata.sql
- Run python news.py to load logs on terminal 
- output.txt gives the sample output provided by the news.py script 


