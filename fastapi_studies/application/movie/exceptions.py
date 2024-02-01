
class ApplicationError(Exception):

    msg: str

    def __str__(self):
        return self.msg


class MoviesNotFound(ApplicationError):

    msg = "No movies were found for this parameters"


class MoviesOutOfRange(ApplicationError):

    msg = "The movies request if out of range"
