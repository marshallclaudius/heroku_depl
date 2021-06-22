from datetime import datetime

class App_Logger():
    def __init__(self):
        pass

    def logs(self, file_object, log_message):
        self.now = datetime.now()
        self.date = datetime.now.date()
        self.current_time = datetime.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(sefl.current_time) + "\t\t" + log_message + "\n"
        )

