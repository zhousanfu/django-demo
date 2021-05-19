import configparser

configs = configparser.ConfigParser()
configs.read('config.ini', encoding='utf-8')
sections = configs.sections() # 获取所有section
database = dict(configs.items('database'))
print(database)
