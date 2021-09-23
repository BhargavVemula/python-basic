class Pycharm:
    def execute(self):
        print('this is best editor for executing ')
        print('best debugger')
        print('best spell checker')


class Mycharm:
    def execute(self):
        print('this is bhargavs own editor')


class Laptop:
    def code(self, ide):
        ide.execute()


ide = Mycharm()
ide = Pycharm()
lap1 = Laptop()
lap1.code(ide)
lap2 = Laptop()
lap2.code(ide)
