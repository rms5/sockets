# UDP Packets

### These scripts are for sending and receiving UDP packets over a network.

##### For one Linux and one OS X machine:

On the Linux machine: 

* Run the init_wifi_ad_hoc.sh script from the wifi_scripts repo to set up a network called "rockets."  This computer's IP address is set to 10.0.0.8.

* Run receive.py and wait for sender.

On the OS X machine:

* Connect to the "rockets" network.

* In the TCP/IP tab under Advanced Wi-Fi Network Preferences, select "Manually" from the "Configure IPv4" dropdown. Then set the following fields:

```
IPv4 Address: 10.0.0.10
Subnet Mask: 255.255.255.0
```

* Run send.py with an integer command-line argument to specify how many packets to send.


###### NOTE: If you want the Linux computer to be the sender, you will have to either
1. Change the IP addresses in these scripts to 10.0.0.10

  OR 
  
2. Change the IP address of the Linux computer as set by init_wifi_ad_hoc.sh to 10.0.0.10, and set the IP address of the Mac to 10.0.0.8 in Network Preferences.
