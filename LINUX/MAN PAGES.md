[[OSCP-FUNDAMENTALS/LINUX/LINUX BASIC COMMANDS]]

Most Linux programs come with built-in documentation called **manual pages**, or **man pages**.
- They explain what a command does
- Show how to use it
- List all available options

These manuals are categorized as below -

![](IMAGES/image-43.png)

EXAMPLE: man ls
![](IMAGES/image-44.png)

When you run: man passwd: 
Linux shows **section 1 by default**, which documents the **`passwd` command** (used to change passwords).

But you wanted to learn about the **file format** of `/etc/passwd`, not the command.

That information is in **section 5**, not section 1.
The `-k` option lets you **search all man pages by keyword**.
Command: man -k passwd

This searches every manual page that contains the word _passwd_ and shows:

- The page name
- The section number
- A short description

![](IMAGES/image-45.png)

This helps you find **where the information lives**.

To avoid partial matches, you can use a **regular expression**:
man -k '^find$'
![](IMAGES/image-46.png)

man -k '^passwd$'
![](IMAGES/image-47.png)

- `^` means _start of the line_
- `$` means _end of the line_

This ensures only **exact matches** for “passwd” are returned.

Now you know:
- Section **1** → command
- Section **5** → file format

Opening a specific man page section

man 5 passwd:
![](IMAGES/image-48.png)

The above shows information about file passwd.
- Field order
- What each field means
- How user information is stored

#help 
example : ls -h 
## Using `-h` or `--help` for quick help

Sometimes you don’t need the full manual—just a quick overview.
Many commands support:
- `-h`
- `--help`

![](IMAGES/image-49.png)

This displays:

- Basic usage
- A list of options
- Short explanations for each option

## When to use each method

### ✅ Use `man` when:

- You want **detailed documentation**
- You need to understand **all options**
- You’re learning deeply


### ✅ Use `-h` / `--help` when:

- You want **quick usage info**
- You already know the command basics


**COMMAND SUMMARY**

man
man -k
man -k 'passwd'
man -k '^passwd$'
man 5 passwd

ls -help
more -h

![](IMAGES/image-50.png)

