
**APT (Advanced Package Tool)** is a package management system used in **Debian, Ubuntu, Kali Linux**.

Kali is **Debian-based**, so APT is the default way to manage software.

Handles **installing, updating, upgrading, and removing packages**.

Automatically resolves **dependencies** (avoids _dependency hell_).

## Why APT is Important

- Applications depend on **shared libraries**.
- Different versions of libraries can break applications.
- APT:
- Tracks dependencies
- Installs required libraries automatically
- Keeps the system consistent and stable
## Updating Package Information

sudo apt update

- Downloads latest package lists from repositories
- **Does NOT install or upgrade software**
- Always run before installing or upgrading packages

## Upgrading Packages

### Upgrade all installed packages

sudo apt upgrade

- Upgrades installed packages
- **Does NOT remove existing packages**


### Upgrade a single package

Command > sudo apt upgrade metasploit-framework


## Searching for Packages

COMMAND > apt-cache search pure-ftpd


## Viewing Package Details

apt show resource-agents

## Removing Packages

sudo apt remove --purge pure-ftpd

Deletes:
- Program files
- Configuration files

## Cleaning Unused Dependencies

Command > apt autoremove


## Exam / Pentesting Notes (PEN-100)

- Always run `apt update` before installs

- Use `apt-cache search` to discover tools

- Prefer `apt install` over `dpkg`

- Use `dpkg` only when installing local `.deb` files

- Clean systems with `apt autoremove`


## Common Commands Summary

apt update

apt upgrade

apt-cache search packagename

apt show packagename

apt install packagename

apt remove --purge package

apt autoremove

dpkg -i file.deb

## Command Recall

**Q:** Update package list **A:** `apt update`

---

**Q:** Upgrade system packages **A:** `apt upgrade`

---

**Q:** Search packages **A:** `apt-cache search`

---

**Q:** Show package details **A:** `apt show`

---

**Q:** Install package **A:** `apt install`

---

**Q:** Remove package completely **A:** `apt remove --purge`

---

**Q:** Remove unused dependencies **A:** `apt autoremove`

---

**Q:** Install local .deb file **A:** `dpkg -i`

