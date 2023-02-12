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


    def testCeasarCipher():
        # Testing encryption without rollover
        encryptedText1 = CeaserCipher.encrypt("abc", 1)
        decryptedText1 = CeaserCipher.decrypt(encryptedText1, 1)
        assert encryptedText1 == "bcd", "Single key increment encryption is NOT working"
        assert decryptedText1 == "abc", "Single key decrement decryption is NOT working"

        # Testing encryption with rollover
        encryptedText2 = CeaserCipher.encrypt("asyvx", 15)
        decryptedText2 = CeaserCipher.decrypt(encryptedText2, 15)
        assert encryptedText2 == "phnkm", "Modulus increment encryption is NOT working"
        assert decryptedText2 == "asyvx", "Modulus key decrement decryption is NOT working"

CeaserCipher