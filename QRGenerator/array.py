def final_color(colors):
    # Function to get the missing color
    def get_missing_color(color1, color2):
        if color1 == color2:
            return color1
        else:
            # The missing color is the one not in the pair (R, G, B)
            return 'RGB'.replace(color1, '').replace(color2, '')

    # Loop until we reduce the colors to a single color
    while len(colors) > 1:
        new_colors = []
        for i in range(len(colors) - 1):
            new_color = get_missing_color(colors[i], colors[i + 1])
            new_colors.append(new_color)
        colors = ''.join(new_colors)  # Update colors to the new row

    return colors  # The final single color

# Example usage:
print(final_color("RRGBRGBB"))  # Output should be 'G'





            


 






    
 









