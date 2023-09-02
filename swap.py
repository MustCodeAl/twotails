def tail_swap(strings):
    # Split each string on ':' to separate the head and tail
    str1_head, str1_tail = strings[0].split(':', 1)
    str2_head, str2_tail = strings[1].split(':', 1)

    # Return the new strings, swapping the tails
    return [f"{str1_head}:{str2_tail}", f"{str2_head}:{str1_tail}"]
