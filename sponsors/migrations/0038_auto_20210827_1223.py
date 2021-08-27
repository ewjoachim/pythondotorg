# Generated by Django 2.0.13 on 2021-08-27 12:23

from django.db import migrations


def populate_sponsorship_package_fk(apps, schema_editor):
    Sponsorship = apps.get_model('sponsors.Sponsorship')
    SponsorshipPackage = apps.get_model('sponsors.SponsorshipPackage')

    for sponsorship in Sponsorship.objects.all().iterator():
        try:
            package = SponsorshipPackage.objects.get(name=sponsorship.level_name)
            sponsorship.package = package
            sponsorship.save()
        except SponsorshipPackage.DoesNotExist:
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0037_sponsorship_package'),
    ]

    operations = [
        migrations.RunPython(populate_sponsorship_package_fk, migrations.RunPython.noop)
    ]