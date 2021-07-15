class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]



class SingletonObjects(metaclass=MetaSingleton):

    def __init__(self):
        self.file_name = None

    def __str__(self):
        return "{0!r} {1}".format(self, self.file_name)

    def _write_log(self, level, msg):
        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def error(self, msg):
        self._write_log("ERROR", msg)

    def warning(self, msg):
        self._write_log("WARNING", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)


obj1 = SingletonObjects()
obj1.file_name = 'log1.txt'
obj1.critical(" ** critical ** ")
print("print obj1: ", obj1)


obj2 = SingletonObjects()
obj1.file_name = 'log2.txt'
obj2.warning("** warning **")
print(obj2)
