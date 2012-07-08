import os

def project_dir(*path):
    base = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(base, *path)

DB = 'sqlite:///%s' % project_dir('database.sqlite')
