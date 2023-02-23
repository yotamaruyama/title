import abc

class key_parent(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def up_input(self):
        # メソッドの内容は記述できない(pass固定)
        pass
    @abc.abstractmethod
    def down_input(self):
        pass
