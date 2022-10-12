from utilities.main import Facebook


with Facebook(teardown=False) as bot:
    #bot.pagepost()
    #bot.post_like_and_comment()
    #bot.grouppost()
    bot.group_like_and_comment()