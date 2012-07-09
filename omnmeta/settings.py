import os


def project_dir(*path):
    base = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(base, *path)

DB_FILENAME = 'database.sqlite'
DB = 'sqlite:///%s' % project_dir(DB_FILENAME)
