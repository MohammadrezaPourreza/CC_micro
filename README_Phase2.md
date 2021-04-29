# CC_micro
ترتیب دستورات برای ایجاد داکر ایمیج
توجه کنید داکر ایمیج ساخته شده بر روی ویندوز با استفاده از دبلیواس ال ساخته شده است
دستوراتی که برای اجرا نیاز داشتیم:
1)"C:\Program Files\Docker\Docker\DockerCli.exe" -SwitchDaemon
2)docker-compose build
3)docker-compose up db
4)docker-compose run web
توجه کنید که برای ران شدن بر روی ویندوز به جای دستور 4 عم باید دستور زیر را بزنید
docker-compose --service-ports run web

