#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def get_news(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result

# The get_articles method lists the top three articles that has been \
    # accessed the most.


def get_articles():
    article_query = """select title, count(*) as num from articles, \
    log where articles.slug  = substring(log.path,10) group by title \
    order by num desc limit 3;"""
    article = get_news(article_query)
    print('\nPopular Articles are:\n')
    for result in article:
        print('\t' + str(result[0]) + ' -- ' + str(result[1]) + ' views')

# The get_authors method lists the sum up of all the articles written \
        # by each author.


def get_authors():
    author_query = """select authors.name, count(*) as num from articles,\
    authors, log where log.status = '200 OK' and authors.id = articles.author\
    and articles.slug = substring(log.path, 10) group by authors.name order\
    by num desc;"""
    auth = get_news(author_query)
    print('\nPopular Authors are:\n')
    for result in auth:
        print('\t' + str(result[0]) + ' -- ' + str(result[1]) + ' views')

# The get_error_per method list the days on which more than 1% of requests\
        # lead to errors.


def get_error_per():
    error_query = """select * from(select date(time), \
    round(100.0*sum(case log.status when '200 OK' then 0\
    else 1 end)/count(log.status),3) as error from log group\
    by date(time) order by error desc) as subq where error > 1;"""
    err = get_news(error_query)
    print('\nDays with more than 1%  errors are:\n')
    for result in err:
        print('\t' + str(result[0]) + ' -- ' + str(result[1]) + '%')


if __name__ == '__main__':
    get_articles()
    get_authors()
    get_error_per()
