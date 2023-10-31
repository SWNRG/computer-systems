# Εργαστήριο 5 - Εμφάνιση και αναζήτηση του περιεχομένου αρχείων

## Περιεχόμενα μαθήματος

- [Εμφάνιση του περιεχομένου αρχείων](#εμφάνιση-του-περιεχομένου-αρχείων)
- [Αναζήτηση του περιεχομένου αρχείων](#αναζήτηση-του-περιεχομένου-αρχείων)

## Εμφάνιση του περιεχομένου αρχείων
[![asciicast](https://asciinema.org/a/r20WQPJXJzKVVtRfCIGu2WzsY.svg)](https://asciinema.org/a/r20WQPJXJzKVVtRfCIGu2WzsY)

Σε αυτό το μάθημα, θα συζητήσουμε εντολές που μας βοηθούν να διαβάσουμε και να εμφανίσουμε το περιεχόμενο αρχείων. Παραδείγματα τέτοιων εντολών είναι:
1. *cat*: Η εντολή `cat` εμφανίζει το περιεχόμενο ενός αρχείου στo τερματικό.
2. *head & tail*: Οι εντολές `head` και `tail` εμφανίζουν τις πρώτες ή τις τελευταίες γραμμές ενός αρχείου, αντίστοιχα. Είναι χρήσιμες για να δούμε το περιεχόμενο μεγάλων αρχείων.
3. *less & more*: Η εντολή `less` προβάλλει το περιεχόμενο ενός αρχείου σε μια περισσότερο διαδραστική μορφή. Ο χρήστης μπορεί να κυκλοφορήσει μέσα στο περιεχόμενο χρησιμοποιώντας τα βασικά πλήκτρα (π.χ. βελάκια). Η εντολή `more` είναι παρόμοια με τη `less` και εμφανίζει το περιεχόμενο ενός αρχείου σε σελίδες. Επίσης διαθέτει βασικές λειτουργίες για την περιήγηση (π.χ. `SPACE` για επόμενη σελίδα, `q` για έξοδο).

Ας δούμε κάποια παραδείγματα. Ξεκινάμε τοποθετώντας τις οδηγίες της εντολής `ls` σε ένα αρχείο και εμφανίζοντας το περιεχόμενο του με την `cat`:

```console
stud@vm2:~$ man ls > ls-info
stud@vm2:~$ cat ls-info
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.

       -a, --all
              do not ignore entries starting with .

       -A, --almost-all
              do not list implied . and ..

       --author
              with -l, print the author of each file

       -b, --escape
              print C-style escapes for nongraphic characters

       --block-size=SIZE
              with  -l,  scale  sizes  by  SIZE  when  printing  them;   e.g.,
              '--block-size=M'; see SIZE format below

       -B, --ignore-backups
              do not list implied entries ending with ~

       -c     with -lt: sort by, and show, ctime (time of last modification of
              file status information); with -l: show ctime and sort by  name;
              otherwise: sort by ctime, newest first

       -C     list entries by columns

       --color[=WHEN]
              colorize  the output; WHEN can be 'always' (default if omitted),
              'auto', or 'never'; more info below

       -d, --directory
              list directories themselves, not their contents

       -D, --dired
              generate output designed for Emacs' dired mode

       -f     do not sort, enable -aU, disable -ls --color

       -F, --classify
              append indicator (one of */=>@|) to entries

       --file-type
              likewise, except do not append '*'

       --format=WORD
              across -x, commas -m, horizontal -x, long -l, single-column  -1,
              verbose -l, vertical -C

       --full-time
              like -l --time-style=full-iso

       -g     like -l, but do not list owner

       --group-directories-first
              group directories before files;

              can   be  augmented  with  a  --sort  option,  but  any  use  of
              --sort=none (-U) disables grouping

       -G, --no-group
              in a long listing, don't print group names

       -h, --human-readable
              with -l and -s, print sizes like 1K 234M 2G etc.

       --si   likewise, but use powers of 1000 not 1024

       -H, --dereference-command-line
              follow symbolic links listed on the command line

       --dereference-command-line-symlink-to-dir
              follow each command line symbolic link

              that points to a directory

       --hide=PATTERN
              do not list implied entries matching shell  PATTERN  (overridden
              by -a or -A)

       --hyperlink[=WHEN]
              hyperlink file names; WHEN can be 'always' (default if omitted),
              'auto', or 'never'

       --indicator-style=WORD
              append indicator with style WORD to entry names: none (default),
              slash (-p), file-type (--file-type), classify (-F)

       -i, --inode
              print the index number of each file

       -I, --ignore=PATTERN
              do not list implied entries matching shell PATTERN

       -k, --kibibytes
              default  to  1024-byte  blocks for disk usage; used only with -s
              and per directory totals

       -l     use a long listing format

       -L, --dereference
              when showing file information for a symbolic link, show informa‐
              tion  for  the file the link references rather than for the link
              itself

       -m     fill width with a comma separated list of entries

       -n, --numeric-uid-gid
              like -l, but list numeric user and group IDs

       -N, --literal
              print entry names without quoting

       -o     like -l, but do not list group information

       -p, --indicator-style=slash
              append / indicator to directories

       -q, --hide-control-chars
              print ? instead of nongraphic characters

       --show-control-chars
              show nongraphic characters as-is (the default, unless program is
              'ls' and output is a terminal)

       -Q, --quote-name
              enclose entry names in double quotes

       --quoting-style=WORD
              use  quoting style WORD for entry names: literal, locale, shell,
              shell-always,  shell-escape,  shell-escape-always,   c,   escape
              (overrides QUOTING_STYLE environment variable)

       -r, --reverse
              reverse order while sorting

       -R, --recursive
              list subdirectories recursively

       -s, --size
              print the allocated size of each file, in blocks

       -S     sort by file size, largest first

       --sort=WORD
              sort  by  WORD instead of name: none (-U), size (-S), time (-t),
              version (-v), extension (-X)

       --time=WORD
              change the default of  using  modification  times;  access  time
              (-u): atime, access, use; change time (-c): ctime, status; birth
              time: birth, creation;

              with -l, WORD determines which time to show;  with  --sort=time,
              sort by WORD (newest first)

       --time-style=TIME_STYLE
              time/date format with -l; see TIME_STYLE below

       -t     sort by time, newest first; see --time

       -T, --tabsize=COLS
              assume tab stops at each COLS instead of 8

       -u     with  -lt:  sort by, and show, access time; with -l: show access
              time and sort by name; otherwise: sort by  access  time,  newest
              first

       -U     do not sort; list entries in directory order

       -v     natural sort of (version) numbers within text

       -w, --width=COLS
              set output width to COLS.  0 means no limit

       -x     list entries by lines instead of by columns

       -X     sort alphabetically by entry extension

       -Z, --context
              print any security context of each file

       -1     list one file per line.  Avoid '\n' with -q or -b

       --help display this help and exit

       --version
              output version information and exit

       The  SIZE  argument  is  an  integer and optional unit (example: 10K is
       10*1024).  Units are K,M,G,T,P,E,Z,Y  (powers  of  1024)  or  KB,MB,...
       (powers  of 1000).  Binary prefixes can be used, too: KiB=K, MiB=M, and
       so on.

       The TIME_STYLE argument can be  full-iso,  long-iso,  iso,  locale,  or
       +FORMAT.   FORMAT  is  interpreted  like in date(1).  If FORMAT is FOR‐
       MAT1<newline>FORMAT2, then FORMAT1 applies to non-recent files and FOR‐
       MAT2  to  recent files.  TIME_STYLE prefixed with 'posix-' takes effect
       only outside the POSIX locale.  Also the TIME_STYLE  environment  vari‐
       able sets the default style to use.

       Using  color  to distinguish file types is disabled both by default and
       with --color=never.  With --color=auto, ls emits color codes only  when
       standard  output is connected to a terminal.  The LS_COLORS environment
       variable can change the settings.  Use the dircolors command to set it.

   Exit status:
       0      if OK,

       1      if minor problems (e.g., cannot access subdirectory),

       2      if serious trouble (e.g., cannot access command-line argument).

AUTHOR
       Written by Richard M. Stallman and David MacKenzie.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report any translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2020 Free Software Foundation, Inc.   License  GPLv3+:  GNU
       GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This  is  free  software:  you  are free to change and redistribute it.
       There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation <https://www.gnu.org/software/coreutils/ls>
       or available locally via: info '(coreutils) ls invocation'

GNU coreutils 8.32               February 2022                           LS(1)
```

Παρατηρούμε ότι το αρχείο είναι πολύ μεγάλο και δυσκολευόμαστε να το διαβάσουμε ή να εντοπίσουμε κάποια πληροφορία σε αυτό.

Στη συνέχεια, εμφανίστε το περιεχόμενο του αρχείου `ls-info` με τη βοήθεια της εντολής `less`:

```console
stud@vm2:~$ less ls-info
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.

       -a, --all
              do not ignore entries starting with .

       -A, --almost-all
              do not list implied . and ..

       --author
ls-info
```

Εμφανίζεται η πρώτη σελίδα του κειμένου. Μπορείτε να χρησιμοποιήσετε βασικά πλήκτρα όπως τα βελάκια και το πλήκτρο `SPACE` για περιήγηση. Πατήστε το πλήκτρο `q` για να τερματίσετε την `less`.

Αντίστοιχα, μπορείτε να δοκιμάσετε το περιβάλλον της εντολής `more`. Η `more` αποτελεί μια απλοποιημένη εκδοχή της `less` και συνήθως χρησιμοποιείται για να βλέπουμε κάποιο μεγάλο κείμενο σελίδα-σελίδα.

```console
stud@vm2:~$ more ls-info
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.

       -a, --all
              do not ignore entries starting with .

       -A, --almost-all
              do not list implied . and ..

       --author
--More--(7%)
```

Η `more` εμφανίζει το ποσοστό του αρχείου που έχει εμφανιστεί στην οθόνη. Χρησιμοποιήστε το πλήκτρο `SPACE` για να δείτε την επόμενη σελίδα και το πλήκτρο `q` για έξοδο.

Στη συνέχεια, εμφανίζουμε τις πρώτες 10 γραμμές του αρχείου με την εντολή `head`:

```console
stud@vm2:~$ head ls-info
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
```

Η παράμετρος `n` μας επιτρέπει να ορίσουμε τον αριθμό των γραμμών του αρχείου που θέλουμε να εμφανίσουμε.

```console
stud@vm2:~$ head -n 5 ls-info
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

```
Δηλαδή, εμφανίσαμε τις πρώτες 5 γραμμές του αρχείου.

Η εντολή `tail` είναι παρόμοια με την εντολή `head`, αλλά εμφανίζει τις τελευταίες γραμμές του αρχείου, αντί τις πρώτες:

```console
stud@vm2:~$ tail -n 5 ls-info
SEE ALSO
       Full documentation <https://www.gnu.org/software/coreutils/ls>
       or available locally via: info '(coreutils) ls invocation'

GNU coreutils 8.32               February 2022                           LS(1)
```
Η παράμετρος `n` λειτουργεί με τον ίδιο τρόπο με την `head`. Αν δεν οριστεί, τότε θεωρείται ο αριθμός 10. 

Δηλαδή, μπορούμε να δούμε το περιεχόμενο ενός αρχείου με διαφορετικούς τρόπους, ανάλογα με τις ανάγκες μας.

## Αναζήτηση του περιεχομένου αρχείων

[![asciicast](https://asciinema.org/a/YAO5k8H8GBiTFNIdG0oIb6izV.svg)](https://asciinema.org/a/YAO5k8H8GBiTFNIdG0oIb6izV)

Για την αναζήτηση του περιεχομένου αρχείων μπορούμε να χρησιμοποιήσουμε τις εντολές `more` ή `less`. Όταν βρισκόμαστε στο περιβάλλον των εντολών αυτών, μπορούμε να πατήσουμε `\keyword`, όπου `keyword` η λέξη που θέλουμε να αναζητήσουμε. Στη συνέχεια, θα μετακινηθεί το κείμενο στα ανάλογα σημεία και θα μαρκαριστεί η λέξη που αναζητούμε. Πατώντας το πλήκτρο `\` όσες φορές επιθυμούμε, επαναλαμβάνουμε την πιο πρόσφατη αναζήτηση μας.

Μια ακόμη χρήσιμη εντολή είναι η `grep`, η οποία επιτρέπει να πραγματοποιούμε αναζητήσεις στο περιεχόμενο αρχείων με τη βοήθεια της γραμμής εντολών.

Για παράδειγμα, η παρακάτω εντολή επιστρέφει όλες τις γραμμές στο αρχέιο `ls-manual` που περιέχουν τη λέξη `list`:

```console
stud@vm2:~$ grep list ls-manual
       ls - list directory contents
              do not list implied . and ..
              do not list implied entries ending with ~
       -C     list entries by columns
              list directories themselves, not their contents
       -g     like -l, but do not list owner
              in a long listing, don't print group names
              follow symbolic links listed on the command line
              do not list implied entries matching shell  PATTERN  (overridden
              do not list implied entries matching shell PATTERN
       -l     use a long listing format
       -m     fill width with a comma separated list of entries
              like -l, but list numeric user and group IDs
       -o     like -l, but do not list group information
              list subdirectories recursively
       -U     do not sort; list entries in directory order
       -x     list entries by lines instead of by columns
       -1     list one file per line.  Avoid '\n' with -q or -b
```

Μπορούμε να περικλείουμε τη λέξη αναζήτησης σε εισαγωγικά ή όχι.

Υπάρχει η δυνατότητα να πραγματοποιούμε περισσότερο πολύπλοκες αναζητήσεις με τη χρήση ειδικών εκφράσεων που ονομάζονται regular expressions. Π.χ. το σύμβολο `^` οδηγεί στην αναζήτηση γραμμών που ξεκινούν από τη λέξη που ακολουθεί το σύμβολο. Για παράδειγμα:

```console
stud@vm2:~$ grep "^GNU" ls-info
GNU coreutils 8.32               February 2022                           LS(1)
```

Αυτή η εντολή θα επιστρέψει όλες τις γραμμές του αρχείου `ls-info` που ξεκινούν με "GNU".

Μπορούμε ακόμα να αντιστρέψουμε το αποτέλεσμα της αναζήτησης με την αξοποιήση της παραμέτρου `v`.

```console
stud@vm2:~$ grep -v "a" ls-info 

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       fied.

       too.





       --block-size=SIZE

              do not list implied entries ending with ~

              otherwise: sort by ctime, newest first

       -C     list entries by columns

       --color[=WHEN]

       -d, --directory
              list directories themselves, not their contents

       -D, --dired



       --file-type


       --full-time
              like -l --time-style=full-iso

       -g     like -l, but do not list owner

       --group-directories-first
              group directories before files;


       -G, --no-group


       --si   likewise, but use powers of 1000 not 1024




       --hide=PATTERN

       --hyperlink[=WHEN]


       -i, --inode

       -I, --ignore=PATTERN

       -k, --kibibytes


       -L, --dereference
              itself


       -n, --numeric-uid-gid







       --quoting-style=WORD

       -r, --reverse
              reverse order while sorting

       -R, --recursive
              list subdirectories recursively

       -s, --size


       --sort=WORD
              version (-v), extension (-X)

       --time=WORD

              with -l, WORD determines which time to show;  with  --sort=time,
              sort by WORD (newest first)

       --time-style=TIME_STYLE

       -t     sort by time, newest first; see --time


              first

       -U     do not sort; list entries in directory order


       -w, --width=COLS



       -Z, --context

       -1     list one file per line.  Avoid '\n' with -q or -b


       --version

       so on.



       0      if OK,



AUTHOR

REPORTING BUGS

COPYRIGHT

SEE ALSO

```

Δηλαδή, εμφανίστηκαν όλες οι γραμμές του αρχείου `ls-info` που ΔΕΝ περιέχουν το γράμμα `a`. Υπενθυμίζουμε ότι το linux διαχωρίζει τα κεφαλαία από τα μικρά γράμματα. Δηλαδή, η εντολή επιστρέφει τις γραμμές που περιέχουν το κεφαλαίο γράμμα `A`.

Μπορούμε να αναζητήσουμε μια λέξη και να αναφερθεί και ο αριθμός σειρών που εντοπίστηκαν:

```console
stud@vm2:~$ grep -n "directory" ls-info
4:       ls - list directory contents
10:       List  information  about  the FILEs (the current directory by default).
46:       -d, --directory
89:              that points to a directory
111:              and per directory totals
183:       -U     do not sort; list entries in directory order
224:       1      if minor problems (e.g., cannot access subdirectory),
```

Αυτή η εντολή επιστρέφει όλες τις γραμμές που περιέχουν τη λέξη `directory`, εμφανίζοντας τον αριθμό κάθε γραμμής μαζί με το περιεχόμενο της.

Τα παραπάνω είναι μερικά παραδείγματα χρήσης της εντολής `grep` με βασικές παραμέτρους. Η εντολή `grep` είναι ένα πολύ ισχυρό εργαλείο για αναζήτηση κειμένου σε αρχεία.
