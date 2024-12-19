# Author: Navjot Singh
# Created: March 22, 2024
# Modified: March 22, 2024
# Description:
# to allow a user to encode a piece of text
# using a cipher, or to decode the text using the same cipher. 


# Define English words and the corresponding emojis.
english_words = ["cat", "horse", "angry", "clap", "map", "alien", "cookiecow", "OK", "apple", "dog",
                 "sad", "banana", "egg", "elephant", "sheep", "bee", "fish", "sleep", "bird", "fox",
                 "tree", "car", "happy", "wave", "carrot", "heart", "zombie"]

emoji_equivalents = ["🐈", "🐎", "😠", "👏", "🗺", "👽", "🍪🐄", "👌", "🍎", "🐕", 
                     "😢", "🍌", "🥚", "🐘", "🐑", "🐝", "🐟", "🛌", "🐦", "🦊",
                     "🌲", "🚗", "😀", "👋", "🥕", "❤", "🧟"]

# Description of the encode function.
def encode(message):
    encoded_string = ""
# Split the input message into words
    words = message.lower().split()  
    for word in words:
        match_found = False
        word_index = 0
        while not match_found and word_index < len(english_words):
            if word == english_words[word_index]:
                # Add corresponding emoji.
                encoded_string += emoji_equivalents[word_index] 
                match_found = True
            word_index += 1
        if not match_found:
            # Do not change it, if the word cannot be found.
            encoded_string += word
        # Leave a gap between each word.
        encoded_string += " "
    # Return the encoded string.  
    return encoded_string

# Description of the decode function.
def decode(message):
    decoded_string = ""
# Split the input message into emojis.
    emojis = message.lower().split()  
    for emoji in emojis:
        match_found = False
        emoji_index = 0
        while not match_found and emoji_index < len(emoji_equivalents):
            if emoji == emoji_equivalents[emoji_index]:
                # Add corresponding english word.
                decoded_string += english_words[emoji_index]
                match_found = True
            emoji_index += 1
        if not match_found:
            # Do not change it, if the emoji cannot be found.
            decoded_string += emoji
        # Leave a gap between each emoji.
        decoded_string += " "
    # Return the decoded string.  
    return decoded_string

# Description of function to manage the code.
keep_running = True
while keep_running:
    # The First Asked Cue.
    print("To encode, enter '1'; to decode, enter '2'; to exit, enter '3'.")
    # Ask the user to input 
    choice = input()
    # Ask for the choice of the programmer.
    if choice == '1':
        # Doing Some Encoding
        text = input("Enter text to encode: ")
        # Encode the text and display the result
        encoded_text = encode(text)
        print("Encoded text:", encoded_text)
    elif choice == '2':
        # Doing Some Decoding
        text = input("Enter text to decode: ")
        # Decode the text and display the result
        decoded_text = decode(text)
        print("Decoded text:", decoded_text)
    elif choice == '3':
        # Exiting the Program
        print("Exiting program.")
        keep_running = False
    else:
        # Error or Invalid Message.
        print("Invalid data entered. Enter either '1,'' '2,'' or '3.'")