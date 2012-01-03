# Read feeds (Atom, RSS) in Pidgin
A Python script that

  * fetches feeds from their specified URLs
  * shows the updates as messages in a conversation view in pidgin
  * keeps track of the time of the updates so that previously shown updates are not shown again

Especially useful for monitoring GitHub updates, since GitHub doesn't have commit notifications by email.
(Though it does have other types of notifications).

# Requirements

  * Python (tested with Python 2.7)
  * [FeedParser][FP] - A Python library for parsing various types of feeds

  [FP]: http://www.feedparser.org

# Installation

  * Copy the feedgin.py file to a local directory such as `~local/bin/`
  * Set up a cron job such as:

    `*/5  * * * * DISPLAY=:0 ./local/bin/feedgin.py`

    The above cron-job runs this script every 5 minutes. The `DISPLAY=:0` setsup the environment to allow DBUS communication in the cronjob.