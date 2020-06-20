from pynotificator import SlackNotification
text = "会議中です"
sn = SlackNotification(text, 'https://hooks.slack.com/services/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')
sn.notify()