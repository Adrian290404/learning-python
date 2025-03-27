def find_super_man(s):
    lower_s = s.lower()
    if "superman" in lower_s:
        return "Are you crazy?"
    
    def hidden_sequence_exists(text, pattern):
        index = -2
        for char in pattern:
            index = text.find(char, index + 2)
            if index == -1:
                return False
        return True

    pattern = "superman"
    reversed_pattern = pattern[::-1]

    if hidden_sequence_exists(lower_s, pattern) or hidden_sequence_exists(lower_s, reversed_pattern):
        return "Hi, SuperMan!"
    else:
        return "Are you crazy?"