from operator import attrgetter

from rest_framework.reverse import reverse
from rest_framework import serializers

class HyperlinkedNestedIdentityField(serializers.HyperlinkedIdentityField):
    def __init__(self, view_name=None, additional_reverse_kwargs={}, **kwargs):
        self.additional_reverse_kwargs = additional_reverse_kwargs
        super(HyperlinkedNestedIdentityField, self).__init__(view_name, **kwargs)
 
    def get_url(self, obj, view_name, request, format):
        if obj.pk is None:
            return None

        kwargs = {}
        for key, value in self.additional_reverse_kwargs.items():
            kwargs[key] = getattr(obj, value, value)
        kwargs.update({self.lookup_url_kwarg: getattr(obj, self.lookup_field)})
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)

class HyperlinkedNestedRelatedField(serializers.HyperlinkedRelatedField):
    def __init__(self, view_name=None, additional_reverse_kwargs={}, **kwargs):
        self.additional_reverse_kwargs = additional_reverse_kwargs
        super(HyperlinkedNestedRelatedField, self).__init__(view_name, **kwargs)

    def to_representation(self, value):
        request = self.context.get('request', None)
        format = self.context.get('format', None)
        return self.get_url(value, self.view_name, request, format)

    def get_url(self, obj, view_name, request, format):
        """
        Given an object, returh the URL that hyperlinks to the object

        May raise a `NoReverseMatch` if the `view_name` and `lookup_field` 
        attributes are not configured to correctly match the URL conf.
        """
        kwargs = {}
        for key, value in self.additional_reverse_kwargs.items():
            kwargs[key] = getattr(obj, value, None)
        kwargs.update({self.lookup_url_kwarg: attrgetter(self.lookup_field)(obj)})
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)
