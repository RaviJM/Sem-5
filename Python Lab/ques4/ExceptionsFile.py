class OSNotFoundException(Exception):
    # Raised when OS is not found
    pass


class OSVersionNotSupportedException(Exception):
    # Raised when required version of OS is not available
    pass


class PythonVersionNotSupportedException(Exception):
    # Raised when required version of Python is not available
    pass


class NumpyNotSupportedException(Exception):
    # Raised when required version of Numpy is not available
    pass


class PandasVersionNotSupportedException(Exception):
    # Raised when required version of Pandas is not available
    pass


class TensorflowVersionNotSupportedException(Exception):
    # Raised when required version of Tensorflow is not available
    pass


