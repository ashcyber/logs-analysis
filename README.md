# Logs Analysis
Project 3/3 of udacity fsnd - Task is to create three queries on newsdata.sql on vagrant vm to answer three questions: 
- What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted    list with the most popular article at the top.
- Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which        authors get the most page views? Present this as a sorted list with the most popular author at the top.
- On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code    that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

## Setup
1. Install Vagrant and Virtualbox 
2. Download [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
2. Download this repository in your local machine 
3. Download [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from this link. 
4. Extract newsdata and this repository code inside fullstack-nanodegree vm/../vagrant folder
6. Cd inside vagrant folder in fullstack-nanodegree-vm repo and enter command vagrant up to setup vm 
7. To launch vagrant vm enter vagrant ssh 

## Getting Started
- Load the tables by using command psql -d news -f newsdata.sql
- newsdata.sql consist of three tables which are authors, articles and logs 
- Check if tables are correctly loaded by testing basic SQL queries after running psql -d news 
- Run python news.py to load logs on terminal 
- output.txt gives the sample output provided by the news.py script 

## news.py 
1. function run_query: runs given query on the db (default is news)
2. function format_error_results : formats error result code to display percent errors  
3. function format_query_results : formats first two queries to display views 
