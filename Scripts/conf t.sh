conf t
hostname R3

int fa0/0
ip address 10.10.10.10 255.255.255.0
no shut

conf t
hostname R2

int fa0/0
ip address 10.10.10.11 255.255.255.0
no shut

int fa0/1
ip address 11.11.11.11 255.255.255.0
no shut



conf t
hostname R1

int fa0/1
ip address 11.11.11.10 255.255.255.0
no shut