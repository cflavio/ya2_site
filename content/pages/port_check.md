Title: Check your ports
Status: hidden

Currently, if you want to play a multiplayer race, Yorg requires that users who host a race should open their port 9099 on their router and on their firewall. **Please note that this requirement will be removed in future releases of Yorg**. If you want to host a race and you can't do that, you should check if your port 9099 is actually open.

How to check if your port 9099 is open
--------------------------------------

First of all, you need to listen to something on the port 9099. You can do this by inviting a user to a match clicking on the "plus" sign on the right side.

<p align="center"><a href="{filename}/images/misc/invite.jpg"><img src="{filename}/images/misc/invite.jpg" width="660" height="371" /></a></p>

When you are in the "room" page (i.e. the following screen)

<p align="center"><a href="{filename}/images/misc/room.jpg"><img src="{filename}/images/misc/room.jpg" width="660" height="371" /></a></p>

you can actually check if your port is open. You can go on [this site](https://www.yougetsignal.com/tools/open-ports) (anyway, there are a lot of alternative sites that do this), and type *9099* in the *Port Number* field. Then, you can push the *Check* button. If the check is positive, then you can host races in Yorg. Otherwise, if the check is negative and you want to host races in Yorg, please check the following conditions:

* your router is configured for port-forwarding traffic on port 9099 to your host;
* your firewall allows traffic on port 9099 for Yorg.

Again, we'll remove this requirement in the future, this is only a temporary step for hosting races. Thank you very much!