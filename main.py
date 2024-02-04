from git import Repo
import gui
from configparser import ConfigParser

config = ConfigParser()



# gui.run()

repo = Repo.init(path='./test')
git = repo.git
# git.add('.')
repo.index.commit('v3')
print(git.status())
# print(git.log())

# git.config('git-ftp.url','ftp://162.105.240.125:21/share/Git')
# git.config('git-ftp.user', 'chenqiwei')
# git.config('git-ftp.password', '03140507')
# git.ftp('init')
# git.ftp('push')