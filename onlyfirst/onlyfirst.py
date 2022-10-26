
def handle_file():
    pass


def process_single(text: str) -> str:
    inx = text.find('=')
    if inx == -1:
        raise Exception('no `=`')
    if text.count('\n') > 2:
        raise Exception('too many \\n')
    return text[:inx+1]


def process_paragraph(text: str) -> str:
    res = []
    for short in text.split('\n'):
        res.append(process_single(text))
    return "\n".join(res)
