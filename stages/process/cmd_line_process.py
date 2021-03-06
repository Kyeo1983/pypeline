from subprocess import Popen

class {{job}}_{{id}}(luigi.Task):    
    def requires(self):
        return {{job}}_{{parent}}()
    
    def run(self):
        devnull = subprocess.DEVNULL
        proc = Popen(['./{{param_jobname}}'], stdout=devnull, stderr=devnull)
        with open(self.output().path, 'w') as out:
            out.write(str('running'))

    def output(self):
        return luigi.LocalTarget(str(ctx['sysFolder']) + '/run/{{id}}.mrk')