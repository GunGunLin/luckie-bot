// ══ Gesture Detection ══
function onResults(res) {
    const lm = res.multiHandLandmarks?.[0];
    if (!lm) {
        document.getElementById('magic-dot').style.display = 'none';
        document.getElementById('magic-array').style.opacity = '0';
        return;
    }
    const x = (1 - lm[9].x) * window.innerWidth, y = lm[9].y * window.innerHeight;
    if (Math.random() > 0.5) particles.push(new Particle(x, y));
    document.body.style.setProperty('--hx', (1-lm[9].x)*100+'%');
    document.body.style.setProperty('--hy', lm[9].y*100+'%');

    if (curScene === 's2') {
        const isFist = [8,12,16,20].every(idx => lm[idx].y > lm[idx-2].y);
        const array = document.getElementById('magic-array');
        if (isFist && !charging && picked.length < 3) { chargeStart = Date.now(); charging = true; array.style.opacity = '1'; }
        if (charging) {
            const prog = (Date.now() - chargeStart) / 1000;
            if (prog > 1.2) { selectOne(); charging = false; array.style.opacity = '0'; }
        }
        if (!isFist) { charging = false; array.style.opacity = '0'; }
        if (x < window.innerWidth * 0.35) velocity -= SCROLL_ACCEL;
        else if (x > window.innerWidth * 0.65) velocity += SCROLL_ACCEL;
    }
}

// ══ Sprite Face Control ══
function setSpriteFace(type) {
    if (customSpriteImg) {
        const emotionMap = { 'O': '😮', 'S': '😌', 'Normal': '' };
        setEmoji(emotionMap[type] || '');
        return;
    }
    const mouth = document.getElementById('sp-mouth');
    const eyeL = document.getElementById('eye-l'); const eyeR = document.getElementById('eye-r');
    if (type === 'O') { mouth.setAttribute('d', 'M46 65 Q50 58 54 65'); eyeL.setAttribute('ry', '1.5'); eyeR.setAttribute('ry', '1.5'); }
    else if (type === 'S') { mouth.setAttribute('d', 'M45 62 Q50 62 55 62'); eyeL.setAttribute('ry', '0.5'); eyeR.setAttribute('ry', '0.5'); }
    else { mouth.setAttribute('d', 'M40 62 Q50 69 60 62'); eyeL.setAttribute('ry', '4.5'); eyeR.setAttribute('ry', '4.5'); }
}

function setEmoji(emoji) {
    const el = document.getElementById('sprite-emotion');
    el.innerText = emoji;
    el.style.display = emoji ? 'block' : 'none';
}

// ══ Settings ══
function openSettings() {
    document.getElementById('api-input').value = apiKey;
    document.getElementById('birth-input').value = birthDate;
    if (customSpriteImg) {
        document.getElementById('settings-sprite-preview').innerHTML = `<img class="sprite-preview" src="${customSpriteImg}">`;
    }
    document.getElementById('settings-modal').style.display = 'flex';
}
function saveSettings() {
    apiKey = document.getElementById('api-input').value;
    birthDate = document.getElementById('birth-input').value;
    localStorage.setItem('lb_ds_api', apiKey);
    localStorage.setItem('lb_birth', birthDate);
    document.getElementById('settings-modal').style.display = 'none';
    showSpriteBubble('Contract bound. Connection updated ✦');
}
