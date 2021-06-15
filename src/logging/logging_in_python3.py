import logging
from datetime import datetime

class MyLogger:

    def __init__(self):
        pass
        #logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #self.logger = logging.getLogger(self.__class__.__name__)

    def log_me(self):
        logging.basicConfig(level=logging.INFO)
        #me = "world"
        #self.logger.info("Hello :{0}".format(me))
        #self.logger.info(f"Hello :{me}")
        #self.logger.info(F"Hello :{me}")
        logging.info("logger: Started run at %s %d " % (datetime.now(), 4))
        print("Started run at %s" % datetime.now())

if __name__ == "__main__":
    #print(f"{MyLogger.__name__}")
    my_logger = MyLogger()
    my_logger.log_me()