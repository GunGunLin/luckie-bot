// ══ Serial ══
var port;
async function connectSerial() {
    try {
        port = await navigator.serial.requestPort();
        await port.open({ baudRate: 115200 });
        document.getElementById('status-text').innerText = "VIBRATION READY";
    } catch(e) { showSpriteBubble('Connection failed. Mouse control active.'); }
}
async function hw(msg) { if (port?.writable) { const w = port.writable.getWriter(); await w.write(new TextEncoder().encode(msg+'\n')); w.releaseLock(); }}
