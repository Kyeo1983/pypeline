class {{job}}_{{id}}(luigi.Task):    
    def requires(self):
        return {{job}}_{{parent}}()
    
    def run(self):
        myvar = "Within Sample run"
        ctx['{{param_out_var}}'] = myvar
        print('>>>> {} <<<<'.format(myvar))
        
        with open(self.output().path, 'w') as out:
            out.write('ran')

    def output(self):
        return luigi.LocalTarget(str(ctx['sysFolder']) + '/run/{{id}}.mrk')
