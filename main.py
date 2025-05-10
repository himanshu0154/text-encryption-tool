import random
import string
import sys 

# List to track all encrypted sentences
encrypted_sentences = []

def encrypt_sentence(words):
    """
    Encrypts a list of words using a custom scheme:
    - Words with less than 3 characters are reversed.
    - Longer words are shifted (first char to end) and wrapped with random prefixes/suffixes
    """
    encrypted_words = []    
    for word in words:
        if len(word) < 3:
            reversed_word = word[::-1]
            encrypted_words.append(reversed_word)
        else:
            # Move the first letter to the end
            rotated_word = word[1:] + word[0]

            # Generate 3 random lowercase letters for prefix and suffix
            prefix = "".join(random.choices(string.ascii_lowercase, k=3))
            suffix = "".join(random.choices(string.ascii_lowercase, k=3))

            # Wrap the rotated word with prefix and suffix
            obfuscated_word = prefix +  rotated_word + suffix
            encrypted_words.append(obfuscated_word)
    encrypted_sentence = " ".join(encrypted_words)
    encrypted_sentences.append(encrypted_sentence)
    print(encrypted_sentence)
        
def decrypt_sentence(index):
        """
        Decrypts the sentence at the given index from the encrypted_sentence list.
        """
        sentence = encrypted_sentences[index]
        decrypted_words = []

        for word in sentence.split(" "):
            if len(word) < 3:
                reversed_word = word[::-1]
                decrypted_words.append(reversed_word)
            else:
                # Remove the 3 letter suffix and prefix
                core_word = word[3:-3]
                # Move the last character to the front
                original_word = core_word[-1] + core_word[:-1] 

                decrypted_words.append(original_word)
        print(" ".join(decrypted_words))
        # Remove the decrypted sentence from the list
        del encrypted_sentences[index]

def main():
    while True:
        action = input("what would you wanna do (encrypted(e)/decrypted(d)/stop/clear): ")
        if action == "e":   
            sentence = input("enter the word: ").split(" ")
            encrypt_sentence(sentence)

        elif action == "d":
            if encrypted_sentences == []:
                print("there isn't anything here")
            else:  
                print(f"please choose from these words :")
                for i, sentence in enumerate(encrypted_sentences):
                    print(f"{i+1}. {sentence}")
                try:
                    index = int(input("enter your the number respect to the sentence you want to choose: "))
                    decrypt_sentence(index-1)
                except IndexError:
                    print("not available")
                except ValueError:
                    print("please enter valid input!!")
                    
        elif action == "stop":
            sys.exit()

        elif action == "clear":
            encrypted_sentences.clear()
            print("the list is cleared")

        else:
            print("please give valid response")
            
if __name__=="__main__":
    main()