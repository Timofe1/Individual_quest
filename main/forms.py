import pymysql
from django.forms import ModelForm, TextInput, Textarea
from .models import Atributs


class FlowersAdd(ModelForm):
    class Meta:
        model = Atributs
        fields =['nameProduct', 'productPrice', 'description', 'typeProduct']
        #
        widgets = {
            'nameProduct': TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Название продукта'
            }),
            'productPrice': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена продукта'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание продукта'
            }),
            'typeProduct': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип продукта'
            }),
        }

        # try:
        #     connection = pymysql.connect(
        #         host='84.201.184.150',
        #         user='090303-pia-21_t',
        #         password='BEcFckRg4L',
        #         database='090303-pia-21_TIMA_KOVTUNEC',
        #
        #     )
        #     print("\n Подключение с изменением успешно  \n")
        #     try:
        #         # cursor = connection.cursor()
        #         with connection.cursor() as cursor:
        #             select_query = "INSERT INTO `flowers` (nameProduct, productPrice, description, typeProduct) VALUES (nameProduct, productPrice, description, typeProduct)"
        #             cursor.execute(select_query)
        #             connection.commit()
        #
        #     finally:
        #         connection.close()
        # except Exception as ex:
        #     print("\n Ошибка подключения с изменением  \n")
        #     print(ex)