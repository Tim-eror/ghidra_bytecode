class Node (object):
    def __init__(self, val: str, children=None):
        self.val = val
        if children is None:
            self.children = []
        else:
            self.children = children

    def insert(self, val: str):
        print("inserting: '" + val + "' into Node " + self.val)
        for i in range(min(len(val), len(self.val))):
            print(f"comparing place {i} of {val} and {self.val}")
            if self.val[i] != val[i] and val[i] != "*":
                print(f"couldnt match {val} and {self.val} in place {i}")
                self._nomatch(val, i)
                return;
        print("matched")
        i += 1
        print(val[i:])
        if not self._pass_to_child(val[i:]):
            self.children.append(Node(val[i:]))
        return;

    def _pass_to_child(self, val):
        if val == "":
            return True
        print(f"trying to match {val} in:")
        print(list(map(lambda x: x.val, self.children)))
        for c in self.children:
            if c.val[0] == val[0]:
                c.insert(val)
                return True;
        return False;

    # easy muggle (einfach muggel)
    def _nomatch(self, val, i=0):
        print("nomatch inserting: '" + val + "' into Node " + self.val)
        if not self._pass_to_child(val[i:]):
            print("new child: " + val[i:])
            print("new child: " + self.val[i:])
            self._shed(i)
            self.children.append(Node(val[i:]))

    def _shed(self, i):
        kids = self.children
        self.children = []
        self.children.append(Node(self.val[i:], kids))
        self.val = self.val[:i]

    def show(self, indentation=0):
        print(_indent(self.val + "{", indentation))
        for c in self.children:
            c.show(indentation + 1)
        print(_indent("}", indentation))

    
    def export(self) -> str:
        if len(children) == 0:
            return val;
        else:
            out = val[:] + "{"
            for c in self.children:
                out += c.export() + ","
            out = out[:-1] + "}"
            return out;

    @classmethod
    def impord(cls, text: str):
        pass


def _indent(text, indentation):
    return "  "*indentation + text

class Baum(Node):
    def __init__(self, val="", children=None):
        self.val = val
        if children is None:
            self.children = []
        else:
            self.children = children

    def insert(self, val):
        if not self._pass_to_child(val):
            self.children.append(Node(val))

