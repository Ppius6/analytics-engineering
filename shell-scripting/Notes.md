## Introduction to Shell Scripting
Shell scripting is a powerful way to automate tasks in Unix-like operating systems. A shell script is a text file containing a series of commands that the shell can execute. This guide will cover the basics of creating and running shell scripts.

### Basic Commands
1. `pwd` - Print Working Directory
   - Usage: `pwd`
   - Description: Displays the current directory you are in.
    - Example:
      ```bash
      $ pwd
      /home/user
      ```
2. `ls` - List Directory Contents
    - Usage: `ls [options] [directory]`
    - Description: Lists files and directories in the specified directory. If no directory is specified, it lists the contents of the current directory.
    - Example:
      ```bash
      $ ls -l
      total 8
      drwxr-xr-x 2 user user 4096 Jan 1 12:00 dir1
      -rw-r--r-- 1 user user  123 Jan 1 12:00 file1.txt
      ```
3. `cd` - Change Directory
    - Usage: `cd [directory]`
    - Description: Changes the current directory to the specified directory.
    - Example:
      ```bash
      $ cd dir1
      $ pwd
      /home/user/dir1
      ```
4. `touch` - Create an Empty File
    - Usage: `touch filename`
    - Description: Creates an empty file with the specified name or updates the timestamp of the file if it already exists.
    - Example:
      ```bash
      $ touch newfile.txt
      $ ls
      newfile.txt
      ```
5. `echo` - Display a Line of Text or a variable Value
    - Usage: `echo [text]` or `echo $VARIABLE`
    - Description: Prints the specified text to the terminal.
    - Example:
      ```bash
      $ echo "Hello, World!"
      Hello, World!

      $ MY_VAR="Hello"
        $ echo $MY_VAR
        Hello
      ```
6. `cat` - Concatenate and Display File Content
    - Usage: `cat filename`
    - Description: Displays the content of the specified file.
    - Example:
      ```bash
      $ cat file1.txt
        This is the content of file1.txt
        ```
7. `rm -rf` - Remove Files or Directories
    - Usage: `rm -rf filename_or_directory`
    - Description: Deletes the specified file or directory and its contents recursively without prompting for confirmation.
    - Example:
      ```bash
      $ rm -rf dir1
      $ ls
      newfile.txt
      ```
8. `cp` - Copy Files or Directories
    - Usage: `cp source destination`
    - Description: Copies files or directories from the source to the destination.
    - Example:
      ```bash
      $ cp file1.txt file2.txt
      $ ls
      file1.txt file2.txt newfile.txt
      ```
9. `mv` - Move or Rename Files or Directories
    - Usage: `mv source destination`
    - Description: Moves or renames files or directories from the source to the destination.
    - Example:
      ```bash
      $ mv file2.txt renamed_file.txt
      $ ls
      file1.txt renamed_file.txt newfile.txt
      ```
10. `rm` - Remove Files
    - Usage: `rm filename`
    - Description: Deletes the specified file.
    - Example:
      ```bash
      $ rm renamed_file.txt
      $ ls
      file1.txt newfile.txt
      ```
11. `mkdir` - Create a New Directory
    - Usage: `mkdir directory_name`
    - Description: Creates a new directory with the specified name.
    - Example:
      ```bash
      $ mkdir new_directory
      $ ls
      file1.txt newfile.txt new_directory
      ```
12. `rmdir` - Remove an Empty Directory
    - Usage: `rmdir directory_name`
    - Description: Deletes the specified empty directory.
    - Example:
      ```bash
      $ rmdir new_directory
      $ ls
      file1.txt newfile.txt
      ```
13. `less` - View File Content One Page at a Time
    - Usage: `less filename`
    - Description: Opens the specified file in a viewer that allows scrolling through the content one page at a time.
    - Example:
      ```bash
      $ less file1.txt
      ```
14. `head` - View the Beginning of a File
    - Usage: `head filename`
    - Description: Displays the first 10 lines of the specified file by default. You can specify the number of lines with the `-n` option.
    - Example:
      ```bash
      $ head -n 5 file1.txt
      ```
15. `tail` - View the End of a File
    - Usage: `tail filename`
    - Description: Displays the last 10 lines of the specified file by default. You can specify the number of lines with the `-n` option.
    - Example:
        ```bash
        $ tail -n 5 file1.txt
        ```
16. `q` - Quit
    - Usage: `q`
    - Description: Exits the current program or command, such as `less`.
    - Example:
      ```bash
      $ less file1.txt
      (Press 'q' to exit)
      ```
17. `ls -R` - List Directory Contents Recursively
    - Usage: `ls -R [directory]`
    - Description: Lists files and directories in the specified directory and all its subdirectories recursively.
    - Example:
      ```bash
      $ ls -R
      .:
      file1.txt  newfile.txt  dir1/

      ./dir1:
      file2.txt
      ```
18. `man [command]` - Manual Pages
    - Usage: `man command`
    - Description: Displays the manual pages for the specified command, providing detailed information about its usage and options.
    - Example:
      ```bash
      $ man ls
      - Displays the manual for the 'ls' command
      ```
19. `cut` - Select columns from a file
    - Usage: `cut -f column_number_a, column_number_b -d, filename`
    - Description: Extracts specific columns from a file based on the delimiter provided.
    - Example:
        ```bash
        $ cut -f 1,3 -d, file.csv
        ```
20. `grep` - Search for a pattern in a file
    - Usage: `grep "pattern" filename`
    - Description: Searches for the specified pattern in the given file and displays the matching lines.
    - Example:
        ```bash
        $ grep "error" logfile.txt
        ```
21. `>` - Redirect Output to a File
    - Usage: `command > filename`
    - Description: Redirects the output of the specified command to a file, overwriting the file if it already exists.
    - Example:
      ```bash
      $ echo "Hello, World!" > hello.txt
      $ cat hello.txt
      Hello, World!
      ```
22. `>>` - Append Output to a File
    - Usage: `command >> filename`
    - Description: Appends the output of the specified command to a file, creating the file if it does not exist.
    - Example:
      ```bash
      $ echo "This is a new line." >> hello.txt
      $ cat hello.txt
      Hello, World!
      This is a new line.
      ```
23. `pipe (|)` - Pass Output to Another Command
    - Usage: `command1 | command2`
    - Description: Takes the output of `command1` and uses it as the input for `command2`.
    - Example:
      ```bash
      $ ls -l | grep "txt"
      -rw-r--r-- 1 user user  123 Jan 1 12:00 file1.txt
      -rw-r--r-- 1 user user   45 Jan 1 12:05 newfile.txt
      ``` 
24. `chmod` - Change File Permissions
    - Usage: `chmod permissions filename`
    - Description: Changes the permissions of the specified file or directory. Permissions can be specified using symbolic (e.g., `u+x`) or numeric (e.g., `755`) notation.
    - Example:
      ```bash
      $ chmod u+x script.sh
      $ ls -l script.sh
      -rwxr--r-- 1 user user  123 Jan 1 12:00 script.sh
      ```
25. `wc` - Word Count
    - Usage: `wc filename`
    - Description: Counts the number of lines, words, and characters in the specified file. You can use options like `-l` for lines, `-w` for words, and `-c` for characters.
    - Example:
      ```bash
      $ wc -l file1.txt
      10 file1.txt
      ```
26. `?` - Match a Single Character
    - Usage: `ls file?.txt`
    - Description: Matches any single character in the specified position. For example, `file?.txt` matches `file1.txt`, `fileA.txt`, etc.
    - Example:
      ```bash
      $ ls file?.txt
      file1.txt  fileA.txt
      ```
27. `*` - Match Zero or More Characters
    - Usage: `ls *.txt`
    - Description: Matches zero or more characters in the specified position. For example, `*.txt` matches `file.txt`, `document.txt`, `notes.txt`, etc.
    - Example:
      ```bash
      $ ls *.txt
      file1.txt  newfile.txt  notes.txt
      ```
28. `[]` - Match Any One of the Characters Inside the Brackets
    - Usage: `ls file[12].txt`
    - Description: Matches any one of the characters inside the brackets. For example, `file[12].txt` matches `file1.txt` and `file2.txt`.
    - Example
        ```bash
        $ ls file[12].txt
        file1.txt  file2.txt
        ```
29. {...} - Match Any of the Comma-Separated Strings Inside the Braces
    - Usage: `ls file{1,2}.txt`
    - Description: Matches any of the comma-separated strings inside the braces. For example, `file{1,2}.txt` matches `file1.txt` and `file2.txt`.
    - Example:
      ```bash
      $ ls file{1,2}.txt
      file1.txt  file2.txt
      ```
30. `sort` - Sort Lines of Text Files
    - Usage: `sort filename`
    - Description: Sorts the lines of the specified file in alphabetical order. You can use options like `-r` for reverse order and `-n` for numerical sort.
    - Example:
      ```bash
      $ sort file1.txt
      apple
      banana
      cherry
      ```
31. `uniq` - Remove Duplicate Lines
    - Usage: `uniq filename`
    - Description: Removes duplicate lines from the specified file. It is often used in combination with `sort`.
    - Example:
      ```bash
      $ sort file1.txt | uniq
      apple
      banana
      cherry
      ```   
32. `bash` - Execute a Shell Script
    - Usage: `bash script.sh`
    - Description: Executes the specified shell script using the Bash shell.
    - Example:
      ```bash
      $ bash script.sh
      ```
33. `sh` - Execute a Shell Script
    - Usage: `sh script.sh`
    - Description: Executes the specified shell script using the default shell (usually sh).
    - Example:
      ```bash
      $ sh script.sh
      ```
      
### Editing files in UNIX
1. `nano` - Simple Text Editor
    - Usage: `nano filename`
    - Description: Opens the specified file in the nano text editor, which is user-friendly and easy to use for beginners.
    - Example:
      ```bash
      $ nano file1.txt
      ```
When working in `nano`, you can use the following commands:
- `CTRL + O` - Save the file (Write Out)
- `CTRL + X` - Exit nano
- `CTRL + K` - Cut a line
- `CTRL + U` - Paste a line

For example, to edit a file named `names.txt`, you would use:
```bash
$ nano names.txt
```
then enter the names, and save the file with `CTRL + O` followed by `ENTER`, and exit with `CTRL + X`.

