# -*- coding: utf-8 -*-
"""
Linux Command Finder - Command Database


Keywords tika tiyenne English words wal + Singlish (romanized Sinhala)
words wal deka wamama, e nisa "file hadanna" wage type kalath eka hoyaganna puluwan.
"""

COMMANDS = [
    # ---------------- FILES & FOLDERS ----------------
    {
        "command": "touch filename.txt",
        "description": "Aluth empty file ekak hadanawa (create a new empty file)",
        "keywords": ["create file", "new file", "make file", "file hadanna", "file ekak hadanna", "touch"],
    },
    {
        "command": "mkdir foldername",
        "description": "Aluth folder ekak (directory) hadanawa",
        "keywords": ["create folder", "new folder", "make directory", "folder hadanna", "directory hadanna", "mkdir"],
    },
    {
        "command": "mkdir -p path/to/folder",
        "description": "Nested folders (folder athule folder) ekpaarama hadanawa",
        "keywords": ["nested folder", "sub folder hadanna", "folder athule folder", "mkdir -p"],
    },
    {
        "command": "cp source destination",
        "description": "File ekak copy karanawa",
        "keywords": ["copy file", "file copy karanna", "duplicate file", "cp"],
    },
    {
        "command": "cp -r source destination",
        "description": "Folder ekak (okkoma athule dewal ekka) copy karanawa",
        "keywords": ["copy folder", "folder copy karanna", "copy directory", "cp -r"],
    },
    {
        "command": "mv source destination",
        "description": "File/folder ekak move karanawa nathnam rename karanawa",
        "keywords": ["move file", "rename file", "file redi karanna", "wenas karanna nama", "mv", "gaman karawanna"],
    },
    {
        "command": "rm filename",
        "description": "File ekak delete karanawa",
        "keywords": ["delete file", "remove file", "file ain karanna", "file delete karanna", "rm"],
    },
    {
        "command": "rm -r foldername",
        "description": "Folder ekak (okkoma athule ewa ekka) delete karanawa",
        "keywords": ["delete folder", "remove folder", "folder ain karanna", "delete directory", "rm -r"],
    },
    {
        "command": "rm -rf foldername",
        "description": "Folder ekak force ekak delete karanawa (confirm nokara) - waradi welawakadi hondatama saveradiwenna",
        "keywords": ["force delete", "rm -rf", "delete without confirm"],
    },
    {
        "command": "ls -la",
        "description": "Current folder eke okkoma files/folders (hidden ewath) list karanawa, details ekka",
        "keywords": ["list files", "show files", "files balanna", "list directory", "ls", "okkoma files"],
    },
    {
        "command": "pwd",
        "description": "Dan innawa folder eke full path eka pennanawa",
        "keywords": ["current folder", "where am i", "kohomada mama innane", "current path", "pwd"],
    },
    {
        "command": "cd foldername",
        "description": "Wena folder ekakata yanawa (change directory)",
        "keywords": ["change folder", "go to folder", "folder ekata yanna", "cd"],
    },
    {
        "command": "cat filename",
        "description": "File ekaka content screen eke pennanawa",
        "keywords": ["view file", "show file content", "read file", "file balanna", "cat"],
    },
    {
        "command": "less filename",
        "description": "Loku file ekak paginated widihata balanna (scroll karala balanna)",
        "keywords": ["view large file", "scroll file", "less command", "loku file balanna"],
    },
    {
        "command": "nano filename",
        "description": "File ekak terminal eke thiyenakota edit karanawa (simple editor)",
        "keywords": ["edit file", "file edit karanna", "nano editor", "terminal edit"],
    },
    {
        "command": "find /path -name \"filename\"",
        "description": "File ekak wisala widihata (path ekak athule) soyanawa",
        "keywords": ["find file", "search file", "file soyanna", "find command", "locate file"],
    },
    {
        "command": "chmod 755 filename",
        "description": "File ekaka permissions wenas karanawa (read/write/execute)",
        "keywords": ["change permission", "file permission", "permission denna", "chmod", "execute permission"],
    },
    {
        "command": "chown user:group filename",
        "description": "File ekaka owner ekak wenas karanawa",
        "keywords": ["change owner", "file owner", "chown", "owner denna"],
    },
    {
        "command": "wc -l filename",
        "description": "File ekaka lines ganana count karanawa",
        "keywords": ["count lines", "line count", "wc", "lines ganana"],
    },
    {
        "command": "diff file1 file2",
        "description": "File dekaka wenasa (difference) balanawa",
        "keywords": ["compare files", "file diff", "difference between files", "diff"],
    },

    # ---------------- ARCHIVE / COMPRESSION ----------------
    {
        "command": "tar -czvf archive.tar.gz foldername",
        "description": "Folder ekak .tar.gz widihata compress karanawa",
        "keywords": ["compress folder", "create tar", "zip folder", "compress karanna", "tar"],
    },
    {
        "command": "tar -xzvf archive.tar.gz",
        "description": ".tar.gz file ekak extract karanawa",
        "keywords": ["extract tar", "unzip tar", "extract karanna", "decompress"],
    },
    {
        "command": "zip -r archive.zip foldername",
        "description": "Folder ekak .zip file ekak widihata compress karanawa",
        "keywords": ["create zip", "zip folder", "compress zip", "zip karanna"],
    },
    {
        "command": "unzip archive.zip",
        "description": ".zip file ekak extract karanawa",
        "keywords": ["extract zip", "unzip", "unzip karanna", "open zip"],
    },

    # ---------------- SYSTEM / PROCESS ----------------
    {
        "command": "ps aux",
        "description": "Dan run wena okkoma processes list karanawa",
        "keywords": ["list processes", "running processes", "process balanna", "ps"],
    },
    {
        "command": "top",
        "description": "System resources (CPU/RAM) real-time widihata balanawa",
        "keywords": ["system monitor", "cpu usage", "ram usage", "resource balanna", "top"],
    },
    {
        "command": "htop",
        "description": "top wage system monitor ekak, ehema graphical widihata (install karanna one)",
        "keywords": ["htop", "nice system monitor", "cpu memory graph"],
    },
    {
        "command": "kill PID",
        "description": "Process ID ekak dala process ekak niwathanawa",
        "keywords": ["kill process", "stop process", "process kill karanna", "process nawathanna", "kill"],
    },
    {
        "command": "kill -9 PID",
        "description": "Process ekak force ekak niwathanawa",
        "keywords": ["force kill", "kill -9", "force stop process"],
    },
    {
        "command": "killall processname",
        "description": "Namak dala process okkoma (instances okkoma) niwathanawa",
        "keywords": ["killall", "kill by name", "process name kill karanna"],
    },
    {
        "command": "df -h",
        "description": "Disk eke space kochchara athida kiyala balanawa",
        "keywords": ["disk space", "storage balanna", "hard disk space", "df"],
    },
    {
        "command": "du -sh foldername",
        "description": "Folder ekak kochchara size ekakda kiyala balanawa",
        "keywords": ["folder size", "disk usage", "check folder size", "du"],
    },
    {
        "command": "free -h",
        "description": "RAM memory kochchara athida, kochchara use wenawada kiyala balanawa",
        "keywords": ["ram check", "memory usage", "check ram", "free"],
    },
    {
        "command": "uname -a",
        "description": "System eke details (kernel, architecture) balanawa",
        "keywords": ["system info", "kernel version", "uname", "system details"],
    },
    {
        "command": "lscpu",
        "description": "CPU details balanawa",
        "keywords": ["cpu info", "processor details", "lscpu"],
    },
    {
        "command": "uptime",
        "description": "System eka kalada on wela thiyenne kiyala balanawa",
        "keywords": ["system uptime", "how long running", "uptime"],
    },
    {
        "command": "reboot",
        "description": "Computer eka restart karanawa",
        "keywords": ["restart computer", "reboot", "computer restart karanna"],
    },
    {
        "command": "shutdown now",
        "description": "Computer eka wahanawa (shutdown)",
        "keywords": ["shutdown computer", "turn off", "computer wahanna", "poweroff"],
    },
    {
        "command": "whoami",
        "description": "Dan login wela innne kauda kiyala pennanawa",
        "keywords": ["current user", "who am i", "whoami"],
    },
    {
        "command": "history",
        "description": "Kalin run kala commands list ekak pennanawa",
        "keywords": ["command history", "previous commands", "history"],
    },
    {
        "command": "clear",
        "description": "Terminal screen eka clean karanawa",
        "keywords": ["clear screen", "clean terminal", "screen clear karanna", "clear"],
    },

    # ---------------- USERS ----------------
    {
        "command": "sudo useradd username",
        "description": "Aluth user ekak hadanawa",
        "keywords": ["create user", "add user", "new user", "user hadanna", "useradd"],
    },
    {
        "command": "sudo passwd username",
        "description": "User ekaka password eka wenas karanawa",
        "keywords": ["change password", "set password", "password wenas karanna", "passwd"],
    },
    {
        "command": "sudo deluser username",
        "description": "User ekak delete karanawa",
        "keywords": ["delete user", "remove user", "user ain karanna", "deluser"],
    },
    {
        "command": "sudo usermod -aG groupname username",
        "description": "User ekak group ekakata add karanawa",
        "keywords": ["add user to group", "usermod", "group ekata add karanna"],
    },

    # ---------------- PACKAGE MANAGEMENT ----------------
    {
        "command": "sudo apt update",
        "description": "Package list eka update karanawa (Debian/Ubuntu)",
        "keywords": ["update packages", "apt update", "package list update"],
    },
    {
        "command": "sudo apt upgrade",
        "description": "Install wela thiyena packages okkoma upgrade karanawa",
        "keywords": ["upgrade packages", "apt upgrade", "system update"],
    },
    {
        "command": "sudo apt install packagename",
        "description": "Aluth software ekak install karanawa",
        "keywords": ["install software", "install package", "install karanna", "apt install"],
    },
    {
        "command": "sudo apt remove packagename",
        "description": "Software ekak uninstall karanawa",
        "keywords": ["uninstall software", "remove package", "uninstall karanna", "apt remove"],
    },
    {
        "command": "sudo apt autoremove",
        "description": "Awashya nathi packages okkoma clean karanawa",
        "keywords": ["clean packages", "autoremove", "unused packages remove"],
    },
    {
        "command": "sudo dpkg -i package.deb",
        "description": ".deb file ekak install karanawa",
        "keywords": ["install deb file", "dpkg", ".deb install"],
    },

    # ---------------- NETWORK ----------------
    {
        "command": "ip a",
        "description": "Computer eke IP address balanawa",
        "keywords": ["ip address", "check ip", "network address", "ip a", "ifconfig"],
    },
    {
        "command": "ping google.com",
        "description": "Internet connection eka test karanawa",
        "keywords": ["test internet", "ping", "check connection", "internet balanna"],
    },
    {
        "command": "curl https://example.com",
        "description": "URL ekaka content download karala terminal eke pennanawa",
        "keywords": ["download url content", "curl", "fetch website"],
    },
    {
        "command": "wget https://example.com/file.zip",
        "description": "Internet eken file ekak download karanawa",
        "keywords": ["download file", "wget", "file download karanna"],
    },
    {
        "command": "ssh user@hostname",
        "description": "Wena computer ekakata remote widihata connect wenawa",
        "keywords": ["remote connect", "ssh", "connect to server"],
    },
    {
        "command": "scp file.txt user@hostname:/path",
        "description": "File ekak network eken wena computer ekakata copy karanawa",
        "keywords": ["copy file over network", "scp", "remote copy"],
    },
    {
        "command": "sudo netstat -tulnp",
        "description": "Open wela thiyena network ports balanawa",
        "keywords": ["check ports", "open ports", "netstat", "port balanna"],
    },

    # ---------------- TEXT PROCESSING ----------------
    {
        "command": "grep \"text\" filename",
        "description": "File ekak athule text ekak soyanawa",
        "keywords": ["search text in file", "grep", "find text", "text soyanna"],
    },
    {
        "command": "grep -r \"text\" foldername",
        "description": "Folder ekak athule okkoma files walin text ekak soyanawa",
        "keywords": ["search text in folder", "recursive grep", "grep -r"],
    },
    {
        "command": "sed 's/old/new/g' filename",
        "description": "File ekaka text replace karanawa",
        "keywords": ["replace text", "find and replace", "sed", "text wenas karanna"],
    },
    {
        "command": "sort filename",
        "description": "File ekaka lines sort karanawa",
        "keywords": ["sort file", "sort lines", "sort"],
    },
    {
        "command": "awk '{print $1}' filename",
        "description": "File ekaka columns walin data ekak print karanawa",
        "keywords": ["awk", "print column", "extract column"],
    },

    # ---------------- GIT ----------------
    {
        "command": "git clone https://github.com/user/repo.git",
        "description": "GitHub repository ekak download karanawa",
        "keywords": ["clone repo", "git clone", "download repository"],
    },
    {
        "command": "git status",
        "description": "Git repo eke dan tiyena wenaskam status eka balanawa",
        "keywords": ["git status", "check changes"],
    },
    {
        "command": "git add .",
        "description": "Wenaskam okkoma commit ekata add karanawa",
        "keywords": ["git add", "stage changes"],
    },
    {
        "command": "git commit -m \"message\"",
        "description": "Wenaskam commit karanawa message ekak ekka",
        "keywords": ["git commit", "commit changes"],
    },
    {
        "command": "git push",
        "description": "Commit karapu wenaskam GitHub ekata upload karanawa",
        "keywords": ["git push", "upload changes", "push to github"],
    },
    {
        "command": "git pull",
        "description": "GitHub eken aluthma wenaskam download karanawa",
        "keywords": ["git pull", "download latest changes"],
    },
]
