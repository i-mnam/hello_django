from django import forms


class LocationWidget(forms.TextInput):
    template_name = 'blog/widgets/location_widget.html'

    class Media:
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            '//maps.googleapis.com/maps/api/js', # FIXME : api key 지정할 예정
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['readonly'] = True #attrs['readonly'] = 'readonly'
        attrs['style'] = 'background-color: #eee; border:0;'
        return attrs