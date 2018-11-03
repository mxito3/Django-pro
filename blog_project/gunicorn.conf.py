import multiprocessing
bind="127.0.0.1:8000"
workers=4
errorlog="/home/yapie/github/Django-pro/gunicorn.error.conf"
accesslog="/home/yapie/github/Django-pro/gunicorn.access.log"
proc_name="gunicorn_blog_pro"