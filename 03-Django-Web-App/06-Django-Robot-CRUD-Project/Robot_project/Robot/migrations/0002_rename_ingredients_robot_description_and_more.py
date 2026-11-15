
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Robot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='robot',
            old_name='ingredients',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='robot',
            name='instructions',
        ),
        migrations.AddField(
            model_name='robot',
            name='robot_type',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
    ]
