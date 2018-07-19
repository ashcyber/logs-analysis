#!/usr/bin/env python
import psycopg2

# globals
DB_NAME = "news"

# What are the most popular three articles of all time?
query1 = """
SELECT articles.title, count(*) AS views
FROM articles INNER JOIN log
ON log.path = concat('/article/', articles.slug)
WHERE log.status = '200 OK'
GROUP BY articles.title, log.path
ORDER BY views DESC
LIMIT 3
"""

# Who are the most popular article authors of all time?
query2 = """
SELECT authors.name, count(*) AS views
FROM articles
INNER JOIN authors ON articles.author = authors.id
INNER JOIN log ON log.path = concat('/article/', articles.slug)
WHERE log.status = '200 OK'
GROUP BY authors.name
ORDER BY views DESC
"""

# On which days did more than 1% of requests lead to errors?
query3 = """
SELECT total_view.days,
ROUND(((errors_view.error_req*100.0) / total_view.reqs), 1) AS percent
FROM ( SELECT date_trunc('days', time) "days", count(*) AS error_req
 FROM log WHERE status !='200 OK' GROUP BY days) AS errors_view
INNER JOIN ( SELECT date_trunc('days', time) "days", count(*) AS reqs
 FROM log GROUP BY days ) AS total_view
ON errors_view.days = total_view.days
WHERE ROUND(((errors_view.error_req*100.0) / total_view.reqs), 1) > 1.0
ORDER BY percent DESC;
"""


def run_query(query, dbname=DB_NAME):
    try:
        db = psycopg2.connect(database=dbname)
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
        db.close()
        return rows
    except:
        print("Error running the query on " + dbname + " database")


def format_error_results(rows):
    for i in rows:
        print(i[0].strftime('%B %d, %Y') + ' -- ' + str(i[1]) + "% errors")


def format_query_results(rows):
    for i in rows:
        print("\"" + i[0] + " \" -- " + str(i[1]) + " views")

print("What are the most popular three articles of all time?")
format_query_results(run_query(query1))

print("\nWho are the most popular articles authos of all time?")
format_query_results(run_query(query2))

print("\nOn which days did more than 1% of requests lead to errors?")
format_error_results(run_query(query3))
