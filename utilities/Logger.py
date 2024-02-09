import inspect
import logging


class LoggenClass:
    @staticmethod
    def log_generator():
        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)
        logfile = logging.FileHandler("C:\\Users\\hp\\PycharmProjects\\FramePractnight\\Logs\\Nopcom_Logs.logs")
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s %(lineno)s : %(message)s ")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger