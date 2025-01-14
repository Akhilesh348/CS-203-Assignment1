class Metrics:
    def __init__(self):
        self.req_count = 0
        self.error_count = 0
        self.lock = Lock()

    def increment_requests_errors(self):
        with self.lock:
            self.req_count += 1
            self.error_count += 1
            return self.req_count , self.error_count