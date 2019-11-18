# f(un)*society00
## Operation WulfDoS

Description & Purpose:
  * Operation WulfDoS is an attempt to DDoS attack an intentionally vulnerable linux OS running on Raspberry Pi: [RasPwn](https://raspwn.org/index).
  * WulfDoS uses a Beowulf Cluser to execute a simulated DDoS Attack on the RasPwn SSID.
  * Knowledge obtained from Operation WulfDoS:
    - Better understanding TCP vs UDP
    - How to Build a HPC cluster
    - How to perform a DoS attack (TCP & UDP)

Technical Specifications:
  * Hardware: 
    - 3x Raspberry Pi 3
    - 5x Raspberry Pi 4
    - 1x 2TB Seagate External Harddrive
    - 1x Netgear multi-port ethernet splitter
    - 1x Raspberry Pi Tower Case
  * Software: 
    - Linux
    - Raspbian Lite (Debian CLI)
  * Packages: 
    - Slurm (Slurmd, Slurm-Client, Slurmctl)
    - Munge
    - NFS Kernel Server
    - Sockets
    - NTPUpdate
  * Programming Languages: 
    - Python 
    - Bash/Shell Scripting

Main Functionality: Execute DoS script across a 6-pi Beowulf Cluster

## WulfDoS: the flood is coming...