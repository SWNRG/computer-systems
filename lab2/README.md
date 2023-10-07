# Εργαστήριο 2 - Εισαγωγή στη δομή καταλόγων του Linux

## Περιεχόμενα μαθήματος

- [Περιήγηση στο σύστημα](#περιήγηση-στο-σύστημα)

## Περιήγηση στο σύστημα
[![asciicast](https://asciinema.org/a/l5SdmkMPuphjeEv6xoMHBPtT7.svg)](https://asciinema.org/a/l5SdmkMPuphjeEv6xoMHBPtT7)

Καλωσήρθατε στη δεύτερη διάλεξη του μαθήματος των Συστημάτων Υπολογιστών!

Στη συνέχεια, θα συζητήσουμε τις βασικές εντολές του Linux για την περιήγηση στο σύστημα.

Όπως είδαμε στην πρώτη διάλεξη, η προτροπή της γραμμής εντολών δείχνει το σημείο που βρισκόμαστε στον σκληρό δίσκο:

```console
stud@vm2:~$
```

Δηλαδή, βρίσκομαστε στον κατάλογο ~. Το συγκεκριμένο σύμβολο αναπαριστά τον προσωπικό μας κατάλογο.

Οι κατάλογοι του σκληρού δίσκου είναι οργανωμένοι σε δενδροειδή μορφή. Για να εμφανίσουμε το σημείο που βρισκόμαστε μέσα σε αυτό το "δέντρο" του σκληρού δίσκου, δίνουμε την εντολή pwd:

```console
stud@vm2:~$ pwd
/home/stud
```

Δηλαδή, στην περίπτωση μας το σύμβολο ~ αναπαριστά τον κατάλογο /home/stud. Αυτό είναι το σημείο που μπορούμε να τοποθετήσουμε τα προσωπικά μας αρχεία. 

Ας εκτελέσουμε τώρα την εντολή ls για να δούμε τα αρχεία μας:

```console
stud@vm2:~$ ls
file1  file2  file3  myfiles
```

Τo αρχείo myfiles είναι κατάλογος, ενώ τα αρχεία file1, file2 και file3 κανονικά άρχεια. Οι κατάλογοι είναι σαν τους κίτρινους φακέλους στο γραφικό περιβάλλον των Windows. Σε κάποια συστήματα, τα αρχεία χρωματίζονται διαφορετικά από τους καταλόγους.

Για να καταλάβουμε τον τύπο των αρχείων, μπορούμε να δώσουμε την εντολή ls -l (αναλυτική εμφάνιση των αρχείων).

```console
stud@vm2:~$ ls -l
total 20
-rw-r--r-- 1 ics24100 students24   74 Oct  3 10:40 file1
-rw-r--r-- 1 ics24100 students24   74 Oct  3 10:40 file2
-rw-r--r-- 1 ics24100 students24   74 Oct  3 10:40 file3
drwxrwxr-x 2 ics24100 students24 4096 Oct  7 16:36 myfiles
```

Οι κατάλογοι διακρίνονται από τα αρχεία από τον πρώτο χαρακτήρα που εμφανίζει η ls -l. Αν είναι d, το αρχείο είναι κατάλογος, αν είναι -, αποτελεί κανονικό αρχείο (κείμενο, φωτογραφία, κτλ). 

Στο σημείο αυτό, μπορούμε να δώσουμε την εντολή cd (change directory) με την οποία μπορούμε να αλλάξουμε τον κατάλογο που βρισκόμαστε και να μετακινηθούμε σε κάποιον άλλον κατάλογο. Ας μπούμε μέσα στον κατάλογο myfiles:

```console
stud@vm2:~$ cd myfiles
```

Μπορούμε να ξαναδώσουμε την εντολή pwd, ώστε να επαληθεύσουμε το σημείο που βρισκόμαστε στον σκληρό δίσκο:

```console
stud@vm2:~/myfiles$ pwd
/home/stud/myfiles
```

Δηλαδή, η αρχή του σκληρού δίσκου συμβολίζεται με τον χαρακτήρα /. Σε εκείνο το σημείο υπάρχει ο κατάλογος home που περιλαμβάνει τους προσωπικούς καταλόγους όλων των χρηστών. Μέσα στον home βρίσκεται ο κατάλογος stud (του τρέχοντα χρήστη), ο οποίος εμπεριέχει τον κατάλογο myfiles.

Μια τέτοια πλήρη διαδρομή που ξεκινάει από την αρχή του σκληρού δίσκου (την ρίζα / ή αλλιώς root directory), λέγεται απόλυτη διαδρομή.

Ας δούμε τώρα τα περιεχόμενα του καταλόγου myfiles, με τη βοήθεια της ls:

```console
stud@vm2:~/myfiles$ ls -l
total 8
drwxrwxr-x 7 stud stud 4096 Oct  7 15:44 personal
drwxrwxr-x 5 stud stud 4096 Oct  7 15:44 studies
```

Παρατηρούμε ότι εμπεριέχει δύο καταλόγους, τους personal και studies.

Ας μετακινηθούμε στον κατάλογο personal:

```console
stud@vm2:~/myfiles$ cd personal
```

Εμφανίζουμε τα αρχεία του καταλόγου personal:

```console
stud@vm2:~/myfiles/personal$ ls -l
total 20
drwxrwxr-x 2 stud stud 4096 Oct  7 14:02 books
drwxrwxr-x 2 stud stud 4096 Oct  7 15:48 finance
drwxrwxr-x 3 stud stud 4096 Oct  7 15:50 health
drwxrwxr-x 6 stud stud 4096 Oct  7 15:48 mails
drwxrwxr-x 4 stud stud 4096 Oct  7 15:52 photos
```

Παρατηρούμε ότι ο κατάλογος personal εμπεριέχει τους καταλόγους books, finance, health, mails και photos.

Δηλαδή, μέχρι τώρα έχουμε ανακαλύψει την παρακάτω δομή του καταλόγου myfiles:

```
 ├── personal
 │   ├── books
 │   ├── finance
 │   ├── health
 │   ├── mails
 |── studies
```

Μπορούμε να συνεχίσουμε να ανακαλύπτουμε το σύστημα, πηγαίνοντας στον κατάλογο books και εμφανίζοντας τα αρχεία που περιέχει.

```console
stud@vm2:~/myfiles/personal$ cd books
stud@vm2:~/myfiles/personal/books$ ls -l
total 20
-rw-rw-r-- 1 stud stud 4873 Oct  7 13:59 93-Victor_Hugo.txt
-rw-rw-r-- 1 stud stud  776 Oct  7 13:47 Crime_and_Punishment-Fyodor_Dostoevsky.txt
-rw-rw-r-- 1 stud stud 4425 Oct  7 14:02 The_Grapes_of_Wrath-John_Steinbeck.txt
```

Δηλαδή, ο κατάλογος books περιλαμβάνει τρια αρχεία κειμένου. Eμφανίζουμε ένα από αυτά με τη βοήθεια της εντολής cat:

```console
stud@vm2:~/myfiles/personal/books$ cat Crime_and_Punishment-Fyodor_Dostoevsky.txt 
Crime and Punishment follows the mental anguish and moral dilemmas of Rodion Raskolnikov, an impoverished ex-student in Saint Petersburg who plans to kill an unscrupulous pawnbroker, an old woman who stores money and valuable objects in her flat. He theorises that with the money he could liberate himself from poverty and go on to perform great deeds, and seeks to convince himself that certain crimes are justifiable if they are committed in order to remove obstacles to the higher goals of 'extraordinary' men. Once the deed is done, however, he finds himself wracked with confusion, paranoia, and disgust. His theoretical justifications lose all their power as he struggles with guilt and horror and is confronted with both internal and external consequences of his deed.
```

Εδώ όμως δεν υπάρχει άλλος υποκατάλογος να ανακαλύψουμε, για να γυρίσουμε στον πατρικό κατάλογο (τον personal, στην περίπτωση μας), δίνουμε την εντολή cd ..

```console
stud@vm2:~/myfiles/personal/books$ cd ..
```

Μπορούμε να εμφανίσουμε τα περιεχόμενα του καταλόγου personal, δίνοντας την εντολή ls -al. Η παράμετρος a ενεργοποιεί στην ls τη δυνατήτα εμφάνισης κρυφών αρχείων. Τα κρυφά αρχεία στο Unix/Linux ξεκινάνε από τον χαρακτήρα .

```console
stud@vm2:~/myfiles/personal$ ls -al
total 28
drwxrwxr-x 7 stud stud 4096 Oct  7 15:44 .
drwxrwxr-x 4 stud stud 4096 Oct  7 15:43 ..
drwxrwxr-x 2 stud stud 4096 Oct  7 14:02 books
drwxrwxr-x 2 stud stud 4096 Oct  7 15:48 finance
drwxrwxr-x 3 stud stud 4096 Oct  7 15:50 health
drwxrwxr-x 6 stud stud 4096 Oct  7 15:48 mails
drwxrwxr-x 4 stud stud 4096 Oct  7 15:52 photos
```

Δηλαδή ο κατάλογος personal εμπεριέχει δύο κρυφά αρχεία, τα . και ..

Στην πραγματικότητα, τα αρχεία αυτά υπάρχουν σε όλους τους καταλόγους. Το αρχείο .. συνδέει τον κατάλογο με τον πατρικό του κατάλογο, και αυτός είναι ο λόγος που η εντολή cd .. μας μετακινεί έναν κατάλογο πάνω, στο δέντρο καταλόγων του σκληρού δίσκου. 

Ο κατάλογος . συμβολίζει τον τρέχοντα κατάλογο, με αποτέλεσμα η εντολή cd . να μην αλλάζει το σημείο που βρισκόμαστε. Χρησιμοποιούμε τον κατάλογο . όποτε θέλουμε να αναφερθούμε στον τρέχοντα κατάλογο.

Ένας χρήστης μπορεί να δώσει την εντολή cd ~ ή cd χωρίς κανένα όρισμα, για να μετακινηθεί στον προσωπικό του κατάλογο:

```console
stud@vm2:~/myfiles/personal$ cd ~
stud@vm2:~$
```
