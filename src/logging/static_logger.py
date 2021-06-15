import logging

class StaticLogger(object):


    def __init__(self):
        self.logger = StaticLogger.create_logger()

    @classmethod
    def create_logger(cls):
        #logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #formatter = logging.Formatter("[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


        #%(filename)s
        logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(processName)s %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s")
        return logging.getLogger(cls.__name__)

    def log_me(self):
        me = "world"
        StaticLogger.create_logger().info("Hello :{0}".format(me))
        StaticLogger.create_logger().info(f"Hello :{me}")
        StaticLogger.create_logger().info(F"Hello :{me}")
        print(id(StaticLogger.create_logger()))
        print(id(StaticLogger.create_logger()))
        print(id(StaticLogger.create_logger()))
        print(id(StaticLogger.create_logger()))

    def raise_exception_1(self):
        raise Exception("Something went wrong in raise_exception_111")

    def raise_exception_2(self):
        try:
            self.raise_exception_1()
        except BaseException as be:
            raise Exception("Something went wrong in raise_exception_222")

    def throw_exception(self):
        try:
            self.raise_exception_2()

        except BaseException as be:
            own = "hello"
            StaticLogger.create_logger().error(be, exc_info=True)

if __name__ == "__main__":
    my_logger = StaticLogger()
    my_logger.throw_exception()
    #my_logger.log_me()