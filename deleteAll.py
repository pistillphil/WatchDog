'''
WatchDog for Reddit
Copyright (C) 2013  pistillphil

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import praw
from data import *

answer = raw_input('Are you sure you want to delete every submission in r/' + SUBREDDIT + '?\n(type "yes"): ')

if answer == 'yes':
	r = praw.Reddit(USERAGENT)
	r.login(USERNAME, PASSWORD)
	
	submissions = r.get_subreddit(SUBREDDIT).get_new(limit=10000)
	for submission in submissions:
		print 'DELETING:' + submission.title[0:50]
		submission.delete()
		
else:
	print 'Operation aborted...'
	exit(0)