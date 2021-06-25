from SublimeLinter.lint import PythonLinter


class Radon(PythonLinter):
    cmd = 'radon cc ${file_on_disk} -s -n B --total-average'
    regex = (
        r'^(?P<type>[a-zA-z])\s(?P<line>\d+):(?P<col>\d+).+-\s(?P<code>[a-zA-Z])\s\((?P<message>\d+)'
    )
    multiline = True
    defaults = {
        'selector': 'source.python'
    }
