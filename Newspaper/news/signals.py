from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import mail_user
from .models import Post


# функция обработчик с параметрами под регистрацию сигнала
def new_post_notify(sender, instance, created, **kwargs):
    
 
    mail_user(
        subject=subject,
        message=instance.message,
    )

    if created:
        subject = f'{instance.title}'
    else:
        subject = f'Title has been changed{instance.title}'
 
    mail_user(
        subject=subject,
        message=instance.message,
    )
 
# коннектим наш сигнал к функции обработчику и указываем, к какой именно модели после сохранения привязать функцию
post_save.connect(new_post_notify, sender=Post)