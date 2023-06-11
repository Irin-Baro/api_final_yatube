from rest_framework.serializers import ValidationError


class UniqueFieldsValueValidator:
    requires_context = True

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, data, serializer):
        field_values = []
        for field in self.fields:
            value = data[field]
            if value in field_values:
                raise ValidationError(f'Значение "{value}" '
                                      f'поля "{field}" не уникально.')
            field_values.append(value)
        return data
