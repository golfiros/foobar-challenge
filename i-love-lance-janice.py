def solution(s):
    # ascii values for a and z
    a = 97
    z = 122
    # get list of ascii values
    characters = map(ord, s)
    for i, char in enumerate(characters):
        if char <= z and char >= a:
            # if it's a lowercase letter
            # we mirror
            characters[i] = z - (char - a)
    # convert back to a string
    return reduce(lambda x, y: x + y, map(chr, characters))

print solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?") == "did you see last night's episode?"
print solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!") == "Yeah! I can't believe Lance lost his job at the colony!!"
