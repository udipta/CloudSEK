from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from results.models import Results


@receiver(post_save, sender=Results)
def populate_answer(sender, instance, created, **kwargs):
    from calculator.tasks import populate_answers_task
    if created:
        print('*'*100)
        transaction.on_commit(lambda: populate_answers_task.apply_async(args=[instance.id], countdown=10))
