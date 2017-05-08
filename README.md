# rsync-backup
Rsync Backupscript



Adjust the script to your config and configure your cronjobs like this ```crontab -e``` then enter:
```0 5 * * * python /root/backup.py```

script runs everyday at 5 o' clock in the morning and syncs to disks.

parts of interest:
```FUNCTION_WRITE_LOG("/var/log/cron_backup", "starting backup...")``` this is where your logfile will be written.
```returnvalue = os.system('rsync -auv --log-file=/var/log/cron_backup --delete /mnt/shari/ /mnt/backuphdd/')``` Rsync specific. ```-auv```means:
* a = archive mode
* u = skip file if source is older than target
* v = verbose

```delete``` means: delete extraneous files from destination dirs. 
```/mnt/shari``` is the sourcedir and ```/mnt/backuphdd``` is the backuplocation
