import pandas as pd
import json
class Strategy(object):
    def execute(self, path):
        raise NotImplementedError('execute')


class reader(object):
    def __init__(self, strategy: Strategy):
        self.strategy = strategy


class read_comma(Strategy):
    def execute(self, path):
        return pd.read_csv(path, ',')


class read_xml(Strategy):
    def execute(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            text = json.load(f)

        return text


if __name__ == "__main__":
    reader_csv = reader(read_comma())
    reader_xml = reader(read_xml())
    print(reader_csv.strategy.execute('comma.csv'))
    print(reader_xml.strategy.execute('json_exmpl.json'))

