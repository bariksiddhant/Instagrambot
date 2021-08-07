from instapy import InstaPy
import config
#login
session = InstaPy(username=config.username , password = config.password)
session.login()
#like
session.like_by_tags(['bike','ducati'],amount=4)
#follow
session.set_do_follow(True,percentage=25)
#comment
session.set_do_comment(True,percentage=50)
session.set_comments(['Nice bike','Damn'])
session.end()