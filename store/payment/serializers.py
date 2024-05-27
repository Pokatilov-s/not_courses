from rest_framework import serializers
import datetime as dt
from store.services import get_published_course


class PaymentSerializer(serializers.Serializer):
    bank = serializers.CharField(max_length=25)
    card_number = serializers.CharField(max_length=16)
    cvv = serializers.CharField(max_length=3)
    expiry_date = serializers.CharField(max_length=5)
    course_uuid = serializers.UUIDField()


    def validate_bank(self, value):
        if value not in ['Банк у обочины', 'Банк №101', 'Банк МММ']:
            raise serializers.ValidationError('Не разрешённый банк')
        return value


    def validate_card_number(self, value):
        if len(value) not in (13, 14, 15, 16) or not value.isdigit():
            raise serializers.ValidationError('Некорректный номер карты, '
                                              'номер должен состоять только из цифр '
                                              'и иметь длину от 13 до 16 символов')
        return value


    def validate_cvv(self, value):
        if len(value) != 3 or not value.isdigit():
            raise serializers.ValidationError('Некорректный CVV код, должен состоять из трёх цифр')
        return value


    def validate_expiry_date(self, value):
        current_data = dt.datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if (len(value) != 5
                or not (value[:2].isdigit() and value[2] == '/' and value[3:].isdigit())
                or not (0 < int(value[:2]) < 13)
                or current_data > dt.datetime.strptime(value, '%m/%y')):
            raise serializers.ValidationError('Не корректный срок действия, должен быть в формате MM/YY '
                                              'и быть больше текущей даты')
        return value


    def validate_course_uuid(self, value):
        try:
            get_published_course(pk=value)
            return value
        except Exception as e:
            raise serializers.ValidationError(e)
