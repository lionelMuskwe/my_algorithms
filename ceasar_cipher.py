class CeaserCipher:
    characters = ["a", "b", "c", "d", "e" ,"f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def encrypt(plainText, key):
        plainText = plainText.lower()
        plainText = plainText.replace(" ", "")
        return CeaserCipher.transform(plainText, key)

    def decrypt(cipherText, key):
        return CeaserCipher.transform(cipherText, (key * -1))

    def transform(text, key):
        transformed_text = ""
        for character in text:
            transformed_text += CeaserCipher.characters[(CeaserCipher.characters.index(character) + key) % 26]

        return transformed_text

