// Global variable to store the fetch promise
var bgOraclePromise = null;

function startZen() {
    goScene('s3');
    let r = 0;
    const orb = document.getElementById('med-orb');
    
    // START API FETCH IMMEDIATELY IN BACKGROUND
    const prompt = `You are Luckie-Bot, a gentle and mysterious guide of fate. Intent: ${category}. Tarot cards chosen (Past/Present/Future): ${picked.map(c=>c.n).join(', ')}. Please provide an elegant reading in English, following this 3-section structure (separate sections with ---, no title symbols): 1. Deep Reading: 2-3 poetic paragraphs. 2. Core Insight: A single punchy, positive sentence. 3. Daily Quest: A specific actionable task.`;
    bgOraclePromise = fetch("https://api.siliconflow.cn/v1/chat/completions", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${apiKey}` },
        body: JSON.stringify({ model: "deepseek-ai/DeepSeek-V3", messages: [{role:"user", content:prompt}], temperature: 0.85 })
    }).then(r => r.json());
    
    const zen = () => {
        if (r >= 3) { doAI(); return; }
        
        document.getElementById('med-text').innerText = "INHALE";
        orb.style.transform = "scale(2.2)";
        orb.classList.add('inhaling');
        setSpriteFace('S'); setEmoji('🌬️'); hw('BREATHE:IN');
        
        // 呼吸吸收能量特效
        for(let i=0; i<6; i++) {
            setTimeout(spawnOrbParticle, i * 400);
        }

        setTimeout(() => {
            document.getElementById('med-text').innerText = "EXHALE";
            orb.style.transform = "scale(1)";
            orb.classList.remove('inhaling');
            setSpriteFace('O'); setEmoji('💨'); hw('BREATHE:OUT');
            
            setTimeout(() => { r++; zen(); }, 4000);
        }, 4000);
    }; 
    zen();
}

function spawnOrbParticle() {
    if (curScene !== 's3') return;
    const p = document.createElement('div');
    p.className = 'orb-particle';
    p.innerText = '✦';
    
    // 生成圆环状围绕分布的初始位置
    const angle = Math.random() * Math.PI * 2;
    const dist = 180 + Math.random() * 100; // 距离中心的起始半径
    const tx = Math.cos(angle) * dist;
    const ty = Math.sin(angle) * dist;
    
    p.style.setProperty('--tx', `${tx}px`);
    p.style.setProperty('--ty', `${ty}px`);
    
    // 将粒子添加到 s3 场景内，确保不被 orb 挡住
    document.getElementById('s3').appendChild(p);
    
    // 动画结束后移除
    setTimeout(() => p.remove(), 3500);
}

async function doAI() {
    goScene('s4');
    setEmoji('🔮');
    const body = document.getElementById('oracle-body');
    // 在这显示等待字样，以防 API 在 12 秒呼吸后依然没返回
    body.innerHTML = `<div style="text-align:center; padding:150px; color:var(--g); letter-spacing:10px">WEAVING DESTINY TAPESTRY...</div>`;
    
    try {
        const data = await bgOraclePromise; // Await the background fetch triggered in startZen()
        if(!data || !data.choices) throw new Error("API Invalid Data");
        
        renderOracleSections(data.choices[0].message.content);
        setSpriteFace('Normal'); setEmoji('🌟');
        updateGrowth(1);
        showSpriteBubble('Oracle revealed! Garden received +1 energy 🌱');
        hw('BREATHE:DONE');
    } catch (e) {
        body.innerHTML = `<p style="color:var(--g); text-align:center; padding:80px;">Void sync failed.<br><span style="font-size:12px; color:#666; letter-spacing:2px">Check API Key in Settings</span></p>`;
        setEmoji('😔');
        hw('BREATHE:DONE');
    }
}

function renderOracleSections(text) {
    const body = document.getElementById('oracle-body');
    body.innerHTML = `<div style="color:var(--g); text-align:center; font-size:12px; letter-spacing:15px; margin-bottom:60px">${category} · DESTINY TAPESTRY</div>`;
    const sections = text.split('---');
    const titles = ['DEEP READING', 'CORE INSIGHT', 'DAILY QUEST'];
    const icons = ['🔮', '⚡', '🌟'];
    sections.forEach((content, i) => {
        if (!content.trim()) return;
        body.innerHTML += `
            <div class="oracle-section">
                <div class="os-header">
                    <div class="os-icon">${icons[i]}</div>
                    <div class="os-title">${titles[i]}</div>
                    <div style="flex:1; height:1px; background:linear-gradient(to right, rgba(212,175,55,0.3), transparent)"></div>
                </div>
                <div class="os-content ${i===1?'quote':''}">${marked.parse(content.replace(/###.*?\n/, ''))}</div>
            </div>`;
    });
}
