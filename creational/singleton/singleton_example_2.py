class SingletonObjects:
    class __SingletonObjects:
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

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = cls.__SingletonObjects()
        return cls.instance

    def __getattr__(self, name):
       return getattr(self.instance, name)
   
    def __setattr__(self, name: str):
        return setattr(self.instance, name)
  

obj1 = SingletonObjects()
obj1.file_name = 'log1.txt'
obj1.critical(" ** critical ** ")
print("print obj1: ", obj1)


obj2 = SingletonObjects()
obj1.file_name = 'log2.txt'
obj2.warning("** warning **")
print(obj2)
