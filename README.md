# f(un)*society00
## Operation WulfDoS

Description & Purpose:
  * Operation WulfDoS is our attempt to bring down a intentionally vulnerable linux image loaded to a Raspberry Pi called [RasPWN](https://raspwn.org/index).
  * We're using a Beowulf Cluser +II to execute a DDoS Attack on the RasPWN SSID.
  * Purely an academic pursuit, WulfDoS will teach us more about how TCP vs UDP works, and we'll learn about how to put parrallel process multiple raspberry pi computers into one HPC.

Technical Specifications:
  * Hardware: Raspberry Pi 3 & 4, Netgear multi-port ethernet splitter
  * Software: Linux, Raspbian Lite (Debian CLI)
  * Packages: Slurm (Slurmd, Slurm-Client, Slurmctl), Munge, NFS Kernel Server, Sockets
  * Languages: Python, BASH

Main Functionality: Execute DoS script across multiple raspberry pi computers

## WulfDoS: Coming for your processes 