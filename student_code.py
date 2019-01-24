import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        if isinstance(fact, Fact):
            for x in self.facts:
                if x == fact:
                    continue

            self.facts.append(fact)


        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        print("Asking {!r}".format(fact))
        lb = ListOfBindings()
        for y in self.facts:
            is_match = match(y.statement, fact.statement)
            if is_match:
                lb.add_bindings(is_match)

        return lb

