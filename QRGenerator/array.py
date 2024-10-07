def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []

    # Build lines with words fitting within the specified width
    for word in words:
        if sum(len(w) for w in current_line) + len(current_line) + len(word) <= width:
            current_line.append(word)
        else:
            lines.append(current_line)
            current_line = [word]

    # Add the last line
    if current_line:
        lines.append(current_line)

    justified_lines = []

    # Justify all lines except the last one
    for line in lines[:-1]:
        if len(line) == 1:  # Single word in a line
            justified_lines.append(line[0])
            continue

        total_chars = sum(len(word) for word in line)
        total_spaces = width - total_chars
        space_between_words = len(line) - 1
        even_space = total_spaces // space_between_words
        extra_space = total_spaces % space_between_words

        # Create the justified line
        justified_line = ''
        for i, word in enumerate(line):
            justified_line += word
            if i < space_between_words:  # Add spaces if not the last word
                justified_line += ' ' * (even_space + (1 if i < extra_space else 0))

        justified_lines.append(justified_line)

    # Handle the last line
    last_line = ' '.join(lines[-1])
    justified_lines.append(last_line)

    return '\n'.join(justified_lines)

# Example usage
text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor "
        "mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce "
        "at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum "
        "urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet "
        "lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse "
        "rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit "
        "fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. "
        "Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, "
        "ante odio porta lacus, ut elementum justo nulla et dolor.")

justified_text = justify_text(text, 30)
print(justified_text)





            


 






    
 









