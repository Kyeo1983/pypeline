# Config classes should be camel cased
class email(luigi.Config):
    sender = luigi.Parameter(default="luigi-noreply@pypeline.com")
    sendername = luigi.Parameter(default="Mario")
    password = luigi.Parameter()
    username = luigi.Parameter()
    host = luigi.Parameter()
    port = luigi.Parameter()

class {{job}}_{{id}}(luigi.Task):
    def required(self):
        return {{job}}_{{parent}}()

    def run(self):
        """ Sends an email with message
        """
        emailconf = email()
        subprocess.call('echo "{}" | s-nail -s "{}" -r "{}<{}>" -S smtp="{}:{}" -S smtp-use-starttls -S smtp-auth-login -S smtp-auth-user="{}" -S smtp-auth-password="{}" -S ssl-verify=ignore {}'
        .format('{{param_in_body}}', '{{param_in_title}}', emailconf.sendername, emailconf.sender, emailconf.host, emailconf.port, emailconf.username, emailconf.password, emailconf.receiver, '{{param_in_recipient}}'), shell=True)

        with open(self.output().path, 'w') as out:
            out.write('sent')


    def output(self):
        return luigi.LocalTarget(str(ctx['sysFolder']) + '/run/{{id}}.mrk')
