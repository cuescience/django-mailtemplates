from django.db import models
from django.template import Template, Context
import requests

from django.conf import settings

class EMailTemplate(models.Model):
    id = models.CharField(max_length=128, unique=True, primary_key=True)
    title = models.CharField(max_length=256)
    sender = models.EmailField()
    subject = models.CharField(max_length=256)
    text = models.TextField()
    html = models.TextField()

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
        return requests.post(
        settings.MAILGUN_API_URL,
        auth=("api", settings.MAILGUN_API_KEY),
        data={"from": self.sender,
              "to": to,
              "subject": subject,
              "text": text,
              "html": html})

