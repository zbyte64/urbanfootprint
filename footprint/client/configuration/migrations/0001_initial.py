# Generated by Django 5.0.7 on 2024-08-06 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuiltFormFeatureLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='BuiltFormLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='CensusBlockgroupLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='CensusBlockLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='CensusTractLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='EnergyFeatureLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='FeatureLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='LayerSelectionSelectedLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='PhBlockGroupOutcomesLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='VmtFeatureLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
        migrations.CreateModel(
            name='WaterFeatureLayerStyle',
            fields=[
                ('layerstyle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.layerstyle')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.layerstyle',),
        ),
    ]
