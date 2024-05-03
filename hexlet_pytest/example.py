def reverse(string):
    """Reverse string

    >>> reverse('')
    ''

    >>> reverse('Hexlet')
    'telxeH'
    """


    return string[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
