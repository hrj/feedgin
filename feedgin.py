#!/usr/bin/env python

################
# Configuration
feeds = {
  "hrj's activity" : {
    "url":"https://github.com/hrj.atom"
  },
  "Google News" : {
    "url" : "http://news.google.co.in/news?pz=1&cf=all&ned=in&hl=en&output=rss"
  }
}

dataFilePath = '~/.appdata/feedgin.data'
################

import dbus
import feedparser
import calendar
import csv
import os.path

feedProcessedTimes = {name:0 for name in feeds}
dataFilePathExpanded = os.path.expanduser(dataFilePath)

if os.path.exists(dataFilePathExpanded):
  dataFile = open(dataFilePathExpanded, 'rb+')
  dataReader = csv.reader(dataFile)
  for row in dataReader:
    feedProcessedTimes[row[0]] = row[1]

bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

activeAccounts = purple.PurpleAccountsGetAllActive()

if (len(activeAccounts) > 0) :
  account = activeAccounts[0]
  conversation = purple.PurpleConversationNew(1, account, "feedgin")
  for feedName in feeds:
    print "Fetching", feedName
    url = feeds[feedName]["url"]
    ast = feedparser.parse(url)
    #purple.PurpleConversationWrite(conversation, feedName, ast.feed.title, 0, 0)
    #print "feed:", ast.feed
    #print "entries:"
    for x in sorted(ast.entries, key = lambda entry: entry.updated_parsed):
      # for e in x: print e,':', x[e]
      time_since_epoch =  calendar.timegm(x.updated_parsed)
      if time_since_epoch > feedProcessedTimes[feedName]:
        feedProcessedTimes[feedName] = time_since_epoch
        if x.has_key("author_detail"):
          author = x.author_detail
        else:
          class DummyAuthor:
            href='#'
            name='-'
          author = DummyAuthor()
        # Pidgin apparently doesn't show <img/> correctly
        #text = "<img id='42' src='"+x.media_thumbnail[0]["url"]+"' />"
        text = "<br/><b><a href='"+ x.link + "'>"+x.title+"</a></b> <em>by</em> <b><a href='"+author.href+"'>"+author.name+"</a></b>"
        text += "<br/><small>" + x.summary + '</small>'
        purple.PurpleConversationWrite(conversation, feedName, text, 0, time_since_epoch)


dataFile = open(dataFilePathExpanded, 'wb+')
dataWriter = csv.writer(dataFile)
for feedName in feedProcessedTimes:
  dataWriter.writerow([feedName, feedProcessedTimes[feedName]])
