def find_word(grid, word):
    # Iterate through each element in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Check the element and its neighbors (up, down, left, right, diagonals)
            if grid[row][col] == word[0]:
                # Check horizontal match
                if col <= len(grid[0]) - len(word) and "".join([grid[row][x] for x in range(col,col+len(word))]) == word:
                    return (row, col)
                # Check vertical match
                elif row <= len(grid) - len(word) and "".join([grid[x][col] for x in range(row,row+len(word))]) == word:
                    return (row, col)
                # Check diagonal match
                elif row <= len(grid) - len(word) and col <= len(grid[0]) - len(word) and "".join([grid[row+x][col+x] for x in range(0,len(word))]) == word:
                    return (row, col)
                # Check other diagonal match
                elif row <= len(grid) - len(word) and col >= len(word) - 1 and "".join([grid[row+x][col-x] for x in range(0,len(word))]) == word:
                    return (row, col)
    return None

grid = [['D','G','O','O','D','D','O','D','G','O','O','D','D','O'],
        ['O','D','O','O','G','G','G','D','O','D','G','O','G','G'],
        ['O','G','O','G','D','O','O','D','G','O','O','D','D','D'],
        ['D','G','D','O','O','O','G','G','O','O','G','D','G','O'],
        ['O','G','D','G','O','G','D','G','O','G','G','O','G','D'],
        ['D','D','D','G','D','D','O','D','O','O','G','D','O','O'],
        ['O','D','G','O','G','G','D','O','O','G','G','O','O','D']]
word = "dog"

print(find_word(grid, word))
