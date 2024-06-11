class FiniteStateAutomaton:
    def __init__(self):
        self.states = {0: "start", 1: "a_seen", 2: "ab_seen"}
        self.accept_state = 2
        self.current_state = 0

    def transition(self, char):
        if self.current_state == 0:  # Start state
            if char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0
        elif self.current_state == 1:  # 'a' seen
            if char == 'b':
                self.current_state = 2
            elif char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0
        elif self.current_state == 2:  # 'ab' seen
            if char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0

    def is_accepting(self):
        return self.current_state == self.accept_state

    def reset(self):
        self.current_state = 0

    def run(self, input_string):
        self.reset()
        for char in input_string:
            self.transition(char)
        return self.is_accepting()

# Test the Finite State Automaton
fsa = FiniteStateAutomaton()

# Test strings
test_strings = [
    "ab",
    "aab",
    "babab",
    "abab",
    "aaaaab",
    "bba",
    "abc",
    ""
]

for test_string in test_strings:
    result = fsa.run(test_string)
    print(f"Input: {test_string} -> Accepting: {result}")
