class A:
    def feaure1(self):
        print('this is feature1')

    def feature2(self):
        print('this is feature2 from a')


class B:

    def feature2(self):
        print('this is feature3')

    def feature4(self):
        print('this is feature4')


class C(A, B):
    def feature5(self):
        super().feature2()
        print('this is feature5')


c = C()

c.feature5()
