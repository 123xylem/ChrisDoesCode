# from django import _get_queryset
def clean_text(text: str, answer=False) -> str:
    text = text.replace('\\n', '\n')
    text = text.replace('\\t', '\t')

    if answer:
        return f'<pre><code>{text}</code></pre>'
    return text
