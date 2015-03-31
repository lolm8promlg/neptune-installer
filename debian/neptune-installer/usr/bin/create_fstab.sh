#!/bin/bash
#
# disks.sh	Search all the local disks and write them into the /etc/fstab.
#
# Version:	@(#)disks.sh  1.0  15-Oct-2005  juanje@interactors.coop
# edited by Leszek Lesner 2009
# Changelog:
# 2014 -  Distinguish mount options between root and home partition
#	  Use new partitions script for getting uuid and filesystemtype
# 2013 -  Added UUID handling
#         Cleanup of swap adding code
#         Seperating CDROM adding code from SWAP adding code
#         Execute home partition stuff only if HEIM is true
#         Added debugging output for root home and swap
#         
#         Added fallback option if blkid uuid get failed
#         Changed get UUID code to use file instead of blkid
#         Write directly to /tmp/neptune-installer.log
#         Fixed UUID detection
#         Fixed Fallback if UUID detection fails for root or home
#         Use blkid for UUID detection, code cleanup



# Target partition
FSCHOICE=$1

# Target mountpoint 
MNT=$2

# Seperate home
HEIM=$3

# Seperate home partition
HEIMORT=$4

# Get Filesystemtype (the dirty way)
#FSROOT=`df -T | grep $FSCHOICE | tr -s " " | cut -d " " -f 2`

# Get Filesystemtype (the new better way)
FSROOT=`partitions get_filesystem $FSCHOICE`

# Get UUIDs
FSCHOICEUUID=`partitions get_partition_uuid $FSCHOICE`

# Get Filesystemtype from home
FSHOME=`partitions get_filesystem $HEIMORT`

# Globally set mount options
if [ "$FSROOT" == "btrfs" ]; then
  # btrfs
  ROOT_MOUNT_OPT="defaults"
else
  # ext4 and all others basically
  ROOT_MOUNT_OPT="defaults,errors=remount-ro"
fi
if [ "$FSHOME" == "btrfs" ]; then
  # btrfs
  HOME_MOUNT_OPT="defaults"
else
  # ext4 and all others basically
  HOME_MOUNT_OPT="defaults,errors=remount-ro"
fi



if [ "$HEIM" = "j" ]; then
    HEIMORTUUID=`partitions get_partition_uuid $HEIMORT`

    if [ -z "$FSCHOICEUUID" ] || [ -z "$HEIMORTUUID" ]; then 
        # Fallback here
        

	cat <<EOF > $MNT/etc/fstab
# /etc/fstab: static file system information.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
proc            /proc           proc    defaults        0       0
sys             /sys            sysfs   defaults        0       0

$FSCHOICE	/		$FSROOT $ROOT_MOUNT_OPT 0       1
$HEIMORT	/home		$FSHOME	$HOME_MOUNT_OPT 0	   1

EOF

        echo " "
        echo "$FSCHOICE  /  $FSROOT $ROOT_MOUNT_OPT 0 1    added to /etc/fstab"
        echo "$HEIMORT   /home  $FSHOME $HOME_MOUNT_OPT 0 1     added to /etc/fstab"


     else
         # UUID here

	cat <<EOF > $MNT/etc/fstab
# /etc/fstab: static file system information.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
proc            /proc           proc    defaults        0       0
sys             /sys            sysfs   defaults        0       0

UUID=$FSCHOICEUUID	/		$FSROOT $ROOT_MOUNT_OPT 0       1
UUID=$HEIMORTUUID	/home		$FSHOME	$HOME_MOUNT_OPT 0	   1

EOF

         echo " "
         echo "UUID=$FSCHOICEUUID  /  $FSROOT $ROOT_MOUNT_OPT 0 1    added to /etc/fstab"
         echo "UUID=$HEIMORTUUID   /home  $FSHOME $HOME_MOUNT_OPT 0 1     added to /etc/fstab"

    fi

else 
    if [ -z "$FSCHOICEUUID" ]; then 
    
    # Fallback here

	  cat <<EOF > $MNT/etc/fstab
# /etc/fstab: static file system information.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
proc            /proc           proc    defaults        0       0
sys             /sys            sysfs   defaults        0       0

$FSCHOICE	/		$FSROOT $MOUNT_OPT 0       1

EOF
          echo " "
	  echo "$FSCHOICE  /  $FSROOT $ROOT_MOUNT_OPT 0 1   added to /etc/fstab"


    else
        # UUID here

    cat <<EOF > $MNT/etc/fstab
# /etc/fstab: static file system information.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
proc            /proc           proc    defaults        0       0
sys             /sys            sysfs   defaults        0       0

UUID=$FSCHOICEUUID	/		$FSROOT $ROOT_MOUNT_OPT 0       1

EOF

        echo " "
        echo "UUID=$FSCHOICEUUID  /  $FSROOT $ROOT_MOUNT_OPT 0 1   added to /etc/fstab"


    fi


fi
#
# Search for CD/DVDs
#
get_cdroms ()
{
	echo $(head -3 /proc/sys/dev/cdrom/info | tail -1 | cut -f 3-)
}

#
# Add Swap to fstab
#
addSwap_fstab ()
{
	DEVLIST="$(ls /dev/[h-s]d[a-z][0-9]*)"
        for DEV in $DEVLIST
        do
                FS="$(file -sL "$DEV")"
                DEVUUID=`/sbin/blkid -s UUID -o value $DEV`
                #echo $FS # DEBUG
                case "$FS" in 
  		*swap*)
    			# Do stuff
                        echo "SWAP found"
                        entry="UUID=${DEVUUID}  none    swap    sw              0       0"
                        echo $entry >> $MNT/etc/fstab
                        echo "$entry added to /etc/fstab"
    			;;
		esac
        done
}

#
# Add CD/DVD to fstab
#
addCd_fstab ()
{
	# Add cdroms/dvdroms here
	num=0
	cdroms=$(get_cdroms)
	for cd in $cdroms; do
		entry="/dev/${cd}        /media/cdrom${num}   udf,iso9660 ro,user,noauto  0       0"
		mkdir -p $MNT/media/cdrom${num} 2>&1 > /dev/null
		let num=num+1
		echo $entry >> $MNT/etc/fstab
	done
	
}

get_device ()
{
	dev=$(grep /.dirs/dev /proc/mounts | cut -d " " -f 1)
	echo $dev
}

addSwap_fstab
addCd_fstab
 

exit 0
