class ApplicationError(Exception):

    msg: str

    def __str__(self):
        return self.msg


class MoviesNotFound(ApplicationError):
    msg = "No movies were found for this parameters"


class PageOutOfRange(ApplicationError):
    msg = "The requested page is out of range"
