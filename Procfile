web: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py ensure_admin && python -m gunicorn aawaaragardi.wsgi --bind 0.0.0.0:$PORT
