# rsync-backup
Rsync Backupscript



Adjust the script to your config and configure your cronjobs like this:
```crontab -e``` then enter: ```0 5 * * * python /root/backup.py``` and save.

script runs everyday at 5 o' clock in the morning and syncs to disks.


parts of interest:

 `logfile` is where your logfile will be written to.

```returnvalue = os.system('rsync -auv --log-file=/var/log/cron_backup --delete /mnt/shari/ /mnt/backuphdd/')```
Rsync specific. ```-auv```means:
* a = archive mode
* u = skip file if source is older than target
* v = verbose
* --delete = delete extraneous files from destination dirs.

```/mnt/shari``` is the sourcedir and ```/mnt/backuphdd``` is the backuplocation
