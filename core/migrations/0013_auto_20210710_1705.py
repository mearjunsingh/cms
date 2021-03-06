# Generated by Django 3.2.5 on 2021-07-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_ad_target'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Site',
        ),
        migrations.AlterField(
            model_name='ad',
            name='target',
            field=models.CharField(choices=[('ads_side1', 'Sidebar Top'), ('ads_side2', 'Sidebar Between'), ('ads_side3', 'Sidebar Bottom'), ('ads_header', 'Header'), ('ads_footer', 'Footer'), ('ads_homepage', 'Homepage'), ('ads_belowThumbnail', 'Below Thumbnail'), ('ads_belowPost', 'Below Post'), ('ads_belowRelated', 'Below Related'), ('ads_betweenPosts', 'Between Posts (Per 5)'), ('ads_belowFirstSection', 'Below First Section (Homepage)'), ('ads_belowSecondSection', 'Below Second Section (Homepage)')], max_length=50, unique=True, verbose_name='Ad Target'),
        ),
    ]
