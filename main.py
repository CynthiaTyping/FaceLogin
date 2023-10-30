# coding: UTF-8
# @Time    : 2023/10/30
# @Author  : Qi Ming
# @WeChat  : 19310619597
# @FileName: main.py
# @Software: Pycharm
from app import create_app, db
import sys
from flask_migrate import Migrate

sys.path.append('.')
app = create_app()
migrate = Migrate(app, db)
if __name__ == '__main__':
    migrate = Migrate(app, db)
    app.run(debug=True)
