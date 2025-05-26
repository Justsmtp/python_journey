# Mad Libs Story Generator

print("Let's play Mad Libs! Please provide the following words:")

# Prompt the user for inputs
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
adjective4 = input("Enter a final adjective: ")
animal = input("Enter a type of animal: ")
mood = input("How are you feeling today? (happy, excited, tired, grumpy): ").lower()

# Build the story with a conditional touch based on 'mood'
story = f"""
On a beautiful {adjective1} day, I went to the zoo. I saw a funny {adjective2} monkey swinging from the trees.
Then, I spotted a majestic {adjective3} {animal} lounging in the sun. What a wild and {adjective4} experience!
"""

# Conditional addition
if mood == "happy":
    story += "I was so happy to see all the animals playing together!"
elif mood == "excited":
    story += "I couldn't believe how excited I felt as I watched the animals!"
elif mood == "tired":
    story += "Even though I was tired, I still enjoyed my visit to the zoo."
elif mood == "grumpy":
    story += "Even though I felt grumpy, the animals made me smile."
else:
    story += "It was truly an unforgettable day!"

# Display the final story
print("\nHere’s your Mad Libs story:")
print(story)
