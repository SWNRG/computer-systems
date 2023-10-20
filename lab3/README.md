# Εργαστήριο 3 - Απόλυτες και σχετικές διαδρομές καταλόγων στο Linux

## Περιεχόμενα μαθήματος

- [Απόλυτες και σχετικές διαδρομές καταλόγων](#απόλυτες-και-σχετικές-διαδρομές-καταλόγων)

## Απόλυτες και σχετικές διαδρομές καταλόγων
[![asciicast](https://asciinema.org/a/EbyScXzgjqoZNRz92SOQdkWZJ.svg)](https://asciinema.org/a/EbyScXzgjqoZNRz92SOQdkWZJ)

Σε αυτό το μάθημα, θα συζητήσουμε για τις σχετικές και τις απόλυτες διαδρομές των καταλόγων του Linux.

Απόλυτη ονομάζεται μια διαδρομή καταλόγων που ξεκινάει από την ρίζα (root directory).

Η εντολή `pwd` εμφανίζει την απόλυτη διαδρομή του σημείου που βρισκόμαστε.

```console
stud@vm2:~$ pwd
/home/stud
```

Δηλαδή, βρισκόμαστε στον κατάλογο `stud`, o οποίος βρίσκεται μέσα στον κατάλογο `home` ο οποίος με τη σειρά του είναι στην ρίζα των καταλόγων. Η τελευταία συμβολίζεται με τον χαρακτήρα `/`.

Υπενθυμίζουμε άλλους 3 συμβολισμούς καταλόγων:
1) Ο χαρακτήρας `.` αντιπροσωπεύει τον τρέχοντα κατάλογο, δηλαδή η εντολή `cd .` δεν αλλάζει το σημείο που βρισκόμαστε.

```console
stud@vm2:~$ cd .
stud@vm2:~$ # ζητήσαμε να αλλάξουμε κατάλογο και να πάμε εκεί που είμαστε.
```

Ο κατάλογος που βρισκόμαστε ονομάζεται αλλιώς current working directory (cwd) και είναι ο τελευταίος κατάλογος της απόλυτης διαδρομής - στην περίπτωση μας ο `stud`.

Με την είσοδο μας στο σύστημα, το cwd είναι ο προσωπικός μας κατάλογος. Δηλαδή, έχει συνήθως σαν όνομα το όνομα του χρήστη που συνδεθήκαμε.


2) Οι χαρακτήρες `..` συμβολίζουν τον πατρικό κατάλογο του καταλόγου που βρισκόμαστε ή αναφερόμαστε. Δηλαδή, αν δώσουμε `cd ..`.

```console
stud@vm2:~$ cd ..
stud@vm2:/home$ # μετακινούμαστε στον κατάλογο /home (μια θέση πάνω στο δέντρο των καταλόγων).
```

3) Ο χαρακτήρας `~` συμβολίζει τον προσωπικό μας κατάλογο, όπου στην περίπτωση μας είναι ο `/home/stud`. Δηλαδή, οι παρακάτω εντολές είναι ισοδύναμες:

```console
stud@vm2:/home$ cd ~
stud@vm2:~$ pwd
/home/stud
stud@vm2:~$ cd /home/stud
stud@vm2:~$ pwd
/home/stud
```

Μπορούμε επίσης να επιστρέψουμε στον προσωπικό μας κατάλογο δίνοντας `cd` χωρίς κάποιο παραπάνω όρισμα.

```console
stud@vm2:~$ cd
stud@vm2:~$ pwd
/home/stud
```

Ας μετακινηθούμε τώρα στον κατάλογο `myfiles` με τη βοήθεια της εντολής `cd`.

```console
stud@vm2:~$ cd myfiles
stud@vm2:~/myfiles$ pwd
/home/stud/myfiles
```

Παρατηρούμε ότι η απόλυτη διαδρομή του cwd άλλαξε και προστέθηκε ο κατάλογος `myfiles`. Ας δούμε τα περιεχόμενα του `myfiles` με την βοήθεια της `ls`:

```console
stud@vm2:~/myfiles$ ls -l
total 8
drwxrwxr-x 7 stud stud 4096 Oct 16 22:08 personal
drwxrwxr-x 7 stud stud 4096 Oct 17 14:43 studies
```

Ας πάμε στον κατάλογο `studies`:

```console
stud@vm2:~/myfiles$ cd studies
stud@vm2:~/myfiles/studies$ pwd
/home/stud/myfiles/studies
stud@vm2:~/myfiles/studies$ ls -l
total 20
drwxrwxr-x 4 stud stud 4096 Oct  7 15:43 labs
drwxrwxr-x 4 stud stud 4096 Oct  7 15:44 lectures
drwxrwxr-x 2 stud stud 4096 Oct 11 09:22 manuals
drwxrwxr-x 2 stud stud 4096 Oct 17 14:43 music
drwxrwxr-x 2 stud stud 4096 Oct 17 14:42 programs
```

Αν δώσουμε την εντολή `tree`, μπορούμε να δούμε τη δομή των καταλόγων, από τον κατάλογο `studies` και βαθύτερα στο δέντρο.

```console
stud@vm2:~/myfiles/studies$ tree
.
├── labs
│   ├── lab1
│   │   └── lab_report.txt
│   └── lab2
│       └── lab_report.txt
├── lectures
│   ├── lecture1
│   │   └── lecture_notes.txt
│   └── lecture2
│       ├── assignments
│       │   ├── assignment1.txt
│       │   └── assignment2.txt
│       └── lecture_notes.txt
├── manuals
│   ├── man-cat.txt
│   └── man-ls.txt
└── misc
    ├── program1.c
    ├── program2.c
    ├── song1.mp3
    └── song2.mp3

9 directories, 12 files
```

Ας θεωρήσουμε ότι θέλουμε να εμφανίσουμε το αρχείο `lecture_notes.txt` του καταλόγου `lecture2`.

Θα μπορούσαμε να δώσουμε `cd lectures`, `cd lecture2` και `cat lecture_notes.txt`.

Μπορούμε όμως να εμφανίσουμε το αρχείο με μια μόνο εντολή;
 
Οποτεδήποτε αναφερόμαστε σε ένα αρχείο στο linux, μπορούμε να δώσουμε μια διαδρομή πριν το όνομα του, με αποτέλεσμα να το προσπελάσουμε χωρίς να μετακινηθούμε στο σημείο που βρίσκεται.

Για παράδειγμα, μπορούμε να προσθέσουμε στην εντολή `cat` την απόλυτη διαδρομή του αρχείου `lecture_notes.txt`.

```console
stud@vm2:~/myfiles/studies$ cat /home/stud/myfiles/studies/lectures/lecture2/lecture_notes.txt 
No need to take notes.
```

Η διαδρομή αυτή όμως είναι αρκετά μεγάλη.

Ένας εναλλακτικός τρόπος είναι να χρησιμοποιήσουμε ένα άλλο είδος διαδρομής που ονομάζεται σχετική διαδρομή. Η σχετική διαδρομή εκφράζει ένα σημείο της δομής καταλόγων σε σχέση με το σημείο που βρισκόμαστε.

Δηλαδή, μπορούμε να δώσουμε απλώς:

```console
stud@vm2:~/myfiles/studies$ cat lectures/lecture2/lecture_notes.txt 
No need to take notes.
```

Στην ουσία, είναι σαν να αφαιρούμε από την απόλυτη διαδρομή του αρχείου `lecture_notes.txt` την απόλυτη διαδρομή του σημείου που βρισκόμαστε.

Αυτό βέβαια δεν ισχύει πάντα, γιατί μπορεί να χρειαστεί να αναφερθούμε σε διαδρομή που βρίσκεται πάνω από το σημείο που βρισκόμαστε. Εκεί αξιοποιούμε τους χαρακτήρες `..`.

Για παράδειγμα:

```console
stud@vm2:~/myfiles/studies$ cat ../personal/photos/misc/crocodile.txt 
                _ ___                /^^\ /^\  /^^\_
    _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
  _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
 / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
 ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
  _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
 < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
  \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
   `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;
```

Παρατηρούμε ότι οι σχετικές διαδρομές δεν ξεκινάνε από τον χαρακτήρα `/`. Μια εξαίρεση είναι η διαδρομή `~`, η οποία είναι απόλυτη διαδρομή γιατί ακριβώς αντιπροσωπεύει τον κατάλογο `/home/username` (όπου `username` το όνομα του χρήστη), δηλαδή αντιπροσωπεύει διαδρομή που ξεκινάει από τον κατάλογο `/`.

## Δημιουργία, διαγραφή και μετονομασία αρχείων και καταλόγων

Σε αυτό το μάθημα, θα συνδυάσουμε τις σχετικές και τις απόλυτες διαδρομές με εντολές δημιουργίας, διαγραφής και μετονομασίας αρχείων και καταλόγων.

Συγκεκριμένα, θα μελετήσουμε τις παρακάτω εντολές που αφορούν καταλόγους:
1) `mkdir` - δημιουργία καταλόγου,
2) `rmdir` - διαγραφή καταλόγου.

Όπως και τις παρακάτω εντολές που αφορούν κανονικά αρχεία:
1) `cp` - αντιγραφή αρχείων,
2) `mv` - μετακίνηση ή μετονομασία αρχείων,
3) `rm` - διαγραφή αρχείων.

Όλες οι εντολές του Linux που δέχονται σαν όρισμα αρχεία, μπορούν να αναφερθούν σε αυτά τοποθετώντας μια απόλυτη ή σχετική διαδρομή πριν από το όνομα τους. Αυτό έχει σαν αποτέλεσμα να μην χρειάζεται να μετακινηθούμε στον κατάλογο που εμπεριέχει ένα αρχείο, ώστε να αναφερθούμε σε αυτό.

Θα δοκιμάσουμε τις παραπάνω εντολές με ένα παράδειγμα. Μετακινηθείτε στον κατάλογο `personal` ο οποίος βρίσκεται μέσα στον κατάλογο `myfiles`, χρησιμοποιώντας μια απόλυτη διαδρομή και στη συνέχεια εμφανίστε τη δομή καταλόγων με την εντολή `tree`.

```console
stud@vm2:~$ cd myfiles/studies/
stud@vm2:~/myfiles/studies$ tree
.
├── labs
│   ├── lab1
│   │   └── lab_report.txt
│   └── lab2
│       └── lab_report.txt
├── lectures
│   ├── lecture1
│   │   └── lecture_notes.txt
│   └── lecture2
│       ├── assignments
│       │   ├── assignment1.txt
│       │   └── assignment2.txt
│       └── lecture_notes.txt
├── manuals
│   ├── man-cat.txt
│   └── man-ls.txt
└── misc
    ├── program1.c
    ├── program2.c
    ├── song1.mp3
    └── song2.mp3

9 directories, 12 files
```

Παρατηρούμε ότι ο κατάλογος `misc` θα μπορούσε να αναδιοργανωθεί στους καταλόγους `music` και `programs`.

```
├── music
│   ├── song1.mp3
│   └── song2.mp3
└── programs
    ├── program1.c
    └── program2.c

10 directories, 12 files
```

Αρχικά, θα πρέπει να δημιουργήσουμε δύο κενούς καταλόγους, τους `music` και `programs` χρησιμοποιώντας την εντολή `mkdir`.

```console
stud@vm2:~/myfiles/studies$ mkdir music
stud@vm2:~/myfiles/studies$ mkdir programs
```

Σημειώνουμε ότι ή εντολή `mkdir` μπορεί να δεχτεί πολλαπλά ορίσματα αρχείων:

```console
stud@vm2:~/myfiles/studies$ mkdir music programs
```

Στη συνέχεια, θα πρέπει να μεταφέρουμε τα αρχεία `program1.c` και `program2.c` στον κατάλογο `programs`, όπως και τα αρχεία `song1.mp3` και `song2.mp3` στον κατάλογο `music`.

Η μεταφορά των αρχείων μπορεί να γίνει με τις εντολές `cp` και `mv` (αντιγραφή και διαγραφή αρχείου). Η `cp` μπορεί να εκτελεστεί με διαφορετικούς τρόπους - ανάλογα με τη θέση που βρισκόμαστε, αρκεί να οριστούν σωστά οι σχετικές η οι απόλυτες διαδρομές των αρχέιων και τον καταλόγων.

Για παράδειγμα, μπορούμε να εκτελέσουμε την `cp` από τον κατάλογο studies:

```console
stud@vm2:~/myfiles/studies$ cp misc/song1.mp3 music/
stud@vm2:~/myfiles/studies$ cp misc/song2.mp3 music/
stud@vm2:~/myfiles/studies$ cp misc/program1.c programs/
stud@vm2:~/myfiles/studies$ cp misc/program2.c programs/
```

Ένας ισοδύναμος τρόπος είναι:

```console
stud@vm2:~/myfiles/studies$ cp misc/song1.mp3 misc/song2.mp3 music/
stud@vm2:~/myfiles/studies$ cp misc/program1.c misc/program2.c programs/
stud@vm2:~/myfiles/studies$ rm misc/song1.mp3 misc/song2.mp3 misc/program1.c misc/program2.c
```

Τα αρχικά αρχεία και ο κατάλογος misc θα πρέπει να διαγραφούν με τις παρακάτω εντολές:

```console
stud@vm2:~/myfiles/studies$ rm misc/song1.mp3 
stud@vm2:~/myfiles/studies$ rm misc/song2.mp3 
stud@vm2:~/myfiles/studies$ rm misc/program1.c 
stud@vm2:~/myfiles/studies$ rm misc/program2.c
stud@vm2:~/myfiles/studies$ rmdir misc
```

ή εναλλακτικά:

```console
stud@vm2:~/myfiles/studies$ rm misc/song1.mp3 misc/song2.mp3 misc/program1.c misc/program2.c
stud@vm2:~/myfiles/studies$ rmdir misc
```

Στην περίπτωση που χρησιμοποιούσαμε την εντολή `mv`, θα είχαμε ακριβώς την ίδια σύνταξη με την `cp`, αλλά δεν θα χρειαζόταν να διαγράψουμε τα αρχικά αρχεία. Θα διαγράφαμε μόνο τον κατάλογο `misc` στο τέλος.

Ένας άλλος τρόπος είναι να μετακινηθούμε στον κατάλογο `misc` και να μεταφέρουμε τα αρχεία από εκεί:

```console
stud@vm2:~/myfiles/studies$ cd misc
stud@vm2:~/myfiles/studies/misc$ mv program1.c program2.c ../programs
stud@vm2:~/myfiles/studies/misc$ mv song1.mp3 song2.mp3 ../music
stud@vm2:~/myfiles/studies/misc$ cd..
stud@vm2:~/myfiles/studies$ rmdir misc
```

Υπενθυμίζουμε ότι οι χαρακτήρες `..` αντιπροσωπεύουν τον πατρικό κατάλογο.

Τέλος, θα μπορούσαμε να μετακινηθούμε στους καταλόγους `programs` και `misc` και να μεταφέρουμε τα αρχεία από τον κατάλογο `misc` στο σημείο που βρισκόμαστε:

```console
stud@vm2:~/myfiles/studies$ cd program
stud@vm2:~/myfiles/studies/program$ mv ../misc/program1.c ../misc/program2.c .
stud@vm2:~/myfiles/studies/program$ cd ../music
stud@vm2:~/myfiles/studies/music$ mv ../misc/song1.mp3 ../misc/song2.mp3 .
stud@vm2:~/myfiles/studies/music$ cd..
stud@vm2:~/myfiles/studies$ rmdir misc
```

Ο χαρακτήρας `.` συμβολίζει το κατάλογο που βρισκόμαστε.
