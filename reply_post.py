import praw
import pdb
import os
import re
#create the Reddit instance
reddit = praw.Reddit('grootbot')

#if this has never run before, create an empty list
if not os.path.isfile('posts_replied_to.txt'):
	posts_replied_to = []
#if it has run before, add to our current list	
else:
#read the file into a list and remove any empty values	
	with open('posts_replied_to.txt', 'r') as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split('\n')
		posts_replied_to = list(filter(None, posts_replied_to))
#get top 5 values from the subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):
#if bot has not replied to the post before
	if submission.id not in posts_replied_to:
#case insesitive search
		if re.search("i love python", submission.title, re.IGNORECASE):
#reply to the post
			submission.reply("Botty bot says: Me too!!!!")
			print("Bot replying to : ", submission.title)
#store current id in list
			posts_replied_to.append(submission.id)
#write the updated list to the file
with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")


