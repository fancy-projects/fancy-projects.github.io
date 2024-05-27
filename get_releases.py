from urllib.request import urlopen
from json import loads

resp = loads(urlopen('https://api.github.com/repos/fancy-projects/fancy-cli/releases').read())


print(resp)