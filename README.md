# Read feeds (Atom, RSS) in Pidgin
This is a simple Python script that
  * fetches specified feeds
  * shows them in a conversation view in pidgin

Especially useful for monitoring GitHub updates, since GitHub doesn't have commit notifications by email.
(Though it does have other types of notifications).

The script is very basic right now, but will be evolved soon.

# Requirements

  * Python (tested with Python 2.7)
  * [FeedParser][FP]

  [FP]: http://www.feedparser.org

# Installation

  * Copy the feedgin.py file to a local directory such as "local/bin/"
  * Set up a cron job such as:

        */5  * * * * ./local/bin/feedgin.py

