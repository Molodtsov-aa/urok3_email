import os
import smtplib

login = os.environ["Y_LOGIN"]
password = os.environ["Y_Password"]

shablon = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''
site = 'https://dvmn.org/referrals/EcXFbyvO8WgjdPowPmJbB8gEO8IR7egmOtkOb0Jd/'
friend = 'Имя'
name = 'Александр'

shablon = shablon.replace('%website%', site)
shablon = shablon.replace('%friend_name%', friend)
shablon = shablon.replace('%my_name%', name)

address = 'sannikova-school@yandex.ru'
recipient = 'molodcov.alexandr@yandex.ru'
heading = 'Важно'
type = 'text/plain; charset="UTF-8";' 

letter = '''
From: {address}
To: {recipient}
Subject: {heading}
Content-Type: {type}

''' + shablon.format(address=address, recipient=recipient,heading=heading,type=type)

letter = letter.encode("UTF-8")



server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)



server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(address, recipient, letter)
server.quit()