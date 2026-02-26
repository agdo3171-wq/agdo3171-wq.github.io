import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# كود سجل العمليات
logs_html = '''
    <div id="system-logs" style="margin-top:15px; background:rgba(0,20,0,0.9); border:1px solid #0f0; padding:8px; font-family:monospace; font-size:0.65rem; height:60px; overflow:hidden; direction:ltr; text-align:left;">
        <div id="log-container"></div>
    </div>
'''

# الأوامر البرمجية لتحريك السجلات
logs_script = '''
<script>
    const logContainer = document.getElementById('log-container');
    const logMessages = [
        "[OK] Connection established with Proxy #992",
        "[INFO] Encrypting Bitcoin transaction... 88%",
        "[SUCCESS] Account secured for Client_881",
        "[RUNNING] Vulnerability scan on server_alpha",
        "[OK] Windows 10 Pro license generated",
        "[INFO] Cleaning malware from remote device...",
        "[SUCCESS] Anti-extortion shield active"
    ];

    function addLog() {
        const msg = logMessages[Math.floor(Math.random() * logMessages.length)];
        const p = document.createElement('div');
        p.style.color = "#0f0";
        p.innerText = "> " + msg;
        logContainer.prepend(p);
        if (logContainer.children.length > 4) {
            logContainer.removeChild(logContainer.lastChild);
        }
    }
    setInterval(addLog, 3000);
</script>
'''

if 'id="system-logs"' not in content:
    # وضع السجلات قبل نهاية الـ main-frame
    updated = content.replace('</div>\n</div>\n\n<script>', logs_html + '</div>\n</div>\n\n<script>')
    # إضافة السكريبت قبل نهاية الـ body
    updated = updated.replace('</body>', logs_script + '</body>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated)
