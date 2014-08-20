from django.db import models
from django.template import Template, Context
import requests

from django.conf import settings


class EMailTemplateManager(models.Manager):
    def send(self, id, to, data):
        return self.get_query_set().get(id=id).send(to, data)


class EMailTemplate(models.Model):
    id = models.CharField(max_length=128, unique=True, primary_key=True)
    title = models.CharField(max_length=256)
    sender = models.EmailField()
    subject = models.CharField(max_length=256)
    text = models.TextField()
    html = models.TextField()

    #WEB-5
    notifications = models.ManyToManyField("EMailTemplate", related_name="notificated_by", symmetrical=False, blank=True)

    objects = EMailTemplateManager()

    def __unicode__(self):
        return self.title


    def _render(self, data):
        context = Context(data)
        subject_template = Template(self.subject)
        text_template = Template(self.text)
        html_template = Template(self.html)
        subject = subject_template.render(context)
        text = text_template.render(context)
        html = html_template.render(context)
        return subject, text, html

    def send(self, to, data):
        subject, text, html = self._render(data)
        response = requests.post(
            settings.MAILGUN_API_URL,
            auth=("api", settings.MAILGUN_API_KEY),
            data={"from": self.sender,
                  "to": to,
                  "subject": subject,
                  "text": text,
                  "html": html})

        # TODO WEB-5 for many notification this will take quite a while
        # we should do it in the background

        for notification in self.notifications.all():
            for _, mail in settings.MANAGERS:
                notification.send(mail, data)
                # TODO WEB-5 check response and log errors

        return response

