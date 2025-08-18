from django.db import migrations

def populate_usernames(apps, schema_editor):
    CustomUser = apps.get_model('accounts', 'CustomUser')
    for user in CustomUser.objects.filter(username__isnull=True):
        base = user.email.split('@')[0]
        candidate = base
        suffix = 1
        while CustomUser.objects.filter(username=candidate).exists():
            candidate = f"{base}{suffix}"
            suffix += 1
        user.username = candidate
        user.save(update_fields=['username'])

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_username'),
    ]

    operations = [
        migrations.RunPython(populate_usernames, reverse_code=migrations.RunPython.noop),
    ]
