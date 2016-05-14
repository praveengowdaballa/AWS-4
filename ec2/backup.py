#!/usr/bin/python

import boto

# kreiraj snpashot

ec2 = boto.connect_ec2('Access key','Secret Access key')
volumes = ec2.get_all_volumes()
for volume in volumes:
	ec2.create_snapshot(volume.id,"backup made with backup script")


# izbrisi snapshot

ec2 = boto.connect_ec2('Access key','Secret Access key')
volumes = ec2.get_all_volumes()
for volume in volumes:
	if snapshot.description=="backup made with backup script":
		snapshot.delete()