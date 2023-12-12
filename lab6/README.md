# Εργαστήριο 6 - Βασικοί κατάλογοι του συστήματος

## Περιεχόμενα μαθήματος

- [Βασικοί κατάλογοι του συστήματος](#βασικοί-κατάλογοι-του-συστήματος)

## Βασικοί κατάλογοι του συστήματος
[![asciicast](https://asciinema.org/a/RBKO7MhE03tA01riLHwFCZJeE.svg)](https://asciinema.org/a/RBKO7MhE03tA01riLHwFCZJeE)

Το μάθημα θα επικεντρωθεί στους βασικούς καταλόγους ενός συστήματος Linux. Το Linux έχει κληρονομήσει μια βασική αρχή των συστημάτων Unix: "στον κόσμο του Unix, τα πάντα είναι αρχεία."

Σύμφωνα με αυτή τη φιλοσοφία, όλες οι δομές και πληροφορίες του συστήματος, ανεξάρτητα από το είδος τους, παρουσιάζονται ως αρχεία. Αυτό σημαίνει ότι τα αρχεία δεδομένων, τα αρχεία εκτέλεσης, οι συσκευές, τα ημερολόγια καταγραφής συμβάντων (logs), ακόμη και τα περιφερειακά όπως οι συσκευές εισόδου/εξόδου, όλα αντιμετωπίζονται ως αρχεία. Αυτή η ομοιομορφία στον τρόπο που αντιμετωπίζονται τα παραπάνω οδηγεί σε ένα συνεκτικό σύστημα με διαφάνεια, απλότητα και επαναχρησιμοποίηση του κώδικα.

Στα πλαίσια αυτά, είναι σημαντικό να κατανοήσει κανείς τους βασικούς καταλόγους ενός συστήματος Linux. Οι τελευταίοι ορίζονται σύμφωνα με ένα πρότυπο, το Filesystem Hierarchy Standard (FHS). Το FHS καθορίζει τον τρόπο οργάνωσης και τοποθέτησης των αρχείων στο λειτουργικό σύστημα τύπου Unix, συμπεριλαμβανομένου του Linux. Το FHS προσδιορίζει τη δομή του αρχικού συστήματος αρχείων και τον ρόλο κάθε βασικού καταλόγου.

Ορισμένοι από τους βασικούς καταλόγους στο Linux, σύμφωνα με το FHS, αναλύονται παρακάτω.

### Κατάλογος /bin 
Ο κατάλογος `/bin` περιέχει τα βασικά εκτελέσιμα αρχεία (binaries) που απαιτούνται για την χρήση του συστήματος. Για παράδειγμα:

```console
stud@vm2:~$ ls /bin
bash           fuser       networkctl        su
bsd-csh        fusermount  nisdomainname     sync
bunzip2        getfacl     ntfs-3g           systemctl
busybox        grep        ntfs-3g.probe     systemd
bzcat          gunzip      ntfs-3g.secaudit  systemd-ask-password
bzcmp          gzexe       ntfs-3g.usermap   systemd-escape
bzdiff         gzip        ntfscat           systemd-hwdb
bzegrep        hciconfig   ntfscluster       systemd-inhibit
bzexe          hostname    ntfscmp           systemd-machine-id-setup
bzfgrep        ip          ntfsfallocate     systemd-notify
bzgrep         journalctl  ntfsfix           systemd-tmpfiles
bzip2          kbd_mode    ntfsinfo          systemd-tty-ask-password-agent
bzip2recover   kill        ntfsls            tailf
bzless         kmod        ntfsmove          tar
bzmore         less        ntfstruncate      tempfile
cat            lessecho    ntfswipe          touch
chacl          lessfile    open              true
chgrp          lesskey     openvt            udevadm
chmod          lesspipe    pidof             ulockmgr_server
chown          ln          ping              umount
chvt           loadkeys    ping6             uname
cp             login       plymouth          uncompress
cpio           loginctl    ps                unicode_start
csh            lowntfs-3g  pwd               vdir
dash           ls          rbash             wdctl
date           lsblk       readlink          which
dd             lsmod       red               whiptail
df             mkdir       rm                ypdomainname
dir            mknod       rmdir             zcat
dmesg          mktemp      rnano             zcmp
dnsdomainname  more        run-parts         zdiff
domainname     mount       sed               zegrep
dumpkeys       mountpoint  setfacl           zfgrep
echo           mt          setfont           zforce
ed             mt-gnu      setupcon          zgrep
efibootmgr     mv          sh                zless
egrep          nano        sh.distrib        zmore
false          nc          sleep             znew
fgconsole      nc.openbsd  ss
fgrep          netcat      static-sh
findmnt        netstat     stty
```

Παρατηρούμε ότι υπάρχουν αρκετές από τις βασικές εντολές που είδαμε στο μάθημα, όπως οι `ls`, `echo`, `grep`, `chmod`, κτλ.

Ας δούμε τα δικαιώματα της εντολής `ls`:

```console
stud@vm2:~$ ls -l /bin/ls
-rwxr-xr-x 1 root root 126584 Mar  2  2017 /bin/ls
```

Δηλαδή, η εντολή `ls` μπορεί να εκτελεστεί από όλους τους χρήστες. Ο διαχειριστής θα μπορούσε με την παρακάτω εντολή να αφαιρέσει το δικαίωμα εκτέλεσης από τους υπόλοιπους χρήστες.

```console
root@vm2:~# chmod o-x /bin/ls
root@vm2:~# ls -l /bin/ls
-rwxr-xr-- 1 root root 126584 Mar  2  2017 /bin/ls
```
Εαν αφαιρεθεί το δικαίωμα εκτέλεσης από τους λοιπούς χρήστες (others), τότε ένας απλός χρήστης δεν μπορεί να εκτελέσει την εντολή `ls`.

```console
stud@vm2:~$ ls
-bash: /bin/ls: Permission denied
```

Τέλος, με τον παρακάτω συνδυασμό εντολών μπορούμε να βρούμε όλες τις εντολές του `/bin` που έχουν τα γράμματα `rm` στο όνομα τους:

```console
stud@vm2:~$ ls /bin | grep rm
fusermount
ntfs-3g.usermap
rm
rmdir
```
Δηλαδή, τέσσερις εντολές του `/bin` έχουν τους χαρακτήρες `rm` στο όνομα τους.

Επιπρόσθετες εντολές μπορούν να βρεθούν στους καταλόγους `/usr/bin` (εντολές χρηστών) και `/sbin`, `/usr/sbin` (εντολές για τη διαχείριση του συστήματος).

### Κατάλογος /etc 
Ο κατάλογος `/etc` περιέχει τις ρυθμίσεις του συστήματος καθώς και των εγκατεστημένων προγραμμάτων. Οι ρυθμίσεις, όπως όλα στο Linux, είναι αρχεία.

Για παράδειγμα, το αρχείο `/etc/passwd` περιέχει τις παραμέτρους των λογαριασμών των χρηστών. Ας εμφανίσουμε τις παραμέτρους του χρήστη `stud`:

```console
stud@vm2:~$ cat /etc/passwd | grep stud
stud:x:1000:1000:student,,,:/home/stud:/bin/bash
```
Οι παράμετροι περιλαμβάνουν το όνομα του χρήστη (username), μοναδικούς αριθμούς (IDs) για τον χρήστη και την βασική του ομάδα (ονομάζονται UID και GID), την περιγραφή του, τον προσωπικό του κατάλογο, την γραμμή εντολών που χρησιμοποιεί (π.χ. bash), κ.α.

Στο παρελθόν, το δεύτερο πεδίο περιλάμβανε τον κρυπτογραφημένο κωδικό του χρήστη. Σήμερα αυτός βρίσκεται στο αρχείο `/etc/shadow`, το περιεχόμενο του οποίου δεν έχουμε δικαίωμα να δούμε ως απλοί χρήστες:
```console
stud@vm2:~$ ls -l /etc/shadow
-rw-r----- 1 root shadow 255431 Dec  5 11:25 /etc/shadow
```

### Κατάλογος /home
Ο κατάλογος `/home` περιλαμβάνει τους προσωπικούς καταλόγους των χρηστών, δηλαδή ο κάθε χρήστης έχει έναν ξεχωριστό υποκατάλογο για τα προσωπικά του αρχεία.

Ας μετρήσουμε τους καταλόγους των χρηστών στο σύστημα:
```console
stud@vm2:~$ ls /home | wc -l
2003
```

Τώρα ας δούμε τα δικαιώματα πρόσβασης στον προσωπικό κατάλογο του χρήστη `stud`:
```console
stud@vm2:~$ ls -al /home | grep stud
drwxr-----   33 stud         stud          4096 Dec  7 16:35 stud
```
Δηλαδή, μόνο ο χρήστης `stud` μπορεί να μπεί στον συγκεκριμένο κατάλογο και να δει ή να επεξεργαστεί τα αρχεία.

Υπενθυμίζουμε ότι ο χαρακτήρας `~` συμβολίζει τον προσωπικό κατάλογο του ενεργού χρήστη.

```console
stud@vm2:~$ echo ~
/home/stud
```

### Κατάλογοι /lib και /usr/lib
Ο κατάλογος `/lib` περιέχει τις βιβλιοθήκες (libraries) που απαιτούνται από τα εκτελέσιμα αρχεία στους καταλόγους `/bin` και `/sbin`, ενώ ο `/usr/lib` περιλαμβάνει γενικότερης χρήσης βιβλιοθήκες. 

Για παράδειγμα, στον κατάλογο `/lib` μπορούμε να βρούμε τις προεκτάσεις του πυρήνα (modules). Αποτελούν αυτόνομα συστήματα που μπορούν να ενεργοποιηθούν (ή να απενεργοποιηθούν) προσθέτοντας λειτουργικότητα στον πυρήνα, χωρίς επανεκκίνηση του υπολογιστή.

```console
stud@vm2:~$ ls /lib/modules/4.15.0-142-generic/kernel
arch   crypto   fs      lib  net    spl     virt       zfs
block  drivers  kernel  mm   sound  ubuntu  wireguard
```

### Κατάλογος /dev
Ο κατάλογος `/dev` περιέχει τα αρχεία που αντιπροσωπεύουν τις συσκευές στο σύστημα, όπως σκληροί δίσκοι, πληκτρολόγια, και άλλες συσκευές. Τα αρχεία αυτά είναι εικονικά. 

Για παράδειγμα, το αρχείο `/dev/null` αγνοεί ότι πληροφορία του στέλνεται. Μπορούμε να χρησιμοποιήσουμε αυτή τη συσκευή για να απορρίψουμε την έξοδο μιας εντολής:
```console
stud@vm2:~$ ls > /dev/null
stud@vm2:~$ 
```

Η συσκευή `/dev/zero` παράγει μηδενικά, ενώ οι συσκευές `/dev/random` και `/dev/urandom` παράγουν ψευδοτυχαίους αριθμούς (με υψηλή και χαμηλότερη εντροπία, αντίστοιχα).

Για παράδειγμα, η παρακάτω εντολή παράγει 8 τυχαίους χαρακτήρες:
```console
stud@vm2:~$ head -c 8 /dev/random
Qt�l�D3"
```

Άλλα αρχεία αντιπροσωπεύουν φυσικές συσκευές, όπως σκληρούς δίσκους (π.χ. `/dev/sda`, `/dev/sdb`), τερματικά (π.χ. φυσικά τερματικά - `/dev/ttyX` ή ψευδοτερματικά - `/dev/pts/X`, όπου `X` ο αριθμός του τερματικού), οπτικά μέσα αποθήκευσης (π.χ. `/dev/cdrom` και `/dev/dvd`), κ.α.

Μπορούμε να βρούμε το ψευδοτερματικό του χρήστη `stud`:

```console
stud@vm2:~$ ls -al /dev/pts | grep stud
crw--w----  1 stud tty  136, 0 Dec 12 09:45 0
stud@vm2:~$ echo "hello" > /dev/pts/0
hello
```
Δηλαδή μόνο ο ίδιος ο χρήστης και τα μέλη της ομάδας `tty` μπορούν να γράψουν στην οθόνη του `stud`.

### Κατάλογοι /mnt, /media και /cdrom
Χρησιμοποιείται για την προσωρινή προσάρτηση (mounting) εξωτερικών συσκευών ή filesystems.

### Κατάλογος /usr
Περιέχει τις εφαρμογές, τις βιβλιοθήκες και τα αρχεία δεδομένων για τους χρήστες.

### Κατάλογος /var
Περιέχει μεταβαλλόμενα αρχεία, όπως ημερολόγια του συστήματος (logs), προσωρινά αρχεία (κατάλογος `/var/tmp`), ή αρχεία που αντιπροσωπεύουν εργασίες που αναμένουν εκτέλεση, όπως οι εκτυπώσεις (κατάλογος `/var/spool`).

Για παράδειγμα, το αρχείο /var/log/auth.log καταγράφει γεγονότα που σχετίζονται με την επαλήθευση της ταυτότητας χρηστών:

```console
stud@vm2:/var/log$ tail -1 auth.log
Dec 12 09:51:39 vm2 sshd[16757]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.92.0.123  user=root
```
Δηλαδή, η τελευταία εγγραφή του αρχείου εντόπισε αποτυχημένη είσοδο στο σύστημα με τον λογαριασμό του διαχειριστή.

### Κατάλογος /tmp
Χρησιμοποιείται για την αποθήκευση προσωρινών αρχείων από εφαρμογές και χρήστες. Το περιεχόμενο αυτού του καταλόγου διαγράφεται κατά την επανεκκίνηση. Έχει ένα ειδικό καθεστώς στο σύστημα (που ορίζεται με το δικαίωμα `t`), όπου όλοι οι χρήστες μπορούν να δημιουργήσουν εκεί αρχεία, αλλά κανένας δεν μπορεί να διαγράψει αρχεία άλλου χρήστη:
```console
stud@vm2:~$ ls -al / | grep tmp
drwxrwxrwt    8 root     root      4096 Dec 12 09:30 tmp
```

### Κατάλογος /proc
Ο κατάλογος `/proc` στο Linux παρέχει πρόσβαση σε πληροφορίες και ρυθμίσεις του πυρήνα του λειτουργικού συστήματος. Προσέξτε ότι η πλειονότητα των ρυθμίσεων συστήματος γίνεται μέσω των αρχείων ρυθμίσεων, των εργαλείων διαχείρισης συστήματος ή των εντολών γραμμής εντολών, και όχι απευθείας μέσα από τον κατάλογο `/proc`.

Συγκεκριμένα, ο υποκατάλογος `/proc/sys/` παρέχει πρόσβαση σε διάφορες παραμέτρους και ρυθμίσεις του πυρήνα του Linux, όπως οι ρυθμίσεις δικτύου, η διαχείριση μνήμης κ.ά.

```console
stud@vm2:~$ ls /proc/sys
abi  debug  dev  fs  kernel  net  user  vm  xen
```

Για παράδειγμα, ένας χρήστης θα μπορούσε να διαβάσει το όνομα του υπολογιστή (hostname).

```console
stud@vm2:~$ cat /proc/sys/kernel/hostname
vm2
stud@vm2:~$ ls -al /proc/sys/kernel/hostname 
-rw-r--r-- 1 root root 0 Dec  1 14:41 /proc/sys/kernel/hostname
```

Η εντολή `echo "new_hostname" > /proc/sys/kernel/hostname` μπορεί να αλλάξει το όνομα του υπολογιστή εαν εκτελεστεί από τον διαχειριστή. Σημειώστε ότι αυτό δεν θα είναι μόνιμο και θα ισχύει μόνο για τη διάρκεια της τρέχουσας συνεδρίας.

Άλλα παραδείγματα είναι τα αρχεία `/proc/cpuinfo` και `/proc/meminfo` που εμφανίζουν πληροφορίες για τον επεξεργαστή ή την μνήμη.

Δηλαδή, η παρακάτω εντολή εμφανίζει την τρέχουσα διαθέσιμη μνήμη, η οποία αλλάζει δυναμικά.

```console
stud@vm2:~$ cat /proc/meminfo | grep MemFree
MemFree:          912068 kB
stud@vm2:~$ cat /proc/meminfo | grep MemFree
MemFree:          912332 kB
```

Το αρχείο `/proc/filesystems` εμφανίζει τα συστήματα αρχείων (filesystems) που υποστηρίζονται από τον πυρήνα του Linux:

```console
stud@vm2:~$ cat /proc/filesystems
nodev	sysfs
nodev	rootfs
nodev	ramfs
nodev	bdev
nodev	proc
nodev	cpuset
nodev	cgroup
nodev	cgroup2
nodev	tmpfs
nodev	devtmpfs
nodev	configfs
nodev	debugfs
nodev	tracefs
nodev	securityfs
nodev	sockfs
nodev	dax
nodev	bpf
nodev	pipefs
nodev	hugetlbfs
nodev	devpts
	ext3
	ext2
	ext4
	squashfs
	vfat
nodev	ecryptfs
	fuseblk
nodev	fuse
nodev	fusectl
nodev	pstore
nodev	mqueue
nodev	autofs
nodev	xenfs
nodev	binfmt_misc

```

Το αρχείο `/proc/loadavg` παρέχει πληροφορίες σχετικά με το φορτίο του συστήματος, συμπεριλαμβανομένων των μέσων φορτίων για την τελευταία 1, 5 και 15 λεπτά.

```console
stud@vm2:~$ cat /proc/loadavg
0.00 0.00 0.00 1/159 19840
```

Τέλος, στον υποκατάλογο `/proc` διατηρείται υποκατάλογος του τύπου `/proc/[PID]/` για κάθε πρόγραμμα που τρέχει στο σύστημα (ονομάζεται διεργασία και το [PID] είναι ο αριθμός αναγνώρισης της διεργασίας). Παρέχει πληροφορίες όπως η κατάσταση της διεργασίας, η κατανάλωση μνήμης κ.ά.

Δηλαδή, όπως και στην περίπτωση του καταλόγου `/dev`, τα αρχεία του καταλόγου `/proc` είναι εικονικά.
