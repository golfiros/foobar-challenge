def solution(plaintext):
    # main reference for this translator was wikipedia
    # https://en.wikipedia.org/wiki/Braille
    output = ""
    numeric_sequence_list = [("10","00"),
                        ("11","00"),
                        ("10","10"),
                        ("10","11"),
                        ("10","01"),
                        ("11","10"),
                        ("11","11"),
                        ("11","01"),
                        ("01","10"),
                        ("01","11")]
    decade_list = [("0","0"), ("1","0"), ("1","1")]
    characters = map(ord, plaintext)
    for char in characters:
        # handle spaces
        if char == 0x20:
            output += "000000"
            continue
        # handle uppercase
        if char < 0x60:
            output += "000001"
            char += 0x20
        offset = char - 0x61
        # w is different
        if offset == 22:
            output += "010111"
            continue
        if offset > 22:
            offset -= 1
        numeric = numeric_sequence_list[offset % 10]
        decade = decade_list[offset / 10]
        output += numeric[0] + decade[0] + numeric[1] + decade[1]
    return output

print solution("code") == "100100101010100110100010"
print solution("Braille") == "000001110000111010100000010100111000111000100010"
print solution("The quick brown fox jumps over the lazy dog") == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
