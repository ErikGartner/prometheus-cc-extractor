from collections import Counter
import re
###
from mrcc import CCJob
import mrjob


class ObamaBornExtractor(CCJob):

    OUTPUT_PROTOCOL = mrjob.protocol.JSONValueProtocol

    relation = '|'.join(['(?:born in)', '(?:grew up)'])
    name = 'Obama'
    filter_reg = re.compile('({}[^.?]+(?:{})[^.?]*)'.format(name, relation),
                            re.IGNORECASE)

    def process_record(self, record):

        if record['Content-Type'] != 'text/plain':
            return

        data = record.payload.read()
        match = re.findall(ObamaBornExtractor.filter_reg, data)
        if len(match) == 0:
            # Document didn't contain the sought after string
            return

        self.increment_counter('commoncrawl', 'matching_documents', 1)
        yield record.url, {'url': record.url, 'sentences': match, 'document': data}

if __name__ == '__main__':
    ObamaBornExtractor.run()
