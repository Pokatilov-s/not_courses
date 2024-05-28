from store.serializers import TransactionsDetailsModelSerializer, UserCourseSerializer


def create_pay_transaction(data):
    serializer = TransactionsDetailsModelSerializer(data=data)
    if serializer.is_valid():
        transaction = serializer.save()
        return transaction.uuid


def enroll_user_in_course(data):
    serializer = UserCourseSerializer(data=data)
    if serializer.is_valid():
        obj = serializer.save()
        return obj.uuid
