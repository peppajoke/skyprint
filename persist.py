import os
import pickle

class Persist:
    def __init__(self, filename):
        self.filename = filename

        # Check if the file exists, and create it if not
        if not os.path.exists(self.filename):
            with open(self.filename, 'wb') as f:
                pickle.dump(None, f)

    def get(self):
        with open(self.filename, 'rb') as f:
            return pickle.load(f)

    def set(self, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
