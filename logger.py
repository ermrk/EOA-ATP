import os


class logger:
    evaluations = 0
    best_so_far=0

    def __init__(self, folder, name):
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.file_name = folder + name
        self.max_evaluations = 100000
        logger.evaluations = 0
        logger.best_so_far=0

    def write(self, value):
        if self.evaluations < self.max_evaluations:
            file = open(self.file_name, "a")
            if value>logger.best_so_far:
                logger.best_so_far=value
            file.write(str(logger.best_so_far) + "\n")
            file.close()
            logger.evaluations += 1

    def break_it(self):
        if logger.evaluations < self.max_evaluations:
            return False
        else:
            return True
