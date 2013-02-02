# FeedGin : Feeds in Pidgin
A Python script that

  * fetches feeds (RSS, Atom) from their specified URLs
  * shows the updates as messages in a conversation view in pidgin
  * keeps track of the time of the updates so that previously shown updates are not shown again

Can be used with any RSS / Atom feeds including:

  * Blog updates
  * Twitter posts
  * GitHub updates, etc.

# Requirements

  * Python (requires Python 2.7+)
  * [FeedParser][FP] 5.1 - A Python library for parsing various types of feeds

  [FP]: http://code.google.com/p/feedparser

# Installation

  * Copy the `feedgin.py` file to a local directory such as `~local/bin/`
  * Edit the file to setup feeds. Follow the examples in the top of the file.
  * Set up a cron job such as:

    `*/5  * * * * DISPLAY=:0 ./local/bin/feedgin.py`

    The above cron-job runs this script every 5 minutes. The `DISPLAY=:0` sets up the environment to allow DBUS communication in the cronjob.
