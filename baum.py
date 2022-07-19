import logging
logging.basicConfig(level=logging.DEBUG)

class Node (object):
    def __init__(self, val: str, children=None, data=None):
        self.val = val
        if children is None:
            self.children = []
        else:
            self.children = children
        self.data = data

    

    def search(self, val: str):
        logging.debug("search: '" + val + "' in Node " + self.val)
        if len(val) < len(self.val):
            logging.debug("Not found. Input is shorter than nodes value")
            return False
        
        len_val = len(self.val)
        for i in range(len_val):
            #logging.debug(f"comparing place {i} of {val} and {self.val}")
            if self.val[i] != val[i] and self.val[i] != "*" and val[i] != "*":
                logging.debug(f"couldnt match {val} and {self.val} in place {i}. Symbol difference: {val[i]} is not {self.val[i]}")
                return False
        logging.debug(f"partly match found: {self.val}")

        if len(self.children) == 0 or 0 == len(val[len_val:]):
            logging.info(f"match found: {self.val}. Data = {self.data}")
            return self.data

        for c in self.children:
            logging.debug(f"searching for {val} in {c.val}")
            data = c.search(val[len_val:])
            if data:
                logging.debug("ending search")
                break
     
        return data


    def insert(self, val: str, data):
        logging.debug("inserting: '" + val + "' into Node " + self.val)
        for i in range(min(len(val), len(self.val))):
            #logging.debug(f"comparing place {i} of {val} and {self.val}")
            if self.val[i] != val[i] and self.val[i] != "*" and val[i] != "*":
                logging.debug(f"couldnt match {val} and {self.val} in place {i}")
                self._nomatch(val, data, i)
                return;
        logging.debug("matched")
        i += 1
        logging.debug(val[i:])
        if not self._pass_to_child(val[i:], data):
            self.children.append(Node(val[i:], data=data))
        return

    def _pass_to_child(self, val, data):
        if val == "":
            return True
        logging.debug(f"trying to match {val} in:")
        logging.debug(list(map(lambda x: x.val, self.children)))
        for c in self.children:
            if c.val[0] == val[0]:
                c.insert(val, data)
                return True
        return False

    # easy muggle (einfach muggel)
    def _nomatch(self, val, data, i=0):
        logging.debug("nomatch inserting: '" + val + "' into Node " + self.val)
        v = val[i:]
        if not self._pass_to_child(v, data):
            logging.debug("new child: " + v)
            logging.debug("new child: " + self.val[i:])
            self._shed(i)
            self.children.append(Node(v, data=data))

    def _shed(self, i):
        data = self.data
        kids = self.children
        self.children = []
        self.data = None
        self.children.append(Node(self.val[i:], kids, data))
        self.val = self.val[:i]

    def show(self, indentation=0):
        print(_indent(f"{self.val}, {self.data} " + "{", indentation))
        for c in self.children:
            c.show(indentation + 1)
        print(_indent("}", indentation))

    
    def export(self) -> str:
        if len(self.children) == 0:
            return self.val;
        else:
            out = self.val[:] + "{"
            for c in self.children:
                out += c.export() + ","
            out = out[:-1] + "}"
            return out

    @classmethod
    def impord(self, text: str):
        name = ""
        for c in text:
            match c:
                case "{":
                    self.impord()
                case "}":
                    self.children.append(name)
                    return
                case ",":
                    self.children.append(name)
                    name = ""

        


def _indent(text, indentation):
    return "  "*indentation + text

class Baum(Node):
    def __init__(self, val="", children=None):
        self.val = val
        if children is None:
            self.children = []
        else:
            self.children = children
        self.data = None

    def insert(self, val, data):
        if not self._pass_to_child(val,data):
            self.children.append(Node(val, data=data))

