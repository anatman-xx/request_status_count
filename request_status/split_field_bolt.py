from pyleus.storm import SimpleBolt

class SplitFieldBolt(SimpleBolt):
    OUTPUT_FIELDS = ['ip', 'status']

    def process_tuple(self, tup):
        if (len(tup.values) == 0):
            return
            
        request = tup.values[0]

        values = request.split('\t')
        if (len(values) != 11):
            return

        self.emit((values[0], int(values[7])), anchors = [tup])

if __name__ == '__main__':
    SplitFieldBolt().run()
