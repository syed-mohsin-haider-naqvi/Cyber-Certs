# Packet Tracer — Configure Basic Wireless Security

**Course:** Endpoint Security (Cisco Networking Academy)
**Lab:** 5.3.10 — Configure Basic Wireless Security

---

## Scenario

A small business owner realizes his wireless network needs securing against unauthorized access and wants WPA2 Personal set up. The task was straightforward on paper — confirm the network works before any security is applied, configure WPA2 Personal on the router, connect the laptop with the new passphrase, then confirm the network still works exactly the same as before, just now actually secured.

This is the first wireless-specific config task I've done — everything else so far across the Cisco courses has been wired network, endpoint, or log-analysis focused, so this was genuinely new territory.

---

## Part 1 — Verifying Connectivity Before Any Security

Before touching any settings, opened the laptop's web browser and navigated to `www.cisco.pka` to confirm the site actually loaded over the wireless connection as it currently stood — unsecured, but functional. Page displayed fine.

<img width="352" height="472" alt="image" src="https://github.com/user-attachments/assets/8b6d26b8-e415-4c29-bbbb-643d736f2b65" />

This step matters for the same reason it did in other labs — establishing a working baseline first means if something breaks later, it's clearly the security change causing it, not some unrelated connectivity issue.

---

## Part 2 — Configuring WPA2 Personal on the Router

Accessed the wireless router's admin page by entering its IP (`192.168.1.1`) directly into the browser, logging in with `admin` / `admin` for username and password.

<img width="359" height="475" alt="image" src="https://github.com/user-attachments/assets/d61be025-1aa4-4d3b-aad8-e4ea40e6a71c" />

Navigated to the Wireless menu, then into Wireless Security specifically. The security mode was sitting on Disabled by default — changed the 2.4 GHz network's security mode to **WPA2 Personal**, and entered `Network123` in the Passphrase field. Left the 5 GHz networks alone as disabled, per the instructions — the small business setup here only needed the 2.4 GHz band actually secured.

Scrolled down and saved the settings, then closed the browser to move on to the client side.

---

## Part 3 — Reconnecting the Laptop With the New Security

With the router now requiring WPA2, the laptop's existing open connection wouldn't work anymore — needed to reconnect properly with the new credentials.

Opened PC Wireless from the laptop's desktop, went to the Connect tab, and selected the **Academy** network from the list of available wireless networks. The site information panel confirmed the network was now showing `WPA2-PSK` as its security type — visible proof the router-side change had actually taken effect and was being broadcast.

<img width="720" height="420" alt="image" src="https://github.com/user-attachments/assets/925c9d66-502b-492e-8076-47a9e481f974" />

Clicking Connect prompted for the pre-shared key. Entered `Network123` and hit Connect.

<img width="718" height="453" alt="image" src="https://github.com/user-attachments/assets/1b0f83e9-8ae2-4b10-9838-a6f903e3fee2" />

---

## Part 4 — Verifying Connectivity Still Works

Went back to the web browser and reloaded `www.cisco.pka` — page loaded successfully again, same as before the security was applied. Confirmed the laptop was genuinely connected and passing traffic through the now-secured network, not just showing a connected status without actual working connectivity.

Packet Tracer's activity results also confirmed everything checked out correctly — "Congratulations Guest! You completed the activity," with a 100% pass across the assessment items and connectivity tests.

<img width="722" height="555" alt="image" src="https://github.com/user-attachments/assets/85d56515-1174-48f8-9bc2-194e7b6f7dd1" />
<img width="717" height="392" alt="image" src="https://github.com/user-attachments/assets/a299933e-74c6-4e14-bf8b-9e28ce911639" />

---

## Putting It Together

The core idea of this lab was proving that adding security doesn't have to mean breaking functionality — the network needed to work identically for a legitimate user before and after, with the only real difference being that an attacker without the passphrase can no longer just join freely. Testing connectivity at both the start and the end made that comparison concrete rather than just assumed.

---

## What Tripped Me Up

Nothing here gave me real trouble — this was one of the more straightforward labs so far, mostly because the steps were laid out clearly and WPA2 Personal setup is genuinely a simple, well-defined process once you know where the settings live in the router admin panel. If anything, the main thing worth remembering for next time is just where the Wireless Security menu sits specifically, since that's not always in the same place across different router admin interfaces in the real world.

---

## Tools Used

- Cisco Packet Tracer (router admin web interface, PC Wireless connection utility, laptop browser for verification)
