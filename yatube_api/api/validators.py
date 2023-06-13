from rest_framework.serializers import ValidationError


class UniqueFieldsValueValidator:
    def __init__(self, fields):
        self.fields = fields

    def check_fields(self, data):
        missing_fields = [field for field in self.fields if field not in data]
        if missing_fields:
            raise KeyError(
                [f'Поле "{field}" отсутствует в сериализаторе'
                 for field in missing_fields]
            )

    def __call__(self, data):
        self.check_fields(data)
        field_values = {data[field] for field in self.fields}
        if len(field_values) != len(self.fields):
            raise ValidationError(
                [f'Значение "{data[field]}" поля "{field}" не уникально.'
                 for field in self.fields]
            )
