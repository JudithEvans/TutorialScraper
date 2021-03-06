# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# next line imports a function from scraperwiki. it's not related to the lxml.html library
import scraperwiki
# next line imports the lxml.html library
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
# print html
#
# # Find something on the page using css selectors
# use the .fromstring function to turn html into a lxml 'object', a variable called 'root'
root = lxml.html.fromstring(html)
# use .cssselect method on root to grab 'td' tags and put in tds
tds = root.cssselect('td')
# print tds

# for td in tds:
  # print lxml.html.tostring(td)
  # print td.text

# creating a second column. in addition to the tds -- that will contain a unique index number
indexno = 0
for td in tds: 
  # so each time it runs, the index number increases by 1
  indexno = indexno + 1
  record = {"td" : td.text, "index": indexno}
  # print record
  scraperwiki.sqlite.save(["index"],record)
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
