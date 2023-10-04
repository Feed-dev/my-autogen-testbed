# filename: create_poem.py
poem = """
Raki, a dog, so brave and bold,
In winters warm, in summers cold.
He wags his tail, all day and night,
Seeing his joy, is a delightful sight.

He guards the house, with all his might,
No intruders can escape his sight,
In his presence, we never feel alone,
His happy place is near the throne.

With a wagging tail and a shiny coat,
Raki loves to playfully gloat,
A dog, a friend so precious and sagacious,
His love and loyalty are simply contagious.
"""

# Open the file with write mode.
with open("poem.txt", "w") as file:
    file.write(poem)
    
print("Poem written to poem.txt")