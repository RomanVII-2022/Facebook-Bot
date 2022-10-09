from utilities.main import Facebook


with Facebook(teardown=False) as bot:
    bot.get_landing_page()
    bot.login_page('vicmkinyua77@gmail.com', 'Vicky1998')
    bot.menu()
    bot.create_post('You only live once', 'C:\pictures\phone.jpg')