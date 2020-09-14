Edit your settings.py as following

Add os.path.join(BASE_DIR, 'polls/templates') to your TEMPLATES
Add 'polls' app to INSTALLED_APPS
Set allowed hosts to all ALLOWED_HOSTS = ['*']

Run `python manage.py makemigrations polls`
Run `python manage.py migrate`
Run `python manage.py shell` in your project directory
    ```
    >>> from polls.models import Choice, Question
    >>> from django.utils import timezone
    >>> q = Question(question_text="Answer to the Ultimate Question", pub_date=timezone.now())
    >>> q.save()
    >>> q.choice_set.create(choice_text='42', votes=0)
    ```
Run `python manage.py createsuperuser` and create superuser with the username that has been given at your assignment and so is your password

Copy the url you got in ngrok and paste it at the assignment.

