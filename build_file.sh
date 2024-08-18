pip install -r requirements.txt



echo "collect static ...  "
python3 manage.py collectstatic --noinput --clear


echo "make migration...."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput