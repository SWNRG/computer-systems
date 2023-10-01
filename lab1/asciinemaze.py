#!/usr/bin/python3

import sys, random, shutil

lospeed = 0.03
hispeed = 0.3
thinkscaler = 3
tabtime = 0.0001
skiplinechar = '§'  # skip delays for whole line, i.e., for command output
skippromptchar = '±'  # skip delays upto $ character, i.e., for linux prompt
clschar = '&' # clear screen character
delaychar = '~' # wait 2 seconds
clsansi = '\\u001b[2J' # clear screen ansi
cursorhomeansi = '\\u001b[H' # move cursor to home ansi
skipprintingchar = False

def escape_ansi(text):
    # This function takes a text with ANSI escape codes and encodes them for storage
    return text.encode('unicode_escape').decode('utf-8')


def main(argv):
    if (len(argv) < 1):
        print("Input file is missing!")
        exit(1)
    else:
        # Create header line
        # Use the width and height as the terminal is now!
        col, row = shutil.get_terminal_size()
        sys.stdout.write('{"timestamp": 1541886839, "width":')
        sys.stdout.write(str(col))
        sys.stdout.write(', "version": 2, "env": {"TERM": "xterm-256color", "SHELL": "/bin/bash"}, "height": ')
        sys.stdout.write(str(row))
        print('}')

        # Read all lines of the file
        t=0
        skipdelays = False     # flag to skip delays for the current line
        promptperiod = False   # keep track the part of text that is a shell prompt
        for line in open(argv[0]):
            prev=' ' # Rem.: For leading tabulation spaces!

            skipprintingchar = False

            # Check if the line starts with the skipline character
            if line.startswith(skiplinechar) or line.startswith(clschar):
                skipdelays = True
                skipprintingchar = True
            elif line.startswith(skippromptchar):
                skipdelays = True
                promptperiod = True
                # printing of skippromptchar is already skipped
            else:
                skipdelays = False
                promptperiod = False

            # If line starts with delay char, set 2 seconds wait time
            if line.startswith(delaychar):
                t=t+2
                skipprintingchar = True

            # And add one line for each character
            for c in line:
                sys.stdout.write('[')
                if ((c == '\t') or (c == ' ') or (c == '\n')):
                    # When char is tab or space it might be a source code!
                    # That means we must skip tabulation spaces and also
                    # we should wait a bit after end of words (thinking time)
                    if ((prev == '\t') or (prev == ' ')): # \n missing here for a cause!
                        if not skipdelays:
                            t = t + tabtime # fast tabulation!
                    else:
                        if not skipdelays:
                            t = t + random.uniform(lospeed*thinkscaler, hispeed*thinkscaler) # thinking time
                else:
                    if not skipdelays:
                        t = t + random.uniform(lospeed, hispeed) # usual writin' time

                sys.stdout.write(str(t))
                sys.stdout.write(', "o", "')
                if (c == '\t'):
                    sys.stdout.write('\\t')
                elif (c == '\n'):
                    # Rem.: Endl is used by the file format this way!!!
                    # skip end of line, in the case of clear or delay chars
                    if (prev != clschar) and (prev != delaychar):
                        sys.stdout.write('\\r\\n')
                elif (c == '"'):
                    sys.stdout.write('\\"')
                elif (c == '\\'):
                    sys.stdout.write('\\\\')
                else:
                    if (c == skippromptchar):
                        # it is the beginning of a prompt, setting color on
                        sys.stdout.write('\\u001b[1;32m')
                    elif (((c == '$') or (c == '#')) and (promptperiod == True)):
                        # it is the end of a prompt, setting color off
                        sys.stdout.write('\\u001b[0m'+c)
                        # we skip delays in the space character that follows
                    elif ((prev == '$') or (prev == '#')) and (c == ' ') and (promptperiod == True):
                        # print space character
                        sys.stdout.write (' ')
                        skipdelays = False
                        promptperiod = False
                    elif (c == clschar):
                        sys.stdout.write (clsansi+cursorhomeansi)
                    elif skipprintingchar:
                        # do not print control characters
                        sys.stdout.write ('')
                        # enable printing characters that follow
                        skipprintingchar = False
                    else:
                        # printable character
                        sys.stdout.write(str(c))
                print('"]')
                prev = c # update prev char

if __name__ == "__main__":
   main(sys.argv[1:])
