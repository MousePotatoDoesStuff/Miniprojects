class WFCTemplate:
    def apply_neighbor(self):
        raise NotImplementedError

class BaseWFC(WFCTemplate):
    def __init__(self, variants, connections, rules):
        self.variants = variants
        self.connections = connections
        self.rules = rules


def main():

    return


if __name__ == "__main__":
    main()
