from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Order 
from django.core.mail import send_mail

#order confirmation email
@receiver(post_save, sender=Order)
def send_Order_Confirmation_email(sender,instance,created,**kwargs):
  if created:
    subject = "congratulations! your order is submited"
    messege = (
      f"Hello ! {instance.user.username},\n\n"
      f"thank you for your order!\n"
      f"your order_id is {instance.id}"
    )
    from_email = "munnaahsan845@gmail.com"
    recipent_list = [instance.user.email]
    send_mail(
      subject,
      messege,
      from_email,
      recipent_list
    )