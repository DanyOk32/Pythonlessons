-library models
-для створення моделі бази данних
models.Charfield(max_length: '<255!!!!')
.IntegerField()
.TextField(alot of symb)
.BooleanField()
.FloatDield()

django.forms import model_to_dict -(функція перетворює модель на дікт)




manage.py migrate - перетворює базу даних по всіх "міграціях"
manage.py migrate 'app' 'id of migr' | 'app' zero (відкат)
manage.py makemigration - записує зміни в "міграцію"


