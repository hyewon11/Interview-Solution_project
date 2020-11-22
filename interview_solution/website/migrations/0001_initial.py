<<<<<<< HEAD
# Generated by Django 3.0.3 on 2020-11-18 00:53
=======
# Generated by Django 3.0.7 on 2020-11-12 16:55
>>>>>>> b3bbbb4c003c908f00bdddb93880eb2667194d54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('userID', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='아이디')),
                ('username', models.CharField(blank=True, max_length=10, null=True, verbose_name='유저이름')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='연락처')),
                ('school', models.CharField(blank=True, max_length=10, null=True, verbose_name='학교')),
                ('grade', models.CharField(blank=True, max_length=10, null=True, verbose_name='학년')),
                ('sClass', models.CharField(blank=True, max_length=10, null=True, verbose_name='반')),
                ('is_activate', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('question', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='질문')),
                ('department', models.IntegerField(blank=True, null=True, verbose_name='학과')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('userID', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='아이디')),
                ('username', models.CharField(blank=True, max_length=10, null=True, verbose_name='유저이름')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='연락처')),
                ('school', models.CharField(blank=True, max_length=15, null=True, verbose_name='학교')),
                ('grade', models.IntegerField(blank=True, null=True, verbose_name='학년')),
                ('sClass', models.IntegerField(blank=True, null=True, verbose_name='반')),
                ('is_activate', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentQuestion',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('title', models.CharField(default='제목', max_length=100, verbose_name='제목')),
<<<<<<< HEAD
                ('video1', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='영상1')),
                ('video2', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='영상2')),
                ('video3', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='영상3')),
=======
                ('video_url1', models.URLField(blank=True, null=True, verbose_name='영상1 url')),
                ('video_url2', models.URLField(blank=True, null=True, verbose_name='영상2 url')),
                ('video_url3', models.URLField(blank=True, null=True, verbose_name='영상3 url')),
                ('video1', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='영상1')),
                ('video2', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='영상2')),
                ('video3', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='영상3')),
                ('audio1_url1', models.URLField(blank=True, null=True, verbose_name='음성1 url')),
                ('audio2_url2', models.URLField(blank=True, null=True, verbose_name='음성2 url')),
                ('audio3_url3', models.URLField(blank=True, null=True, verbose_name='음성3 url')),
>>>>>>> b3bbbb4c003c908f00bdddb93880eb2667194d54
                ('audio1', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='음성1')),
                ('audio2', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='음성2')),
                ('audio3', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='음성3')),
                ('script1', models.CharField(blank=True, max_length=50000, null=True, verbose_name='스크립트1')),
                ('script2', models.CharField(blank=True, max_length=50000, null=True, verbose_name='스크립트2')),
                ('script3', models.CharField(blank=True, max_length=50000, null=True, verbose_name='스크립트3')),
                ('adverb1', jsonfield.fields.JSONField(default=dict)),
                ('adverb2', jsonfield.fields.JSONField(default=dict)),
                ('adverb3', jsonfield.fields.JSONField(default=dict)),
                ('repetition1', jsonfield.fields.JSONField(default=dict)),
                ('repetition2', jsonfield.fields.JSONField(default=dict)),
                ('repetition3', jsonfield.fields.JSONField(default=dict)),
                ('speed1', models.FloatField(blank=True, null=True, verbose_name='말하기 속도1')),
                ('speed2', models.FloatField(blank=True, null=True, verbose_name='말하기 속도2')),
                ('speed3', models.FloatField(blank=True, null=True, verbose_name='말하기 속도3')),
                ('comment1', models.CharField(blank=True, max_length=10000, null=True, verbose_name='댓글1')),
                ('comment2', models.CharField(blank=True, max_length=10000, null=True, verbose_name='댓글2')),
                ('comment3', models.CharField(blank=True, max_length=10000, null=True, verbose_name='댓글3')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='날짜')),
                ('share', models.BooleanField(default=True, verbose_name='공유')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Teacher'),
        ),
        migrations.AddField(
            model_name='user',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Teacher'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
