

class Queue:
    queue = []

    def __init__(self, data) -> None:
        self.data = data
        Queue.queue.append(self)
    
    @staticmethod
    def get_queue_list():
        return Queue.queue
