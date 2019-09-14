import re
from rake_nltk import Rake


class PTagWrapMixin:

    def wrap_description_p_tag(self, field_name):
        if getattr(self, field_name):
            text_p_wrapped = [f'<p>{line.strip()}</p>' if not line.startswith('<p>') else line
                              for line in getattr(self, field_name).split('\n')]
            setattr(self, field_name, ''.join(text_p_wrapped))


def clean_html(raw_html):
    clean_pattern = re.compile('<.*?>')
    clean_text = re.sub(clean_pattern, '', raw_html)
    clean_text = re.sub(r'[^A-z]', ' ', clean_text)
    return clean_text


class KeywordExtractorMixin:

    def get_keywords(self, field_name):
        r = Rake()
        r.extract_keywords_from_text(clean_html(getattr(self, field_name)))
        keywords = r.get_ranked_phrases()
        if len(keywords) > 3:
            keywords = keywords[:3]
        return ', '.join(keywords)
