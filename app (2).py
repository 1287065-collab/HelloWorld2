import html
import random

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Hello World", page_icon="✨", layout="centered")

st.title("✨ Hello World!")
st.write("Create an animated greeting. Customize the name, font, background, and effect.")

name = st.text_input("Enter your name:", value="World", max_chars=40)
fonts = {
    "Arial": "Arial, sans-serif",
    "Georgia": "Georgia, serif",
    "Courier New": "'Courier New', monospace",
    "Comic Sans MS": "'Comic Sans MS', cursive",
    "Times New Roman": "'Times New Roman', serif",
    "Trebuchet MS": "'Trebuchet MS', sans-serif",
    "Impact": "Impact, sans-serif",
}
font_name = st.selectbox("Choose a font:", list(fonts))
font_size = st.slider("Choose a font size:", 20, 100, 56, 2)

backgrounds = {
    "Soft Pink": "#ffe4ec",
    "Sky Blue": "#dff3ff",
    "Lavender": "#eee5ff",
    "Mint Green": "#dcfce7",
    "Sunny Yellow": "#fff6c7",
    "Dark Night": "#172033",
    "White": "#ffffff",
}
background_name = st.selectbox("Choose a background:", list(backgrounds))
effect = st.selectbox(
    "Choose an animated effect:",
    ["None", "Rain", "Snow", "Hail", "Wind Gust", "Confetti", "Tornado"],
)

display_name = name.strip() or "World"
safe_name = html.escape(display_name)
background = backgrounds[background_name]
font = fonts[font_name]
text_color = "#ffffff" if background_name == "Dark Night" else "#243047"
animation_id = f"hello-{random.randint(10000, 99999)}"

effect_css = {
    "None": "",
    "Rain": """
        .particle { width:2px; height:22px; background:#60a5fa; border-radius:5px;
                    animation: rainFall .8s linear infinite; }
        @keyframes rainFall { from {transform:translateY(-80px)}
                              to {transform:translateY(500px)} }
    """,
    "Snow": """
        .particle { width:10px; height:10px; background:white; border-radius:50%;
                    box-shadow:0 0 5px #94a3b8; animation:snowFall 5s linear infinite; }
        @keyframes snowFall { 0% {transform:translateY(-60px) translateX(0)}
            50% {transform:translateY(220px) translateX(35px)}
            100% {transform:translateY(500px) translateX(-20px)} }
    """,
    "Hail": """
        .particle { width:13px; height:13px; background:#bae6fd; border-radius:50%;
                    box-shadow:inset -2px -2px 3px #64748b;
                    animation:hailFall 1.2s linear infinite; }
        @keyframes hailFall { 0% {transform:translateY(-60px) translateX(0)}
            80% {transform:translateY(420px) translateX(35px)}
            100% {transform:translateY(500px) translateX(-10px)} }
    """,
    "Wind Gust": """
        .particle { width:65px; height:3px; background:#64748b; border-radius:5px;
                    animation:windMove 2s ease-in-out infinite; }
        @keyframes windMove { 0% {transform:translateX(-150px);opacity:0}
            30% {opacity:1} 100% {transform:translateX(700px);opacity:0} }
    """,
    "Confetti": """
        .particle { width:10px; height:16px; background:#f43f5e;
                    animation:confettiFall 3s linear infinite; }
        @keyframes confettiFall { 0% {transform:translateY(-60px) rotate(0deg)}
                                  100% {transform:translateY(500px) rotate(720deg)} }
    """,
    "Tornado": """
        .particle { width:8px; height:8px; background:#94a3b8; border-radius:50%;
                    animation:tornadoSpin 2s linear infinite; }
        @keyframes tornadoSpin { 0% {transform:rotate(0deg) translateX(10px)}
                                 100% {transform:rotate(360deg) translateX(10px)} }
    """,
}

particles = []
for _ in range(60):
    left = random.randint(0, 100)
    delay = random.uniform(0, 4)
    duration = random.uniform(1, 5)
    size = random.randint(4, 12)
    particles.append(
        f'<div class="particle" style="left:{left}%;top:-40px;'
        f'animation-delay:-{delay:.2f}s;animation-duration:{duration:.2f}s;'
        f'width:{size}px;height:{size}px"></div>'
    )

tornado_html = ""
if effect == "Tornado":
    tornado_html = '<div class="tornado"><div class="tornado-funnel"></div></div>'

animation_html = f"""
<div id="{animation_id}" class="scene">
  <div class="greeting">Hello, {safe_name}!</div>
  {''.join(particles)}
  {tornado_html}
</div>
<style>
.scene {{
  position:relative;width:100%;height:420px;overflow:hidden;display:flex;
  align-items:center;justify-content:center;background:{background};
  border-radius:20px;isolation:isolate;
}}
.greeting {{
  font-family:{font};font-size:{font_size}px;font-weight:bold;color:{text_color};
  text-align:center;z-index:2;position:relative;padding:20px;overflow-wrap:anywhere;
  animation:greetingPulse 3s ease-in-out infinite;
}}
@keyframes greetingPulse {{ 0%,100% {{transform:scale(1)}} 50% {{transform:scale(1.04)}} }}
.particle {{position:absolute;z-index:3;pointer-events:none;}}
{effect_css[effect]}
.tornado {{
  position:absolute;bottom:-30px;left:50%;width:220px;height:350px;
  transform:translateX(-50%);z-index:1;animation:tornadoSway 4s ease-in-out infinite;
}}
.tornado-funnel {{
  position:absolute;inset:0;
  background:repeating-linear-gradient(0deg,#94a3b8,#64748b 12px,#cbd5e1 24px);
  clip-path:polygon(45% 0%,55% 0%,58% 25%,70% 50%,100% 100%,0% 100%,30% 50%,42% 25%);
  opacity:.7;animation:funnelSpin 1.5s linear infinite;
}}
@keyframes funnelSpin {{from {{background-position:0 0}} to {{background-position:0 100px}}}}
@keyframes tornadoSway {{
  0%,100% {{transform:translateX(-50%) rotate(-4deg)}}
  50% {{transform:translateX(-50%) rotate(4deg)}}
}}
</style>
"""

components.html(animation_html, height=440, scrolling=False)
st.caption("The animation loops continuously. Select None to turn off the effect.")
