# Εργαστήριο 8 - Διεργασίες

## Περιεχόμενα μαθήματος

- [Διεργασίες στο Linux](#διεργασίες-στο-linux)

## Διεργασίες στο Linux
[![asciicast](https://asciinema.org/a/RBKO7MhE03tA01riLHwFCZJeE.svg)](https://asciinema.org/a/RBKO7MhE03tA01riLHwFCZJeE)

Το μάθημα θα επικεντρωθεί στις διεργασίες (processes) και τις σχετικές εντολές του Linux.

Μια διεργασία αποτελεί την εκτέλεση ενός προγράμματος. Αποτελείται από οδηγίες εκτέλεσης αλλά και δεδομένα (π.χ. που διαβάζονται από αρχεία ή αποτελούν είσοδο από έναν χρήστη.

Οποιαδήποτε εντολή δίνεται στον υπολογιστή ξεκινά μια νέα διεργασία και τερματίζει όταν ολοκληρώνει η εντολή τις λειτουργίες που επιτελεί.

Έχουμε τρείς διαφορετικούς τύπους διεργασιών:
1. *Διαλογικές* - αρχικοποιούνται και ελέγχονται από μια σύνοδο τερματικού. Μπορούν να βρίσκονται είτε στο προσκήνιο (`fg`), είτε στο παρασκήνιο (`bg`). Οι διαλογικές διεργασίες συνδέονται με ένα τερματικό.
2. *Αυτόματες* - εκτελούνται συγκεκριμένη μέρα και ώρα (μέσω των εντολών `cron` ή `at`, αντίστοιχα) ή όταν ο φόρτος του συστήματος είναι αρκετά χαμηλός (εντολή `batch`). Οι αυτόματες διεργασίες δεν συνδέονται με κάποιο τερματικό.
3. *Δαίμονες (daemons)* - αποτελούν διεργασίες διακομιστή που εκτελούνται συνεχώς, π.χ. ο δαίμονας της σύνδεσης ssh που ονομάζεται sshd, ο διακομιστής ιστοσελίδων (web server) httpd.

Ο πυρήνας διατηρεί στη μνήμη του λίστα με όλες τις διεργασίες που χειρίζεται, καταγράφοντας τις παρακάτω πληροφορίες:
1. *Ιδιοκτήτης* - ο χρήστης στον οποίον ανήκει η διεργασία (π.χ. αυτός που εκτέλεσε το σχετικό πρόγραμμα).
2. *Ιδιοκτήτρια ομάδα* - σε ποια ομάδα χρηστών ανήκει η διεργασία.
3. *PID (Process ID)* - Μοναδικός αριθμός που αποτελεί την ταυτότητα της διεργασίας.
4. *PPID (Parent PID)* - Η ταυτότητα της γονικής διεργασίας.
5. *STIME (Start Time)* - Η ώρα εκκίνησης της διεργασίας.
6. *ΤΙΜΕ* - για πόσο χρόνο έχει καταλάβει η διεργασία την CPU.
7. *TTY* - με ποιο τερματικό συνδέεται η διεργασία.
8. *CMD* - ποια εντολή δημιούργησε τη διεργασία.
9. *ENV* - πίνακας με τις μεταβλητές περιβάλλοντος της διεργασίας. Οι μεταβλητές περιβάλλοντος στο Linux είναι προσδιορισμένες τιμές που αποθηκεύονται στο σύστημα και χρησιμοποιούνται από τις εφαρμογές και το κέλυφος για να προσδιορίσουν παραμέτρους, όπως διαδρομές αρχείων και άλλες ρυθμίσεις.
10. *STATUS* - η κατάσταση της διεργασίας (π.χ. created, waiting, running, terminated, blocked ή swapped out).
11. *Priority* - η προτεραιότητα της διεργασίας την οποία μπορεί να ορίσει ο χρήστης, αν έχει το αντίστοιχο δικαίωμα.

Μπορούμε να εμφανίσουμε τις ενεργές διεργασίες στο σύστημα με τη βοήθεια της εντολής `top`. Η τελευταία λειτουργεί περίπου όπως ο task manager των Windows. Στο πάνω μέρος της οθόνης εμφανίζονται διάφορες γενικές πληροφορίες για τις διεργασίες και τους πόρους που καταναλώνουν.

Στη συνέχεια, παρατίθονται οι διεργασίες, ταξινομημένες από την περισσότερο απαιτητική σε πόρους στην λιγότερο.
 
```console
stud@vm2:~$ top
top - 11:48:28 up 4 days, 21:06,  1 user,  load average: 0.00, 0.00, 0.00
Tasks: 128 total,   1 running,  81 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.1 st
KiB Mem :  3031196 total,   832868 free,   200340 used,  1997988 buff/cache
KiB Swap:   999420 total,   999420 free,        0 used.  2576184 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
  736 avahi     20   0   45040   3576   3196 S   0.3  0.1   0:51.56 avahi-daem+
    1 root      20   0  185344   5868   3836 S   0.0  0.2   0:08.50 systemd
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.03 kthreadd
    4 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/0:+
    6 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 mm_percpu_+
    7 root      20   0       0      0      0 S   0.0  0.0   0:00.33 ksoftirqd/0
    8 root      20   0       0      0      0 I   0.0  0.0   0:58.87 rcu_sched
    9 root      20   0       0      0      0 I   0.0  0.0   0:00.00 rcu_bh
   10 root      rt   0       0      0      0 S   0.0  0.0   0:00.06 migration/0
   11 root      rt   0       0      0      0 S   0.0  0.0   0:01.59 watchdog/0
   12 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/0
   13 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/1
   14 root      rt   0       0      0      0 S   0.0  0.0   0:01.33 watchdog/1
   15 root      rt   0       0      0      0 S   0.0  0.0   0:00.22 migration/1
   16 root      20   0       0      0      0 S   0.0  0.0   0:00.32 ksoftirqd/1
   18 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/1:+
   19 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/2
   20 root      rt   0       0      0      0 S   0.0  0.0   0:01.50 watchdog/2
```

Η εντολή `top` τερματίζει με το πλήκτρο `q`.

Μια άλλη χρήσιμη εντολή είναι η εντολή `ps`, η οποία εμφανίζει πληροφορίες σχετικά με τις ενεργές διεργασίες.

Ας δοκιμάσουμε την εντολή `ps`:

```console
stud@vm2:~$ ps
  PID TTY          TIME CMD
22709 pts/1    00:00:00 bash
25170 pts/1    00:00:00 ps
```

Εαν εκτελέσουμε την `ps` χωρίς παραμέτρους, εμφανίζονται μόνο οι διαλογικές εργασίες (αυτές που σχετίζονται με το τερματικό) του συγκεκριμένου χρήστη.

Εαν προσθέσουμε την παράμετρο `x` (η `ps` δεν απαιτεί την `-` πριν τις παραμέτρους), προκύπτουν και οι υπόλοιπες διεργασίες του χρήστη.

```console
stud@vm2:~$ ps x
  PID TTY      STAT   TIME COMMAND
22677 ?        Ss     0:00 /lib/systemd/systemd --user
22678 ?        S      0:00 (sd-pam)
22708 ?        R      0:00 sshd: stud@pts/1
22709 pts/1    Ss     0:00 -bash
26487 pts/1    R+     0:00 ps x
```

Με την προσθήκη της παραμέτρου `a`, μπορούμε να εμφανίσουμε τις διεργασίες όλων των χρηστών.

```console
stud@vm2:~$ ps ax
  PID TTY      STAT   TIME COMMAND
    1 ?        Ss     0:11 /sbin/init splash
    2 ?        S      0:00 [kthreadd]
    4 ?        I<     0:00 [kworker/0:0H]
    6 ?        I<     0:00 [mm_percpu_wq]
    7 ?        S      0:00 [ksoftirqd/0]
    8 ?        I      1:14 [rcu_sched]
    9 ?        I      0:00 [rcu_bh]
   10 ?        S      0:00 [migration/0]
   11 ?        S      0:01 [watchdog/0]
   12 ?        S      0:00 [cpuhp/0]
   13 ?        S      0:00 [cpuhp/1]
   14 ?        S      0:01 [watchdog/1]
   15 ?        S      0:00 [migration/1]
   16 ?        S      0:00 [ksoftirqd/1]
   18 ?        I<     0:00 [kworker/1:0H]
   19 ?        S      0:00 [cpuhp/2]
   20 ?        S      0:01 [watchdog/2]
   21 ?        S      0:00 [migration/2]
   22 ?        S      0:01 [ksoftirqd/2]
   24 ?        I<     0:00 [kworker/2:0H]
   25 ?        S      0:00 [cpuhp/3]
   26 ?        S      0:01 [watchdog/3]
   27 ?        S      0:00 [migration/3]
   28 ?        S      0:00 [ksoftirqd/3]
   30 ?        I<     0:00 [kworker/3:0H]
   31 ?        S      0:00 [kdevtmpfs]
   32 ?        I<     0:00 [netns]
   33 ?        S      0:00 [rcu_tasks_kthre]
   34 ?        S      0:00 [kauditd]
   36 ?        S      0:00 [khungtaskd]
   37 ?        S      0:00 [oom_reaper]
   38 ?        I<     0:00 [writeback]
   39 ?        S      0:00 [kcompactd0]
   40 ?        SN     0:00 [ksmd]
   41 ?        SN     0:00 [khugepaged]
   42 ?        I<     0:00 [crypto]
   43 ?        I<     0:00 [kintegrityd]
   44 ?        I<     0:00 [kblockd]
   45 ?        I<     0:00 [ata_sff]
   46 ?        I<     0:00 [md]
   47 ?        I<     0:00 [edac-poller]
   48 ?        I<     0:00 [devfreq_wq]
   49 ?        I<     0:00 [watchdogd]
   55 ?        S      0:01 [kswapd0]
   56 ?        I<     0:00 [kworker/u129:0]
   57 ?        S      0:00 [ecryptfs-kthrea]
   99 ?        I<     0:00 [kthrotld]
  100 ?        I<     0:00 [acpi_thermal_pm]
  101 ?        S      0:07 [xenbus]
  102 ?        S      0:00 [xenwatch]
  103 ?        S      0:00 [khvcd]
  104 ?        S      0:00 [scsi_eh_0]
  105 ?        I<     0:00 [scsi_tmf_0]
  106 ?        S      0:00 [scsi_eh_1]
  107 ?        I<     0:00 [scsi_tmf_1]
  113 ?        I<     0:00 [ipv6_addrconf]
  122 ?        I<     0:00 [kstrp]
  139 ?        I<     0:00 [charger_manager]
  189 ?        I<     0:00 [kdmflush]
  191 ?        I<     0:00 [bioset]
  204 ?        I<     0:00 [kworker/0:1H]
  205 ?        I<     0:00 [kworker/3:1H]
  222 ?        S      0:09 [jbd2/dm-0-8]
  223 ?        I<     0:00 [ext4-rsv-conver]
  266 ?        Ss     1:47 /lib/systemd/systemd-journald
  276 ?        I<     0:00 [kworker/1:1H]
  289 ?        Ss     0:00 /sbin/lvmetad -f
  294 ?        Ss     0:00 /lib/systemd/systemd-udevd
  495 ?        I<     0:00 [kdmflush]
  497 ?        I<     0:00 [bioset]
  509 ?        I<     0:00 [ext4-rsv-conver]
  522 ?        I      0:02 [kworker/u128:1]
  575 ?        Ssl    0:00 /lib/systemd/systemd-timesyncd
  722 ?        Ssl   10:55 /usr/lib/accountsservice/accounts-daemon
  724 ?        Ss     0:01 /lib/systemd/systemd-logind
  730 ?        Ss     0:00 /usr/sbin/acpid
  734 ?        Ss     0:00 /usr/sbin/cron -f
  736 ?        Ss     1:05 avahi-daemon: running [vm2.local]
  744 ?        Ssl    0:30 /usr/sbin/rsyslogd -n
  746 ?        Ss     0:14 /usr/bin/dbus-daemon --system --address=systemd: --no
  794 ?        I<     0:02 [kworker/2:1H]
  828 ?        S      0:00 avahi-daemon: chroot helper
  840 ?        Ssl    1:53 /usr/sbin/NetworkManager --no-daemon
  903 ?        Ss     0:42 /usr/sbin/irqbalance --pid=/var/run/irqbalance.pid
 1206 ?        Ssl    0:00 /usr/lib/policykit-1/polkitd --no-debug
 1210 ?        Ss     0:02 /bin/sh /usr/sbin/xe-daemon
 1212 ?        Ssl    0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unatt
 1218 ?        Ss     0:24 /usr/sbin/sshd -D
 1439 ?        Ssl    0:31 /usr/bin/whoopsie -f
 1451 ?        Ss     0:00 /bin/bash /usr/share/xdiagnose/failsafeXServer
 1452 hvc0     Ss+    0:00 /sbin/agetty --keep-baud 115200 38400 9600 hvc0 vt220
 1453 tty1     Ss+    0:00 /sbin/agetty --noclear tty1 linux
 1573 ?        Ss     0:01 /usr/lib/postfix/sbin/master
 1584 ?        S      0:00 qmgr -l -t unix -u
 1590 ?        S      0:00 xinit /usr/share/xdiagnose/failsafeXinit /etc/X11/xor
 1591 tty2     S<sl+   0:02 /usr/lib/xorg/Xorg :0 -br -once -config /etc/X11/xor
 1599 ?        S      0:00 /bin/bash /usr/share/xdiagnose/failsafeXinit /etc/X11
 1606 ?        Sl     0:00 zenity --warning --text <big><b>The system is running
 1615 ?        S      0:00 dbus-launch --autolaunch 5e1f52776b4d4be1aca5defc63a5
 1616 ?        Ss     0:00 /usr/bin/dbus-daemon --fork --print-pid 5 --print-add
 1618 ?        Sl     0:00 /usr/lib/at-spi2-core/at-spi-bus-launcher
 1623 ?        S      0:00 /usr/bin/dbus-daemon --config-file=/etc/at-spi2/acces
 1625 ?        Sl     0:00 /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-s
 1783 ?        S      0:00 tlsmgr -l -t unix -u -c
14479 ?        I      0:00 [kworker/2:1]
20072 ?        I      0:01 [kworker/2:2]
20077 ?        I      0:00 [kworker/1:1]
20079 ?        I      0:00 [kworker/3:1]
20193 ?        S      0:00 pickup -l -t unix -u -c
22060 ?        I      0:00 [kworker/u128:3]
22675 ?        Ss     0:00 sshd: stud [priv]
22677 ?        Ss     0:00 /lib/systemd/systemd --user
22678 ?        S      0:00 (sd-pam)
22708 ?        S      0:00 sshd: stud@pts/1
22709 pts/1    Ss     0:00 -bash
22754 ?        I      0:00 [kworker/1:2]
25626 ?        I      0:00 [kworker/u128:0]
26469 ?        I      0:01 [kworker/0:1]
26472 ?        Ss     0:00 /usr/sbin/cupsd -l
26473 ?        Ssl    0:00 /usr/sbin/cups-browsed
26486 ?        Ss     0:00 sshd: [accepted]
26607 ?        S      0:00 sleep 60
26608 pts/1    R+     0:00 ps ax
28511 ?        I      0:01 [kworker/0:0]
52366 ?        I      0:00 [kworker/3:2]
62166 ?        Ss     0:00 sshd: ics24048 [priv]
62168 ?        Ss     0:00 /lib/systemd/systemd --user
62169 ?        S      0:00 (sd-pam)
62244 ?        S      0:07 sshd: ics24048@pts/0
62245 pts/0    Ss+    0:00 -bash
```

Τέλος, η παράμετρος `u` μορφοποιεί την εμφάνιση των διεργασιών, ώστε να φαίνεται και ο ιδιοκτήτης τους.

```console
stud@vm2:~$ ps u
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
stud     22709  0.0  0.1 138824  5520 pts/1    Ss   16:05   0:00 -bash
stud     26834  0.0  0.1 153424  3328 pts/1    R+   16:33   0:00 ps u
```
