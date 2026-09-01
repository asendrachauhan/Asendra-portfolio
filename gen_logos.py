import os
OUT = "/home/claude/build/assets/tech"
CHIP_BG = "#f3f0e6"

def wrap(inner, bg=CHIP_BG):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="15" fill="{bg}"/>
{inner}
</svg>'''

def write(name, svg):
    with open(os.path.join(OUT, f"{name}.svg"), "w") as f:
        f.write(svg)
    print("wrote", name)

# React — atom: 3 rotated ellipse rings + core
react_inner = '''<g transform="translate(32,32)" fill="none" stroke="#149ECA" stroke-width="2.6">
<ellipse rx="21" ry="8.4"/>
<ellipse rx="21" ry="8.4" transform="rotate(60)"/>
<ellipse rx="21" ry="8.4" transform="rotate(120)"/>
</g>
<circle cx="32" cy="32" r="4.2" fill="#149ECA"/>'''
write("react", wrap(react_inner))

# Angular — shield with A
angular_inner = '''<path d="M32 8 L53 15.5 L49.5 44 L32 56 L14.5 44 L11 15.5 Z" fill="#DD0031"/>
<path d="M32 8 L53 15.5 L49.5 44 L32 56 Z" fill="#C3002F"/>
<path d="M32 16 L44 42 L39.6 42 L37.1 36 L26.8 36 L24.3 42 L20 42 Z M32 24.2 L28.4 32.4 L35.6 32.4 Z" fill="#fff"/>'''
write("angular", wrap(angular_inner))

# TypeScript — blue square, TS
ts_inner = '''<rect x="10" y="10" width="44" height="44" rx="7" fill="#3178C6"/>
<text x="32" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="20" font-weight="700" fill="#fff">TS</text>'''
write("typescript", wrap(ts_inner))

# JavaScript — yellow square, JS
js_inner = '''<rect x="10" y="10" width="44" height="44" rx="7" fill="#F7DF1E"/>
<text x="32" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="19" font-weight="700" fill="#111">JS</text>'''
write("javascript", wrap(js_inner))

# Node.js — green hexagon
node_inner = '''<path d="M32 9 L52 20.5 V43.5 L32 55 L12 43.5 V20.5 Z" fill="#3C873A"/>
<path d="M32 9 L52 20.5 V43.5 L32 55 Z" fill="#2E7D32" opacity=".55"/>
<text x="32" y="37.5" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="12.5" font-weight="700" fill="#fff">JS</text>'''
write("nodejs", wrap(node_inner))

# Express — dark monogram
express_inner = '''<rect x="10" y="10" width="44" height="44" rx="7" fill="#0a0d0d"/>
<text x="32" y="39" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="20" font-style="italic" font-weight="700" fill="#fff">ex</text>'''
write("express", wrap(express_inner))

# MongoDB — leaf
mongo_inner = '''<path d="M32 8 C42 16 45 28 38 42 C36 46 33.5 49 32 52 C30.5 49 28 46 26 42 C19 28 22 16 32 8 Z" fill="#47A248"/>
<path d="M32 8 C42 16 45 28 38 42 C36 46 33.5 49 32 52 Z" fill="#3F9142" opacity=".5"/>
<line x1="32" y1="30" x2="32" y2="54" stroke="#fff" stroke-width="1.6" opacity=".8"/>'''
write("mongodb", wrap(mongo_inner))

# Redis — red monogram
redis_inner = '''<rect x="10" y="10" width="44" height="44" rx="7" fill="#D82C20"/>
<text x="32" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="21" font-weight="800" fill="#fff">R</text>'''
write("redis", wrap(redis_inner))

# Git — branch diamond
git_inner = '''<g stroke="#F05033" stroke-width="2.6" fill="none">
<line x1="22" y1="42" x2="42" y2="22"/>
<line x1="32" y1="32" x2="42" y2="42"/>
</g>
<circle cx="22" cy="42" r="4.6" fill="#F05033"/>
<circle cx="42" cy="22" r="4.6" fill="#F05033"/>
<circle cx="42" cy="42" r="4.6" fill="#F05033"/>'''
write("git", wrap(git_inner))

# GitHub — simplified cat silhouette
github_inner = '''<path d="M32 10c-11 0-20 8.9-20 19.9 0 8.8 5.7 16.3 13.6 18.9 1 .2 1.4-.4 1.4-1v-3.6c-5.5 1.2-6.7-2.6-6.7-2.6-.9-2.3-2.2-2.9-2.2-2.9-1.8-1.2.1-1.2.1-1.2 2 .1 3 2 3 2 1.8 3 4.6 2.2 5.7 1.7.2-1.3.7-2.2 1.2-2.7-4.4-.5-9-2.2-9-9.7 0-2.1.8-3.9 2-5.3-.2-.5-.9-2.6.2-5.4 0 0 1.6-.5 5.4 2a18.6 18.6 0 0 1 9.8 0c3.7-2.5 5.4-2 5.4-2 1.1 2.8.4 4.9.2 5.4 1.2 1.4 2 3.2 2 5.3 0 7.5-4.6 9.2-9 9.7.7.6 1.4 1.9 1.4 3.8v5.6c0 .6.4 1.2 1.4 1a20 20 0 0 0 13.6-18.9C52 18.9 43 10 32 10Z" fill="#171515"/>'''
write("github", wrap(github_inner))

# Figma — layered rings
figma_inner = '''<circle cx="26" cy="20" r="7.5" fill="#0ACF83"/>
<circle cx="26" cy="35" r="7.5" fill="#A259FF"/>
<circle cx="38" cy="27.5" r="7.5" fill="#1ABCFE"/>
<path d="M18.5 43a7.5 7.5 0 1 1 15 0v7.5h-7.5a7.5 7.5 0 0 1-7.5-7.5Z" fill="#F24E1E"/>
<path d="M18.5 27.5a7.5 7.5 0 0 1 7.5-7.5h0v15h0a7.5 7.5 0 0 1-7.5-7.5Z" fill="#FF7262"/>'''
write("figma", wrap(figma_inner))

# Postman — orange circle, arrow
postman_inner = '''<circle cx="32" cy="32" r="22" fill="#FF6C37"/>
<path d="M22 38 L40 24 M40 24 L34 24 M40 24 L40 30" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'''
write("postman", wrap(postman_inner))

# AI / GenAI — abstract spark (kept custom since no fixed brand)
ai_inner = '''<path d="M32 12 L36 27 L51 32 L36 37 L32 52 L28 37 L13 32 L28 27 Z" fill="#e8501c"/>
<circle cx="46" cy="16" r="3.2" fill="#e8501c"/>'''
write("ai", wrap(ai_inner, bg="#0a0d0d"))
