from SublimeLinter.lint import PythonLinter


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

def split_match(self, match):
        """
        Return the components of the error message.
        We override this to customize the message.
        """
        match, line, col, error, warning, message, near = super().split_match(match)

        if match:

            message = "This %s had a Radon cyclomatic complexity rank of %s, and scored %s." % (type_code[match.group('type')], match.group('code'), message,  message_code[message])

        return match, line, col, error, warning, message, near