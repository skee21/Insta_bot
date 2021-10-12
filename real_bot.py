from instapy import InstaPy 

session = InstaPy(username="#your_username", password="#your_password", headless_browser = True, multi_logs = True, browser_executable_path = (r'C:\Program Files\Mozilla Firefox\firefox.exe')).login()

session.login() 
#loginned and session started

session.set_relationship_bounds(enabled=True, max_followers=1000)
#would not interact with accounts more than 10000 followers

session.like_by_tags(["stories"], amount = 1) #change it
#likes the post with these hashtags

#session.set_dont_like([])
#does not likes these posts

session.set_do_follow(True)
#follows 80% of people whose post is liked

session.set_do_comment(enabled=True, percentage= 100) #will comment on posts it interacts	#change it

session.set_comments(["#your_comment"]) #it will comment this on the posts

session.set_quota_supervisor(enabled=True, peak_comments_daily=200, peak_comments_hourly=20) #not let's you get banned by insta!!
#daily comments limit 24o while hourly limiy 2o

session.end() 
#closes the browser
