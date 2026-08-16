def shared_letters(note_a: str, note_b: str) -> str:
    my_note = ""
    for i in note_a:
        if i in note_b and i not in my_note:
            my_note += i 
    return my_note
