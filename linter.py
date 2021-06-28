"""Sublimelinter plugin for Radon cyclomatic complexity."""
from SublimeLinter.lint import PythonLinter

type_code = {
    "F": "Function",
    "M": "Method",
    "C": "Class",
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
    """Radon complexity linter.

    Regex output
    ============

    type: M/F/C (Method, Function, Class)
    line: line number of exception
    col: col number of exception
    message: M/F/C name
    code: A-F complexity rank
    value: numberic value of complexity

    Message output: <type_code> <message> has a complexity rank of <code> (<warning>).

    Code output: <code>

    Warning: if A/B/C
    Error: all other ranks

    """

    cmd = "radon cc ${temp_file} -s -n B"
    defaults = {
        "selector": "source.python",
    }
    line_col_base = (1, 0)
    multiline = True
    regex = (
        r"^\s+(?P<type>[a-zA-z])\s(?P<line>\d+):"
        r"(?P<col>\d+)\s(?P<message>.+)\s-\s"
        r"(?P<code>[a-zA-Z])\s\((?P<warning>\d+)\)"
    )
    tempfile_suffix = "py"

    def split_match(self, match):
        """
        Return the components of the error message.

        We override this to customize the message.
        """
        output = super().split_match(match)

        output["message"] = "%s %s has a complexity rank of %s (%s)." % (
            type_code[match.group("type")],
            match.group("message"),
            match.group("code"),
            match.group("value"),
        )

        return output
