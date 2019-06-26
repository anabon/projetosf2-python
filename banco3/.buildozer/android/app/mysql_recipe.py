
from pythonforandroid.toolchain import PythonRecipe

class mysqlRecipe(PythonRecipe):
    version = 'master'
    url = 'https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-8.0.11.tar.gz'

    depends = ['python2', 'protobuf']

    site_packages_name = 'mysql'

recipe = mysqlRecipe()



