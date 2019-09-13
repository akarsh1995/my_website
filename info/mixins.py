class PTagWrapMixin:

    def wrap_description_p_tag(self, field_name):
        if getattr(self, field_name):
            text_p_wrapped = [f'<p>{line.strip()}</p>' if not line.startswith('<p>') else line
                              for line in getattr(self, field_name).split('\n')]
            setattr(self, field_name, ''.join(text_p_wrapped))
