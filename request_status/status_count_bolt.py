import collections

import redis

from pyleus.storm import SimpleBolt

class StatusCountBolt(SimpleBolt):
    def initialize(self):
        self.storage = redis.Redis()
        self.status_count = collections.defaultdict(int)

    def process_tick(self):
        for i in self.status_count:
            self.storage.incr(i, self.status_count[i])

        self.status_count.clear()

    def process_tuple(self, tup):
        if (len(tup.values) == 0):
            return
            
        ip, status = tup.values
        self.status_count[status] += 1

if __name__ == '__main__':
    StatusCountBolt().run()
