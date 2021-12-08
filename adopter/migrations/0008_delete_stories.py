
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopter', '0007_stories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='stories',
        ),
    ]
