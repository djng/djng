# -*- coding: utf-8 -*-
import re

regex = re.compile('^<(?P<name>.*)>\s*(?P<email>.*@.*)')


def parse_emails(emails):
    """
    Parse a list of emails of the following format:
    <John Doe> john@abc.com, <Betty Boo> boo@bbs.com
    :param str emails: "Comma separated emails"
    :return: A list of name, email tuples
    :rtype: list
    """
    if not emails:
        return []

    email_tuples = []
    for email in emails.split(','):
        r = regex.match(email.strip())
        if r:
            email_tuples.append(r.groups())

    return email_tuples


def bool_value(value, default=False):
    """
    Convert strings like 'yes', 'y', 'true', '1',
    'no', 'n', 'false', '0' or '' to boolean values.
    :param str value: "Value to parse to bool"
    :param bool default: "Default value if unable to convert"
    :rtype: bool
    """
    if not value:
        return default

    true_values = ('yes', 'y', 'true', '1')
    false_values = ('no', 'n', 'false', '0', '')
    normalized_value = value.strip().lower()
    if normalized_value in true_values:
        return True
    elif normalized_value in false_values:
        return False
    else:
        return default
