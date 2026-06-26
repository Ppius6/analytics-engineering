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
      $ head folder/file.txt
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

      $ sort -r file1.txt
      cherry
      banana
      apple

      $ sort -n numbers.txt
      1
      2
      10
      
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

34. `ls -F` - Prints a slash (`/`) after directory names, an asterisk (`*`) after executable files, and an at symbol (`@`) after symbolic links.
    - Usage: `ls -F [directory]`
    - Description: Lists files and directories in the specified directory, appending special characters to indicate the type of each entry.
    - Example:
      ```bash
      $ ls -F
      file1.txt  newfile.txt  dir1/  script.sh*
      ```
      
35. `history` - View Command History
    - Usage: `history`
    - Description: Displays a list of previously executed commands in the terminal. From the history output, you can re-execute a command by typing `!n`, where `n` is the command number in the history list.
    - Example:
      ```bash
      $ history
      1  pwd
      2  ls -l
      3  cd dir1
      4  history

      $ !2 # This will re-execute the command `ls -l`
      total 8
      drwxr-xr-x 2 user user 4096 Jan 1 12:00 dir1
      -rw-r--r-- 1 user user  123 Jan 1 12:00 file1.txt
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

### Navigation

To navigate through directories while making changes, we can use the `~` symbol to represent the home directory. For example, if you want to navigate to a directory called `projects` in your home directory, you can use:

```bash
$ cd ~/projects
```

This command will take you to the `projects` directory located in your home directory, regardless of your current location in the filesystem.

### Downloading Data on the Command Line

#### Using `curl`

`curl` is a command-line tool used to transfer data from or to a server. It supports various protocols, including HTTP, HTTPS, FTP, and more. You can use `curl` to download files from the internet directly to your local machine.

The basic `curl` syntax is as follows:

```bash
$ curl [options] [URL]
```

We can view a full list of the options available for `curl` by using the `--help` flag:

```bash
$ curl --help
```

To download a file using `curl`, you can use the following command:

```bash
$ curl -O [URL]
```

To download a file and rename it, you can use:

```bash
$ curl -o [new_filename] [URL]
```

To download multiple files, you can use:

```bash
$ curl -O URL[0-9]
```

`curl` has two useful option flags in case of timeouts during downloads. 

- `-L` redirects the HTTP URL if a 300 error code is returned.
- `-C` allows you to resume a download if it was interrupted.

Putting everything together:

```bash
$ curl -L -O -C [URL]
```

The order of the flags does not matter, but the URL must always be last.

#### Using `wget`

`wget` is another command-line tool used for downloading files from the internet. It is non-interactive, meaning it can run in the background without requiring user input. It is used to download files over HTTP, HTTPS, SFTP, and FTP protocols.

To check if `wget` is installed on your system, you can use the following command:

```bash
which wget
```

To install `wget`, you can use the following command:

```bash
sudo apt-get install wget # For Debian/Ubuntu-based systems
brew install wget # For macOS with Homebrew
gnuwin32 wget # For Windows with GnuWin32
```

The basic `wget` syntax is as follows:

```bash
$ wget [option flags] [URL]
```

Some useful option flags for `wget` include:

- `-b` - Download in the background
- `-c` - Resume a download if it was interrupted
- `-q` - Turn off the `wget` output to the terminal

We can use all the option flags together as follows:

```bash
$ wget -bqc [URL]
```

To download multiple files with `wget`, we first need to save a list of file locations in a text file. Then, we can use the `-i` option to download all the files listed in that text file. For example, if we have a file called `file_list.txt` containing the URLs of the files we want to download, we can use the following command:

```bash
$ wget -i file_list.txt
```

We can also set an upper download bandwidth limit with the `--limit-rate` option. For example, to limit the download speed to 500 KB/s, we can use:

```bash
$ wget --limit-rate=500k -i file_list.txt
```

We can set a mandatory pause time (in seconds) between downloads with the `--wait` option. For example, to set a 5-second pause between downloads, we can use:

```bash
$ wget --wait=5 -i file_list.txt
```

`curl` can be used for downloading and uploading files from 20+ protocols and is easier to install across all operating systems while `wget` is primarily used for downloading files over HTTP, HTTPS, SFTP, and FTP, has many built-in functionalities for handling multiple downloads, and is more efficient for downloading large files. Both tools are powerful and can be used based on your specific needs and preferences.

#### `csvkit` for data processing on the command line

`csvkit` is a suite of command-line tools for working with CSV files. It allows you to perform various operations on CSV files, such as filtering, sorting, and converting them to other formats. To install `csvkit`, you can use the following command:

```bash
pip install csvkit or pip install --upgrade csvkit
```

`in2csv` is a tool within the `csvkit` suite that converts various file formats to CSV. For example, to convert an Excel file to CSV, you can use:

```bash
$ in2csv file.xlsx > file.csv
```

If, for example, the data we want is not in the first sheet of the Excel file, we can first print all sheet names and the specify the sheet we want to convert:

```bash
$ in2csv -n SpotifyData.xlsx
Sheet1
Sheet2
```

```bash
$ in2csv SpotifyData.xlsx --sheet "Sheet2" > Sheet2.csv
```

`csvlook` renders a CSV file in a pretty-printed format in the terminal. For example, to view the contents of a CSV file in a readable format, you can use:

```bash
$ csvlook file.csv
| column1 | column2 | column3 |
|---------|---------|---------|
| value1  | value2  | value3  |
```

`csvstat` provides statistics about the columns in a CSV file. For example, to get statistics about the columns in a CSV file, you can use:

```bash
$ csvstat file.csv
  1. column1
    <type>      Text
    <nulls>     0
    <uniqueness> 100%
    <min>       value1
    <max>       value10
  2. column2
    <type>      Number
    <nulls>     0
    <uniqueness> 90%
    <min>       1
    <max>       100
```

`csvcut` allows you to select specific columns from a CSV file. 

We can view the column names in a CSV file by using the `-n` option.

For example, to select only the `name` and `age` columns from a CSV file, you can use:

```bash
$ csvcut -c "name","age" file.csv
name,age
Alice,30
Bob,25
```

or by using the column numbers:

```bash
$ csvcut -c 1,2 file.csv
name,age
Alice,30
Bob,25
```

But if we are not sure about the column names, we can first print all column names and then select the columns we want:

```bash
$ csvcut -n file.csv
  1: name
  2: age
  3: city
```

`csvgrep` allows you to filter rows in a CSV file based on specific criteria. It must be paired with one of these options:

- `-m`: followed by the exact row value to match
- `-r`: followed by a regular expression to match
- `-f`: followed by the path to a file containing the values to match

For example, to filter rows where the `age` column is greater than 30, you can use:

```bash
$ csvgrep -c "age" -r "^[3-9][0-9]$" file.csv
name,age,city
Alice,35,New York
Bob,40,Los Angeles
```

`csvstack` stacks up the rows from two or more CSV files into a single CSV file. 

`csvstack -h` provides the usage information for the `csvstack` command.

For example, to combine `file1.csv` and `file2.csv` into a single file called `combined.csv`, you can use:

```bash
$ csvstack file1.csv file2.csv > combined.csv
```

However, we need to ensure that the columns in both files are the same and in the same order. If the columns are different, we can use the `-g` option to specify a group name for each file:

```bash
$ csvstack -g "file1","file2" file1.csv file2.csv > combined.csv
```

We can rename the column from group names to something more meaningful by using the `-n` option:

```bash
$ csvstack -g "file1","file2" -n "source" file1.csv file2.csv > combined.csv
```

To chain multiple commands together, `;` can be used to separate commands. For example, to convert an Excel file to CSV and then view its contents in a pretty-printed format, you can use:

```bash
$ in2csv file.xlsx > file.csv; csvlook file.csv
| column1 | column2 | column3 |
|---------|---------|---------|
| value1  | value2  | value3  |
```

`&&` links commands together such that the next command will only execute if the previous command was successful. For example, to convert an Excel file to CSV and then view its contents in a pretty-printed format only if the conversion was successful, you can use:

```bash
$ in2csv file.xlsx > file.csv && csvlook file.csv
| column1 | column2 | column3 |
|---------|---------|---------|
| value1  | value2  | value3  |
```

`|` allows you to pass the output of one command as input to another command. For example, to convert an Excel file to CSV and then view its contents in a pretty-printed format, you can use:

```bash
$ in2csv file.xlsx | csvlook
| column1 | column2 | column3 |
|---------|---------|---------|
| value1  | value2  | value3  |
```

### Database Operations on the Command Line

`sql2csv` executes an SQL query on a large variety of SQL databases such as MySQL, PostgreSQL, SQLite, and more. It outputs the results of the query in CSV format.

For full documentation, `sql2csv -h` provides the usage information for the `sql2csv` command. `sql2csv -v` or `sql2csv --verbose` provides the traceback of the command execution, which can be useful for debugging.

The syntax for `sql2csv` is as follows:

```bash
$ sql2csv --db "sqlite:///path/to/database.db" \
          --query "SELECT * FROM table_name" \
          > output.csv
```

Note that for SQLite, we start with `sqlite:///` followed by the path to the database file and ends with `.db`. For MySQL and PostgreSQL, the syntax is slightly different. For MySQL, we use `mysql://username:password@host:port/database_name`, and for PostgreSQL, we use `postgresql://username:password@host:port/database_name` with no `.db` extension.

`csvsql` allows you to execute SQL queries on CSV files. It treats the CSV file as a database table, enabling you to perform SQL operations such as SELECT, INSERT, UPDATE, and DELETE on the data.

It works by creating an in-memory SQLite database and loading the CSV data into it. You can then execute SQL queries on the loaded data. This is suitable for small to medium-sized CSV files, but may not be efficient for very large datasets.

The syntax for `csvsql` is as follows:

```bash
$ csvsql --query "SELECT * FROM file WHERE column_name = 'value'" file.csv
```

We can perform further operations such as joining multiple CSV files, filtering data, and aggregating results using SQL queries with `csvsql`. For example, to join two CSV files on a common column, you can use:

```bash
$ csvsql --query "SELECT a.*, b.* FROM file1 AS a JOIN file2 AS b ON a.common_column = b.common_column" file1.csv file2.csv
```

We can also push data back to the database using `csvsql` with the `--insert` option. For example, to insert data from a CSV file into a database table, you can use:

```bash
$ csvsql --db "sqlite:///path/to/database.db" --insert file.csv
```

We can add `--no-inference` to prevent `csvsql` from trying to infer the data types of the columns in the CSV file and treat them as text. Also, `--no-constraints` can be used to prevent `csvsql` from adding any constraints (such as primary keys or unique constraints) to the database table when creating it from the CSV file. This can be useful if you want to create a simple table without any restrictions on the data.

```bash
$ csvsql --no-inference --no-constraints --db "sqlite:///path/to/database.db" --insert file.csv
```

### Data Pipeline on the Command Line

Data job automation can be achieved on the command line by chaining together various commands and tools to create a data pipeline. A data pipeline is a series of steps that process and transform data from its raw form to a more usable format.

A `scheduler` is a tool that allows you to schedule and automate the execution of commands or scripts at specific times or intervals. Common schedulers include `cron` for Unix-like systems and `Task Scheduler` for Windows.

`cron` is a time-based job scheduler in Unix-like operating systems. It allows you to schedule commands or scripts to run automatically at specified times and intervals. The `crontab` command is used to manage the cron jobs.

To add a job to the `crontab`, we can use the following methods:

1. Open the terminal and type `crontab -e` to edit the crontab file or modify the crontab using a text editor of your choice.

2. Echo the command directly into the crontab using the following syntax:

```bash
$ echo "0 0 * * * /path/to/script.sh" | crontab
```

Then check if the job was added successfully with:

```bash
$ crontab -l
0 0 * * * /path/to/script.sh
```

In chosing when to schedule the job, the first five fields of the cron job specify the schedule:
- Minute (0-59)
- Hour (0-23)
- Day of the month (1-31)
- Month (1-12)
- Day of the week (0-7, where both 0 and 7 represent Sunday)

For example, to schedule a job to run every day at midnight, you would use:

```bash
$ echo "0 0 * * * /path/to/script.sh" | crontab
```

or

```bash
$ echo "0 0 * * * python /path/to/script.py" | crontab
```

To schedule a job to run every Monday at 9 AM, you would use:

```bash
$ echo "0 9 * * 1 /path/to/script.sh" | crontab
```

or

```bash
$ echo "0 9 * * 1 python /path/to/script.py" | crontab
```

Further resources can be found at: https://crontab.guru/ to see more ways to schedule cron jobs.