import cryptography.fernet as fnt


class SecureFile:
    def __init__(self, path, code=None):
        if code is None:
            code = fnt.Fernet.generate_key()
        self.path = path
        self.code = code
        self.f = fnt.Fernet(code)
        return

    def load(self):
        F = open(self.path, 'rb')
        cipher = F.read()
        F.close()
        plaintext = self.f.decrypt(cipher)
        return str(plaintext)

    def save(self, plaintext=''):
        cipher = self.f.encrypt(bytes(plaintext))
        F = open(self.path, 'wb')
        F.write(cipher)
        F.close()
        return


def main():
    k = fnt.Fernet.generate_key()
    print(k)
    f = fnt.Fernet(k)
    return


if __name__ == "__main__":
    main()
