#!/bin/bash
#
# Neptune Installer 0.90
#
# A small Installerscript to Install Neptune. Released under Beerware (C) (R)
#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# Leszek Lesner wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.
# ----------------------------------------------------------------------------
#
# unoffical german translation:
#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# Leszek Lesner schrieb diese Datei. Solange Sie diesen Vermerk nicht entfernen,
# können Sie mit der Datei machen, was Sie möchten. Wenn wir uns eines Tages treffen
# und Sie denken, die Datei ist es wert, können Sie mir dafür ein Bier ausgeben.
# ----------------------------------------------------------------------------
#
# by Leszek Lesner <leszek@zevenos.com>

exec > /tmp/neptune-installer.log 2>&1

### Check if Xorg is running
xorg=`ps -A | grep Xorg | wc -l`
if [ $xorg == 1 ]; then 
  msgbox=gdialog 
else
  msgbox=dialog
fi

### Ask for language
if [ "$LANG" == "de_DE.UTF-8" ]
then
  language=de;
else
  language=en;
fi

### Check if uefi
[ -d /sys/firmware/efi ] && efi_enabled="yes" || efi_enabled="no"

# Load language specific messages
welcome=`awk 'NR==1' /usr/share/neptune-installer/$language.messages`
askroot=`awk 'NR==2' /usr/share/neptune-installer/$language.messages`
askroot2=`awk 'NR==3' /usr/share/neptune-installer/$language.messages`  
wrongpw=`awk 'NR==4' /usr/share/neptune-installer/$language.messages`
userask=`awk 'NR==5' /usr/share/neptune-installer/$language.messages`
usercreatemsg=`awk 'NR==6' /usr/share/neptune-installer/$language.messages`
userpwask=`awk 'NR==7' /usr/share/neptune-installer/$language.messages`
userpwask2=`awk 'NR==8' /usr/share/neptune-installer/$language.messages`
mntcreate=`awk 'NR==9' /usr/share/neptune-installer/$language.messages`
partitionmanager=`awk 'NR==10' /usr/share/neptune-installer/$language.messages`
cancel=`awk 'NR==11' /usr/share/neptune-installer/$language.messages`
menucontrols=`awk 'NR==12' /usr/share/neptune-installer/$language.messages`
format=`awk 'NR==13' /usr/share/neptune-installer/$language.messages`
endpart=`awk 'NR==14' /usr/share/neptune-installer/$language.messages`
cfdiskpart=`awk 'NR==15' /usr/share/neptune-installer/$language.messages`
mkfspart=`awk 'NR==16' /usr/share/neptune-installer/$language.messages`
mkfsformat=`awk 'NR==17' /usr/share/neptune-installer/$language.messages`
targetpart=`awk 'NR==18' /usr/share/neptune-installer/$language.messages`
mnttarget=`awk 'NR==19' /usr/share/neptune-installer/$language.messages`
homeask=`awk 'NR==20' /usr/share/neptune-installer/$language.messages`
homepart=`awk 'NR==21' /usr/share/neptune-installer/$language.messages`
homeskip=`awk 'NR==22' /usr/share/neptune-installer/$language.messages`
grubask=`awk 'NR==23' /usr/share/neptune-installer/$language.messages`
grubansweryes=`awk 'NR==24' /usr/share/neptune-installer/$language.messages`
grubanswerno=`awk 'NR==25' /usr/share/neptune-installer/$language.messages`
installmsg=`awk 'NR==26' /usr/share/neptune-installer/$language.messages`
configuremsg=`awk 'NR==27' /usr/share/neptune-installer/$language.messages`
installgrubmsg=`awk 'NR==28' /usr/share/neptune-installer/$language.messages`
grubpartask=`awk 'NR==29' /usr/share/neptune-installer/$language.messages`
fstabmsg=`awk 'NR==30' /usr/share/neptune-installer/$language.messages`
sephomemsg=`awk 'NR==31' /usr/share/neptune-installer/$language.messages`
configurehomemsg=`awk 'NR==32' /usr/share/neptune-installer/$language.messages`
userskipmsg=`awk 'NR==33' /usr/share/neptune-installer/$language.messages`
initramfsmsg=`awk 'NR==34' /usr/share/neptune-installer/$language.messages`
configureusermsg=`awk 'NR==35' /usr/share/neptune-installer/$language.messages`
movehomemsg=`awk 'NR==36' /usr/share/neptune-installer/$language.messages`
installendmsg=`awk 'NR==37' /usr/share/neptune-installer/$language.messages`

### Start Welcome msgbox ###
# $msgbox --msgbox "$welcome" 5 50
# clear ;
# if [ "$msgbox" == "gdialog" ]; then
#   zenity --entry --hide-text --text "$askroot" >tmp.pwd
# else
#   $msgbox --insecure --passwordbox "$askroot" 0 0 2>tmp.pwd
# fi
# opt=${?}
#     if [ $opt != 0 ]; then rm tmp.*; exit 1; fi		# Abort Installation if pressed Cancel
ROOTPWD=`cat /tmp/neptune-installer/tmp.pwd`
# if [ "$msgbox" == "gdialog" ]; then
#   zenity --entry --hide-text --text "$askroot2" >tmp.pwd2
# else
#   $msgbox --insecure --passwordbox "$askroot2" 0 0 2>tmp.pwd2
# fi
# opt=${?}
#     if [ $opt != 0 ]; then rm tmp.*; exit 1; fi
# ROOTPWD2=`cat tmp.pwd2`
# if [ "$ROOTPWD" != "$ROOTPWD2" ]; then
# 	$msgbox --msgbox "$wrongpw" 5 50;
# 	exit 1;fi;

### Setup new user & password + groups ###
# $msgbox --inputbox "$userask" 0 0 2> tmp.user
# clear ;
BENUTZER=`cat /tmp/neptune-installer/tmp.user` ;
VOLLERNUTZERNAME=`cat /tmp/neptune-installer/tmp.cuser` ;
# echo $usercreatemsg ;
# ##### Necessary ######
if [ ! -e /tmp/neptune-installer-sudoDisabled.tmp ]
then
  adduser user sudo ;
else
  cp /usr/lib/kde4/libexec/kdesu-distrib/kdesu /usr/bin/kdesu ;
  update-alternatives --set kdesu /usr/lib/kde4/libexec/kdesu-distrib/kdesu ;
  su user -c "kwriteconfig --file kdesurc --group super-user-command --key super-user-command su"
  cp /home/user/.kde/share/config/kdesurc /usr/share/neptune-base/profiles/kde-profile/share/config/kdesurc
fi
# adduser user scanner ; # should fix scanner problems after install
# adduser fuse ; # important for mount encrypted filesystems
# adduser lpadmin ; # important for printer configuration support
# if [ "$msgbox" == "gdialog" ]; then
#   zenity --entry --hide-text --text "$userpwask" > tmp.userpwd
# else
#   $msgbox --insecure --passwordbox "$userpwask" 0 0 2> tmp.userpwd
# fi
# opt=${?}
#     if [ $opt != 0 ]; then rm tmp.*; exit 1; fi
BENUTZERPWD=`cat /tmp/neptune-installer/tmp.userpwd`
# if [ "$msgbox" == "gdialog" ]; then
#   zenity --entry --hide-text --text "$userpwask2" > tmp.userpwd2
# else
#   $msgbox --insecure --passwordbox "$userpwask2" 0 0 2> tmp.userpwd2
# fi
# opt=${?}
#     if [ $opt != 0 ]; then rm tmp.*; exit 1; fi
# BENUTZERPWD2=`cat tmp.userpwd2`
# if [ "$BENUTZERPWD" != "$BENUTZERPWD2" ]; then
# 	$msgbox --msgbox "$wrongpw" 5 50;
# 	exit 1;fi;


### Create a mountpoint for our target partition ###
echo "";
echo $mntcreate 
mkdir -p /hdinstall ;
if [ "$msgbox" == "gdialog" ]; then
  dcopRef=`kdialog --progressbar "$mntcreate" 10` ;
  export dcopRef
  qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 1
fi

### Get partition and mount it under hdinstall ###
clear ;
export TARGET=`cat /tmp/neptune-installer/tmp.hd` ;
umount $TARGET
if [ -f /tmp/neptune-installer-formatRoot.tmp ]; then
  echo "Formatting..."
  if [ -f /tmp/neptune-installer-formatRootExt4.tmp ]; then
    mkfs.ext4 -F $TARGET -L "NEPTUNE" 
    if [ ! "$?" == 0 ]; then
    echo "Formatting failed!"
    exit 1
    fi
  elif [ -f /tmp/neptune-installer-formatRootF2FS.tmp ]; then
    mkfs.f2fs -l "NEPTUNE" $TARGET
    if [ ! "$?" == 0 ]; then
    echo "Formatting failed!"
    exit 1
    fi
  else
    mkfs.btrfs -f -L "NEPTUNE" $TARGET
    if [ ! "$?" == 0 ]; then
      echo "Formatting failed!"
      exit 1
    fi
  fi
fi
echo "" ;
echo "$mnttarget" ;
mount $TARGET /hdinstall ;
EXT4check=$(mount | grep $TARGET | cut -d " " -f 5)
if [ "$msgbox" == "gdialog" ]; then
  qdbus $dcopRef setLabelText "$mnttarget"
  qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 2
fi

### Asking for seperate home partition ###
if [ -e /tmp/neptune-installer/tmp.home ]; then
	HEIM=0
else
	HEIM=1
fi

if [ $HEIM = 0 ]; then
    	HEIMORT=`cat /tmp/neptune-installer/tmp.home` ;
else
	clear ;
	echo "" ;
	echo "$homeskip" ;
fi

if [ ! -e /tmp/neptune-installer/tmp.grubskip ]; then
      ### Asking if GRUB should be installed to MBR or root  ###
      if [ ! -e /tmp/neptune-installer/tmp.grubpart ]; then 
	    GRUBMBR=0
      else
	    GRUBMBR=1
      fi

      if [ $GRUBMBR = 0 ]; then
	    clear ;		
	    echo "$grubansweryes" ;
      else
	    clear ;
	    GRUBMBR=no
	    echo "$grubanswerno" ;
      fi
fi

### Begin copying files ###
#orig_size="1740"
#dest_size_before=$(df -m $TARGET | cut -b32- | awk '/\/hdinstall/{used+=$1} END{print used}')
#dest_size_diff=0
echo "" ;
echo "$installmsg" ;
if [ "$msgbox" == "gdialog" ]; then
  qdbus $dcopRef setLabelText "$installmsg"
  qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 3
  rsync -av --progress / /hdinstall --exclude=/{hdinstall,live,sys,proc,media,home,rofs,cdrom,mnt,var/run,run}/ | awk -f /usr/bin/rsync.awk | cut -c -35 | zenity --progress --width=350 --title "$installmsg" --text="Copying..." --percentage=0 --auto-close;
else
  rsync -av --progress / /hdinstall --exclude=/{hdinstall,live,sys,proc,media,home,rofs,cdrom,mnt,var/run,run}/ ;
fi
# rsync=$!	Progressbar seems not to work this way
# old_percent=0
# 	while ps --pid $rsync &>/dev/null
# 	do
# 		dest_size=$(df -m $TARGET | cut -b32- | awk '/\/hdinstall/{used+=$1} END{print used}')
# 		dest_size_diff=$(( $dest_size - $dest_size_before ))
# 		percent=$((( 100 * $dest_size_diff ) / $orig_size ))
# 		if [ "$percent" != "$old_percent" ]; then
# 			echo "$percent %" 
# 			old_percent="$percent"
# 		fi
# 		sleep 5
# 	done

echo "" ;
echo "$configuremsg" ;
mkdir -p /hdinstall/proc /hdinstall/sys /hdinstall/media /hdinstall/run /hdinstall/var/run ;
if [ "$msgbox" == "gdialog" ]; then
  qdbus $dcopRef setLabelText "$configuremsg"
  qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 4
fi

echo "" ;
echo "$installgrubmsg" ;

### Progressbar kde way with kdialog ;) 
if [ "$msgbox" == "gdialog" ]; then
  qdbus $dcopRef setLabelText "$installgrubmsg"
  qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 5
fi 

### Binding /proc, /dev, /sys to chroot ###
mount --bind /proc /hdinstall/proc ;
mount --bind /sys /hdinstall/sys;
mount --bind /dev /hdinstall/dev ;
mount --bind /dev /hdinstall/dev/pts ;

### Install Grub and chroot into system ###
function install_grub_efi() {
mkdir -p /hdinstall/tmp/efi
cp /live/image/efi/*.deb /hdinstall/tmp/efi/
cp /etc/default/grub /hdinstall/tmp/efi/
cat << EOF > /hdinstall/tmp/grub-efi-install.sh
export DEBIAN_FRONTEND=noninteractive
apt-get -y remove grub-pc;
dpkg -i /tmp/efi/*.deb;
mv /tmp/efi/grub /etc/default/grub 
EOF
          chmod 777 /hdinstall/tmp/grub-efi-install.sh
          chroot /hdinstall /tmp/grub-efi-install.sh;
}

mkdir -p /boot/grub ;
mkdir -p /hdinstall/boot/grub ;
cp /usr/lib/grub/i386-pc/* /hdinstall/boot/grub ;
if [ ! -e /tmp/neptune-installer/tmp.grubskip ]; then
	if [ $GRUBMBR = 0 ]; then
		if [ $efi_enabled == "yes" ]; then
		  install_grub_efi
		  mkdir -p /boot/efi ;
		  mkdir -p /hdinstall/boot/efi ;
		  efi_part=$(partitions list_efi_partitions)
		  mount $efi_part /boot/efi ;
		  mount -o bind /boot/efi /hdinstall/boot/efi ;
		  chroot /hdinstall grub-install --recheck --no-floppy /dev/sda
		else 
		  grub-install --recheck --no-floppy --root-directory=/hdinstall /dev/sda
		fi
		
	else
		clear ;
		export TARGET2=`cat /tmp/neptune-installer/tmp.grubpart` ;
		if [ $efi_enabled == "yes" ]; then
		  install_grub_efi
		  mkdir -p /boot/efi ;
		  mkdir -p /hdinstall/boot/efi ;
		  efi_part=$TARGET2
		  mount $efi_part /boot/efi ;
		  mount -o bind /boot/efi /hdinstall/boot/efi ;
		  grub-install --recheck --no-floppy --root-directory=/hdinstall /dev/sda
		else
		  grub-install --recheck --no-floppy --root-directory=/hdinstall $TARGET2
		fi
	fi
fi

if [ $efi_enabled == "yes" ]; then
  if [ ! -e /boot/efi/EFI/BOOT ]; then
    mkdir -p /boot/efi/EFI/BOOT;
    cp /boot/efi/EFI/neptune/grubx64.efi /boot/efi/EFI/BOOT/bootx64.efi
  fi
fi

if [ "$msgbox" == "gdialog" ]; then
    qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 6
fi
### Search for installed systems and update-grub ###
/usr/bin/os-prober ; 
chroot /hdinstall /usr/sbin/update-grub ;

### Create new fstab for the installed system ###
if [ "$msgbox" == "gdialog" ]; then
    qdbus $dcopRef setLabelText "$fstabmsg"
    qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 7
fi
echo "" ;
echo "$fstabmsg" ;
rm /hdinstall/etc/fstab ;
if [ $HEIM = 0 ]; then
		HEIM=j ;
else
		HEIM=n ;
fi

if [ "$msgbox" == "gdialog" ]; then
      qdbus $dcopRef setLabelText "$configurehomemsg"
      qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 8
fi

if [ "$HEIM" = "j" ]; then
	echo "" ;
        echo "$sephomemsg";
        mkdir -p /sephome ;
        mount $HEIMORT /sephome ;
	if [ -d /sephome/$BENUTZER ]; then	# if home dir already exist don't overwrite
		echo "$homeskip"
        else         
	      rsync -av --progress /home/ /sephome ;
	fi
else
	echo "" ;
        echo "$configurehomemsg";
        mkdir -p /hdinstall/home ;
        if [ -d /hdinstall/home/$BENUTZER ]; then
		echo "$homeskip"
        else         
    	rsync -av --progress /home/ /hdinstall/home ;
	fi
fi
# Create Fstab
/usr/bin/create_fstab.sh $TARGET /hdinstall $HEIM $HEIMORT

### Final Cleanup ###
echo "$initramfsmsg"
cp /live/cow/usr/sbin/update-initramfs.distrib /hdinstall/usr/sbin/update-initramfs
#chroot /hdinstall /usr/bin/apt-get -y purge live-initramfs

# GDM/GDM3/KDM Autologin config
if [ -f /hdinstall/etc/gdm/gdm.conf ]; then
  sed -i  -e "s/AutomaticLoginEnable=true//" \
	  -e "s/AutomaticLogin=user//" \
	  -e "s/TimedLoginEnable=true//" \
	/hdinstall/etc/gdm/gdm.conf ;
fi
if [ -f /hdinstall/etc/gdm3/daemon.conf ]; then
  sed -i  -e "s/AutomaticLoginEnable=true//" \
	  -e "s/AutomaticLogin=user//" \
	  -e "s/TimedLoginEnable=true//" \
	/hdinstall/etc/gdm3/daemon.conf ;
fi
if [ -f /hdinstall/etc/default/kdm.d/live-autologin ]; then
  rm /hdinstall/etc/default/kdm.d/live-autologin ;
fi
if [ -f /hdinstall/etc/kde4/kdm/kdmrc ]; then
  sed -i -r -e "s/^#?AutoLoginEnable=.*\$/AutoLoginEnable=false/" \
	    -e "s/^#?AutoLoginUser=.*\$/AutoLoginUser=/" \
	    -e "s/^#?AutoReLogin=.*\$/AutoReLogin=false/" \
	    -e "s/^#?PreselectUser=.*\$/PreselectUser=Default/" \
	    -e "s/^#?DefaultUser=.*\$/DefaultUser=$BENUTZER/" \
        /hdinstall/etc/kde4/kdm/kdmrc
fi

if [ "$msgbox" == "gdialog" ]; then
      qdbus $dcopRef setLabelText "$configureusermsg"
      qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 9
fi

echo "$configureusermsg"
TMPDIR="/hdinstall/tmp/update.$$"
mkdir -p "$TMPDIR"
cp /hdinstall/etc/passwd $TMPDIR/
cp /hdinstall/etc/shadow $TMPDIR/
cp /hdinstall/etc/group $TMPDIR/
#cp /hdinstall/etc/sudoers $TMPDIR/
#chmod 666 $TMPDIR/sudoers ;

# Change User in passwd file
sed "s/Live user/$VOLLERNUTZERNAME/g; s/user/$BENUTZER/g; s,/home/user,/home/$BENUTZER,g" $TMPDIR/passwd > /hdinstall/etc/passwd ;

# Change User in shadow file
sed "s/user/$BENUTZER/g;" $TMPDIR/shadow > /hdinstall/etc/shadow ;

# Change Passwords for root and user
chroot /hdinstall sh -c "echo 'root:$ROOTPWD' | chpasswd " ;
chroot /hdinstall sh -c "echo '$BENUTZER:$BENUTZERPWD' | chpasswd " ;

# change user in group
sed "s/user/$BENUTZER/g;" $TMPDIR/group > /hdinstall/etc/group ;

# activate sudo for main user
#sed "s/user/$BENUTZER/g;" $TMPDIR/sudoers > /hdinstall/etc/sudoers ;
#sed -i "s/$BENUTZER  ALL=(ALL) NOPASSWD: ALL/$BENUTZER  ALL=(ALL) ALL/g;" /hdinstall/etc/sudoers ;
#chmod 440 /hdinstall/etc/sudoers ;

rm -rf "$TMPDIR"

if [ "$msgbox" == "gdialog" ]; then 
    qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 10
fi
  
if [ "$HEIM" = "j" ]; then
        rm -rf /hdinstall/home ;
        if [ -d /sephome/$BENUTZER ]; then
	echo "Verschieben des Homeverzeichnisses nicht nötig"
	else
	mv /sephome/user /sephome/$BENUTZER;
	rm /sephome/$BENUTZER/Desktop/neptune-installer.desktop ;
	rm /sephome/$BENUTZER/Desktop/*.pdf ;
	fi        
	mkdir /hdinstall/home ;
	umount -lf /sephome ;
	mount  $HEIMORT /hdinstall/home ;
	if [ -d "/hdinstall/home/$BENUTZER" ]; then
		chroot "/hdinstall" chown -R "$BENUTZER":"$BENUTZER" "/home/$BENUTZER"
	fi
else
        #rm -rf /hdinstall/home/user ;
        mv /hdinstall/home/user /hdinstall/home/$BENUTZER;
	if [ -d "/hdinstall/home/$BENUTZER" ]; then
		chroot "/hdinstall" chown -R "$BENUTZER":"$BENUTZER" "/home/$BENUTZER"
	fi
	rm /hdinstall/home/$BENUTZER/Desktop/neptune-installer.desktop ;
	rm /hdinstall/home/$BENUTZER/Desktop/*.pdf ;
        # rm /hdinstall/usr/sbin/neptune-installer  ; #  Delete Installerscript (DEBUG for the moment)
fi

# Create Icon on Desktop that links to Forum
url="http://www.zevenos.com/forum/forumdisplay.php?fid=21" ;
cat >"/hdinstall/home/$BENUTZER/Desktop/Neptune.desktop" <<EOF
[Desktop Entry]
Name=Neptune Forum
Exec=x-www-browser $url
Type=Application
Icon=text-html
Terminal=0
EOF
chmod 777 /hdinstall/home/$BENUTZER/Desktop/Neptune.desktop

#rm "/hdinstall/home/$BENUTZER/.mozilla/firefox/q2vijr9i.default/extensions.ini" ; old debugging for firefox
cp -f "/hdinstall/usr/share/sysvinit/inittab" "/hdinstall/etc/inittab" ; # use the right inittab
#cp -f "/etc/skel/.gconf/apps/gksu/%gconf.xml" "/hdinstall/home/$BENUTZER/.gconf/apps/gksu/" ; # fix for gksu
cp -f "/tmp/neptune-installer.log" "/hdinstall/var/log/neptune-installer.log" ; # copy installation log
rm -r "/hdinstall/home/$BENUTZER/.kde/share/apps/kfileplaces" ;
rm -r "/hdinstall/home/$BENUTZER/.config/akonadi" ;
rm "/hdinstall/home/$BENUTZER/Desktop/persistent-creator.desktop" ;
rm "/hdinstall/etc/skel/Desktop/persistent-creator.desktop" ;
rm /hdinstall/etc/skel/Desktop/*.pdf ;
rm "/hdinstall/etc/skel/Desktop/neptune-installer.desktop" ;
rm "/hdinstall/etc/environment" ;
touch "/hdinstall/etc/environment" ;
ln -sf "/home/$BENUTZER/.config/fontconfig/fonts.conf" "/hdinstall/home/$BENUTZER/.fonts.conf";
echo "" > /hdinstall/etc/mtab ;
#cp -f "/etc/skel/.mozilla/firefox/q2vijr9i.default/chrome/userChrome.css" "/hdinstall/home/$BENUTZER/.mozilla/firefox/q2vijr9i.default/chrome/" ;

# Delete unecessary packages
echo "Entfernen von nicht benötigten Paketen in /hdinstall"
chroot /hdinstall dpkg --remove snapshot-manager ;
chroot /hdinstall dpkg --remove persistent-creator ;
#chroot /hdinstall dpkg --remove live-initramfs ; # Is removed with apt-get purge before already
chroot /hdinstall dpkg --remove neptune-installer ;
#chroot /hdinstall dpkg --remove neptune-advanced-installer ; # Isn't installed at all
cat << EOF > /hdinstall/tmp/remove-live-initramfs.sh
export DEBIAN_FRONTEND=noninteractive
export DEBCONF_NONINTERACTIVE_SEEN=true
apt-get -y remove live-initramfs;
EOF
chmod 777 /hdinstall/tmp/remove-live-initramfs.sh
chroot /hdinstall /tmp/remove-live-initramfs.sh

if [ "$msgbox" == "gdialog" ]; then 
    qdbus $dcopRef org.freedesktop.DBus.Properties.Set org.kde.kdialog.ProgressDialog value 10
fi

# For the startup only on first start
# TODO: Replace with fwizard
#touch /hdinstall/home/$BENUTZER/firstrun
#chmod 777 /hdinstall/home/$BENUTZER/firstrun
#cat >"/hdinstall/usr/bin/checkfirstrun" <<EOF
##!/bin/bash
#if [ -f ~/firstrun ]
#then
#    echo "firstrun exists!"
#    rm ~/firstrun;
#    mplayer -fs /etc/xdg/linuxad.avi
#fi
#EOF
#chmod 777 /hdinstall/usr/bin/checkfirstrun;

#rm /hdinstall/etc/live.conf ;
rm /hdinstall/tmp/neptune-installer/tmp.* ;
umount -l /hdinstall/dev/pts ;
umount -l /hdinstall/dev ;
umount -l /hdinstall/proc ;
umount -l /hdinstall/sys ;
umount -l /hdinstall ;

if [ "$msgbox" == "gdialog" ]; then
	qdbus $dcopRef close
fi


### End Message ###
$msgbox --msgbox "$installendmsg" 0 0
