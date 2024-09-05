# from django import _get_queryset
def clean_text(text: str, answer=False) -> str:

    # Replace double newlines with paragraph tags
    text = text.replace('\\n', '\n')
    # text = text.replace('b\'', '', 1)
    # text = text.replace('b"', '', 1)
    text = text.replace('\\t', '\t')
    # text = text.removesuffix('\'')
    # text = text.removesuffix('"')

    if answer:
        return f'<pre><code>{text}</code></pre>'
    return text
