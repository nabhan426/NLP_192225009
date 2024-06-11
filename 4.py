# Define a simple finite-state machine for pluralization
def pluralize(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    else:
        return word + 's'

# Test the finite-state machine
print(pluralize('cat'))  # Output: cats
print(pluralize('box'))  # Output: boxes
