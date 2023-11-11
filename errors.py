class Error(Exception):
    pass


class LengthError(Error):
    pass


class PasswordsIsNotCorrect(Error):
    pass


class LoginAlreadyExists(Error):
    pass


class RussianCharError(Error):
    pass


class CapitalLetterError(Error):
    pass


class NumberError(Error):
    pass


class SpecialCharError(Error):
    pass
