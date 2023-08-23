# Generated by Django 4.2.4 on 2023-08-21 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('biography', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(null=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('date', models.DateField()),
                ('isbn', models.CharField(max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.authors')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('short_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookshelf.languages')),
            ],
        ),
        migrations.CreateModel(
            name='UserProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookshelf.books')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookshelf.languages')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.styles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.users')),
            ],
        ),
        migrations.CreateModel(
            name='UserDictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.CharField(max_length=255)),
                ('translate', models.CharField(max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.users')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraphs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.books')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookshelf.tags')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.books')),
                ('par_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.paragraphs')),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('short_name', models.CharField(max_length=10)),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookshelf.languages')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.languages'),
        ),
        migrations.CreateModel(
            name='BookGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.books')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshelf.genres')),
            ],
        ),
        migrations.AddField(
            model_name='authors',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookshelf.countries'),
        ),
        migrations.AddField(
            model_name='authors',
            name='lang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookshelf.languages'),
        ),
    ]