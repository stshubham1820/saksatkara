# Generated by Django 5.1.1 on 2024-09-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0006_alter_assessmentskills_assessment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentanswers',
            name='answer_audio',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assessmentanswers',
            name='answer_video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assessmentquestions',
            name='question_audio',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='assessmentanswers',
            table='question_answers',
        ),
        migrations.AlterModelTable(
            name='assessmentquestions',
            table='assessment_questions',
        ),
    ]
