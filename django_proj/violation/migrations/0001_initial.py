# Generated by Django 3.2.9 on 2021-11-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.FloatField(verbose_name='studentID')),
                ('lastName', models.CharField(max_length=50, verbose_name='lastName')),
                ('firstName', models.CharField(max_length=50, verbose_name='firstName')),
                ('middleName', models.CharField(blank=True, max_length=50, verbose_name='middleName')),
                ('course', models.CharField(choices=[('BET', 'Bachelor of Engineering Technology'), ('BSE', 'Bachelor of Science in Engineering'), ('BSIE', 'Bachelor of Science in Industrial Education'), ('BTTE', 'Bachelor of Technical Teacher Education')], default='', max_length=5, verbose_name='course')),
                ('major', models.CharField(choices=[('AET', 'Automotive'), ('CT', 'Civil'), ('COET', 'Computer'), ('ESET', 'Electronics'), ('EET', 'Electrical'), ('MPET', 'Mechanical'), ('PPET', 'Powerplant'), ('ICT', 'Information Communication Technology'), ('IA', 'Industrial Arts'), ('CPET', 'Computer Programming'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), ('EE', 'Electrical Engineering')], default='', max_length=10, verbose_name='major')),
                ('section', models.CharField(choices=[('S-1A', 'S-1A'), ('NS-1B', 'NS-1B'), ('S-2A', 'S-2A'), ('NS-2B', 'NS-2B'), ('S-3A', 'S-3A'), ('NS-3B', 'NS-3B'), ('S-4A', 'S-4A'), ('NS-4A', 'NS-4A')], default='', max_length=10, verbose_name='section')),
                ('studentNo', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='studentNo')),
                ('schoolYear', models.FloatField(verbose_name='schoolYear')),
                ('existingViolation', models.CharField(blank=True, choices=[('Littering', 'Littering'), ('Loitering', 'Loitering'), ('Vandalism', 'Vandalism'), ('Gambling', 'Gambling'), ('Improper haircut', 'Improper haircut'), ('Improper public behavior', 'Improper public behavior'), ('Improper uniform', 'Improper uniform'), ('Wearing of hats in class', 'Wearing of hats in class'), ('Unauthorized use of water', 'Unauthorized use of water'), ('Use of gadgets during class', 'Use of gadgets during class'), ('Wearing of piercing', 'Wearing of piercing'), ('Cross-dressing', 'Cross-dressing')], default='', max_length=100, verbose_name='existingViolation')),
                ('existingComSer', models.CharField(blank=True, choices=[('Summer break volunteer', 'Summer break volunteer'), ('Cafeteria volunteer', 'Cafeteria volunteer'), ('Organizing recyclables', 'Organizing recyclables'), ('Waste segregation', 'Waste segregation'), ('Planting plants', 'Planting plants'), ('Library personnel', 'Library personnel'), ('Garbage collection volunteer', 'Garbage collection volunteer'), ('Community sweeping', 'Community sweeping')], default='', max_length=100, verbose_name='existingComSer')),
                ('remainComSerTime', models.DecimalField(blank=True, decimal_places=0, max_digits=2, verbose_name='remainComSerTime')),
                ('addViolation', models.CharField(choices=[('Littering', 'Littering'), ('Loitering', 'Loitering'), ('Vandalism', 'Vandalism'), ('Gambling', 'Gambling'), ('Improper haircut', 'Improper haircut'), ('Improper public behavior', 'Improper public behavior'), ('Improper uniform', 'Improper uniform'), ('Wearing of hats in class', 'Wearing of hats in class'), ('Unauthorized use of water', 'Unauthorized use of water'), ('Use of gadgets during class', 'Use of gadgets during class'), ('Wearing of piercing', 'Wearing of piercing'), ('Cross-dressing', 'Cross-dressing')], default='', max_length=100, verbose_name='addViolation')),
                ('addComSer', models.CharField(choices=[('Summer break volunteer', 'Summer break volunteer'), ('Cafeteria volunteer', 'Cafeteria volunteer'), ('Organizing recyclables', 'Organizing recyclables'), ('Waste segregation', 'Waste segregation'), ('Planting plants', 'Planting plants'), ('Library personnel', 'Library personnel'), ('Garbage collection volunteer', 'Garbage collection volunteer'), ('Community sweeping', 'Community sweeping')], default='', max_length=100, verbose_name='addComSer')),
                ('offenseType', models.CharField(choices=[('First offense', 'First offense'), ('Second offense', 'Second offense'), ('Third Offense', 'Third Offense')], default='', max_length=25, verbose_name='offenseType')),
                ('addComSerTime', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='addComSerTime')),
            ],
        ),
    ]
