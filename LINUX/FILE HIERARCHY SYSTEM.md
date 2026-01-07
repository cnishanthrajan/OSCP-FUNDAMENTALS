
The FHS exists so that when users interact with an unfamiliar Linux environment, they can still find their way around the machine.

### `/bin`

- Basic commands needed by everyone
- Examples: `ls`, `cp`, `mv`

### `/boot`

- Files needed to **start (boot)** Linux
- Includes the Linux kernel

### `/dev`

- Files that represent **devices**
- Hard disks, USB, keyboard, mouse
- Linux treats devices like files

### `/etc`

- **Configuration files**
- System settings live here
- Think of it as **control settings**

### `/home`

- **Personal folders for users**
-example: /home/nishanth
This is where **your files, downloads, and documents** are
Very important for users and security.

### `/lib`

- **Libraries** needed by basic programs
- Like shared helper files for software
- `/lib` = **helper files for programs**
### `/media`

- Where **USB drives, CDs, DVDs** are mounted
- Plug in a USB → it appears here


### `/mnt` or `/mount`

- **Temporary mount point**
- Usually used by system admins

### `/opt`

- **Optional / third-party software**
- Software not installed by default

### `/root`

- Home directory of the **administrator (root)**
- Normal users cannot access this

### `/run`

- Temporary **runtime data**
- Cleared after reboot
- Used while system is running

### `/sbin`

- System administration programs
- Used mainly by root

### `/srv`

- Data for **server services**
- Example: web server files

### `/tmp`

- Temporary files
- Usually **deleted at reboot**
- Anyone can use it

### `/usr`

- Most **applications and programs**

- Subfolders:

    - `/usr/bin`
    - `/usr/lib`
    - `/usr/sbin`

📁 `/usr/share`
- Data that works on all systems (icons, docs)

📁 `/usr/local`
- Programs installed **manually by admin**
- Won’t interfere with system updates

### `/var`

- **Variable data** (changes often)
- Includes:
    - Logs (`/var/log`)
    - Caches
    - Mail queues
- 
### `/proc` and `/sys`

- Special directories created by the **kernel**
- Show system and hardware info
- Not real files on disk

## Hidden files (dot files)

- Files starting with a **dot (.)** are hidden
- Example:
.bashrc
.profile

These usually store **program settings**.


## Configuration directories inside home

Some programs create **folders** instead of single files.

Example:
~/.ssh/
This stores:
- SSH keys
- SSH settings

## Desktop and Mail folders

- `~/Desktop/`

- Files shown on your graphical desktop

- `~/Mail/`
  Sometimes used to store emails
