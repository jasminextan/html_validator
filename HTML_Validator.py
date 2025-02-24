#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of
    html validation by checking whether every
    opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to
    # generate a list of html tags without any extra text;
    # then process these html tags using the
    # balanced parentheses algorithm from the class/book
    # the main difference between your code and the code from class
    # will be that you will have to
    # keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    tags = _extract_tags(html)
    if '<' in html and '>' not in html:
        return False
    else:
        stack = []
        for tag in tags:
            if tag[1] != '/':
                stack.append(tag)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1][1:-1] == tag[2:-1]:
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions
    that are not meant to be used directly by the
    user are prefixed with an underscore.
    This function returns a list of all
    the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    inside_tag = False
    tags = []
    tag = ''
    for char in html:
        if char == '<':
            inside_tag = True
        if char == '>':
            tag += char
            inside_tag = False
            tags.append(tag)
            tag = ''
        if inside_tag is True:
            if char == ' ':
                inside_tag = False
            else:
                tag += char
        else:
            pass
    return tags
