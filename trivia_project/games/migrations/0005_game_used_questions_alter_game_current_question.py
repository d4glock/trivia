# Generated by Django 5.1.3 on 2024-12-14 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_remove_game_question_count'),
        ('questions', '0003_alter_question_options_alter_question_option_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='used_questions',
            field=models.ManyToManyField(blank=True, related_name='games_used_in', to='questions.question'),
        ),
        migrations.AlterField(
            model_name='game',
            name='current_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_games', to='questions.question'),
        ),
    ]