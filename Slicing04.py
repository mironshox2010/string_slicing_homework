def main(s,n):
    """
    The s string variable is given. return n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return   s[-1*n:]
print(main( s="codeschooluz", n=3))
