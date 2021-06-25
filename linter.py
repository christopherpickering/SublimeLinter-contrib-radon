from SublimeLinter.lint import PythonLinter
#import logging
#logger = logging.getLogger('SublimeLinter.plugins.radon')


type_code = {
    'F': "function",
    "M": "method",
    "C": "class",
}

message_code = {
    "A": "A (1-5) low - simple block.",
    "B": "B (6-10) low - well structured and stable block.",
    "C": "C (11-20) moderate - slightly complex block.",
    "D": "D (21-30) more than moderate - more complex block.",
    "E": "E (31-40) high - complex block, alarming.",
    "F": "F (41+) very high - error-prone, unstable block.",
}


class Radon(PythonLinter):
    cmd = 'radon cc ${file_on_disk} -s -n B'
    regex = (
        r'^\s+(?P<type>[a-zA-z])\s'
        r'(?P<line>\d+):(?P<col>\d+).+-\s'
        r'(?P<code>[a-zA-Z])\s(?P<warning>\()(?P<message>\d+)'
    )
    multiline = True
    defaults = {
        'selector': 'source.python',
    }

    
    def split_match(self, match):
        """
        Return the components of the error message.
        We override this to customize the message.
        """
        match, line, col, error, warning, message, near = super().split_match(match)
        #logger.error(match, line, col, error, warning, message, near)
        #logger.error(super().split_match(match))
        if match:

            message = "This %s had a Radon cyclomatic complexity rank of %s, and scored %s.\n%s" % (type_code[match.group('type')], match.group('code'), message,  message_code[match.group('code')])

        return match, line, col, error, warning, message, near