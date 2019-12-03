def edit_distance(s1, s2):
    # If both strings are empty.
        if s1 == "" and s2 == "":
            return 0
    # If first string is empty.
        if s1 == "":
            return len(s2)
    # If second string is empty.
        if s2 == "":
            return len(s1)
    # If both strings are equal at first index.
        if s1[0] == s2[0]:
            return edit_distance(s1[1:], s2[1:])
    # Uses remove, add, and replace and adds 1 for number of changes.
        return 1 + min(edit_distance(s1, s2[1:]), edit_distance(s1[1:], s2), edit_distance(s1[1:], s2[1:]))


def main():
    s1 = "apple"
    s2 = "pineapple"
    print(edit_distance(s1, s2))


main()

