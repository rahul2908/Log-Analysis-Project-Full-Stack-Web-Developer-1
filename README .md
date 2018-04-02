# Log Analysis

The Log Analysis project build an internal **reporting tool** that will use information from the database to discover what kind of articles the site's readers like.The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

# Steps to Perform

  - Download and install VM using `Virtual Box` from [here](https://www.virtualbox.org/wiki/Downloads).
  - Download and install `Vagrant` from [here](https://www.vagrantup.com/downloads.html).
  - To configure the VM, run the command `vagrant up` in the working folder.
  - Download the [news data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and save it on working VM folder.
  - Running `psql -d news -f newsdata.sql` command will connect to your installed database server and execute the SQL commands in the downloaded file.
  - Run `newsdb.py` on terminal to generate the database report.

# DataBase Info

  The database includes three tables:
  - `authors` -> This table includes information about the authors of articles.
    
    Column|Type|Modifiers
    ------|-----|-----
    name|text|not null
    bio|text|
    id|integer|not null default nextval ('authors_id_seq'::regclass)

  - `articles` -> This table includes the articles themselves.
  
    Column|Type|Modifiers
    ------|-----|-----
    author|integer|not null
    title|text|not null
    slug|text|not null
    lead|text|
    body|text|
    time|time stamp with time zone|default now()
    id|integer|not null default nextval ('articles_id_seq'::regclass)    

  - `log` -> This table includes one entry for each time a user has accessed the site.
  
    Column|Type|Modifiers
    ------|-----|-----
    path|text|
    ip|inet|
    method|text|
    status|text|
    time|time stamp with time zone|default now()
    id|integer|not null default nextval ('authors_id_seq'::regclass)


# Output

Popular Articles are:

	Candidate is jerk, alleges rival -- 338647 views
	Bears love berries, alleges bear -- 253801 views
	Bad things gone, say good people -- 170098 views

Popular Authors are:

	Ursula La Multa -- 507594 views
	Rudolf von Treppenwitz -- 423457 views
	Anonymous Contributor -- 170098 views
	Markoff Chaney -- 84557 views

Days with more than 1%  errors are:

	2016-07-17 -- 2.263%
	

# Code Quality
 - Code is ready for personal review and neatly formatted.
 - It follows the Python [PEP-8 Guidelines][df1]
 
# Comments
 - Comments effectively explain longer code procedures.
