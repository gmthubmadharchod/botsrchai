# 🚀 Speed Optimization Guide for Windows RDP

## Issues Fixed

### 1. ✅ Client Optimization
- **Main Bot Client**: Increased workers to 100, added `max_concurrent_transmissions=10`
- **User Account Clients**: Optimized with workers=100 and max_concurrent_transmissions=10
- **Batch Processing**: Reduced sleep delay from 1s to 0.1s between files

### 2. ✅ Encryption Speedup
- Added `pycryptodome` to requirements.txt for faster encryption (works on Windows without C++ compiler)

## ⚠️ Windows RDP Network Throttling

Windows RDP may throttle network traffic by default. Here's how to fix it:

### Method 1: Disable RDP Network Throttling (Recommended)

1. **Open Registry Editor** (Win + R, type `regedit`)
2. Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TermService\Parameters`
3. Create a new **DWORD (32-bit)** value named: `NetworkThrottlingIndex`
4. Set value to: `4294967295` (or `ffffffff` in hex) - This disables throttling
5. **Restart** the RDP server

### Method 2: PowerShell Command (Run as Administrator)

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\TermService\Parameters" -Name "NetworkThrottlingIndex" -Value 4294967295 -PropertyType DWORD -Force
Restart-Computer
```

### Method 3: Windows Group Policy (If available)

1. Open **Group Policy Editor** (`gpedit.msc`)
2. Navigate to: `Computer Configuration` → `Administrative Templates` → `Windows Components` → `Remote Desktop Services` → `Remote Desktop Session Host` → `Remote Session Environment`
3. Find **"Configure network throttling"**
4. Set to **"Disabled"** or **"Maximum bandwidth available"**

## 📦 Install Updated Dependencies

After making changes, reinstall dependencies:

```bash
pip install -r requirements.txt --upgrade
```

## 🔧 Additional Optimizations

### 1. Check Windows Network Adapter Settings

1. Open **Network Connections** (`ncpa.cpl`)
2. Right-click your network adapter → **Properties**
3. Click **Configure** → **Advanced** tab
4. Look for **"Flow Control"** or **"Receive Buffers"**
5. Set **Flow Control** to **"Disabled"** (if available)
6. Increase **Receive Buffers** to maximum

### 2. Disable Windows QoS Packet Scheduler

1. In Network Adapter Properties (above)
2. **Uncheck** "QoS Packet Scheduler" if enabled
3. Click **OK**

### 3. Check Firewall/Antivirus

- Temporarily disable Windows Firewall to test
- Check if antivirus is scanning network traffic
- Add bot directory to antivirus exclusions

### 4. Telegram Server Location

- Telegram servers may be geographically distant
- Use a VPN or proxy closer to Telegram servers if needed
- Check ping to `api.telegram.org`: `ping api.telegram.org`

## 🧪 Test Speed

After applying fixes:

1. Restart the RDP server
2. Restart the bot
3. Test download/upload speed
4. Check if speed improved

## 📊 Expected Performance

- **Before**: ~100-500 KB/s
- **After**: Should reach 10-50+ MB/s (depending on file size and Telegram limits)

## ⚡ Telegram API Limits

Note: Telegram has rate limits:
- **Download**: ~20-30 MB/s per connection
- **Upload**: ~10-20 MB/s per connection
- **Multiple connections**: Can increase total speed

The bot now uses `max_concurrent_transmissions=10` to utilize multiple connections.

## 🆘 Still Slow?

If speed is still slow after these fixes:

1. **Check actual network speed**: Run `speedtest-cli` or visit speedtest.net
2. **Check RDP connection quality**: Lower RDP display quality to reduce bandwidth usage
3. **Check server resources**: CPU/RAM usage might be bottleneck
4. **Test from different location**: Rule out network routing issues
5. **Check Telegram status**: Telegram servers might be slow

## 📝 Notes

- RDP network throttling is a **Windows feature** to prevent RDP from consuming all bandwidth
- Disabling it may affect RDP performance if you're actively using the remote desktop
- Consider using a dedicated server or VPS instead of RDP for production bots

