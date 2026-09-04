import os
OUT = "/home/claude/build/assets/tech-mini"

def write(name, svg):
    with open(os.path.join(OUT, f"{name}.svg"), "w") as f:
        f.write(svg)
    print("wrote", name)

# All viewBox 0 0 20 20, transparent bg, small inline glyphs for skill-chip pills

write("html5", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<path d="M3 2h14l-1.3 14.6L10 18l-5.7-1.4L3 2Z" fill="#E34F26"/>
<path d="M10 3.3v13.3l4.6-1.3 1-11.8Z" fill="#EF6228" opacity=".001"/>
<path d="M10 3.3H4.3l.35 3.9H10v-3.9Z" fill="#fff" opacity=".85"/>
<path d="M10 10.9H6.9l.25 2.7L10 14.5v-3.6Z" fill="#fff" opacity=".85"/>
</svg>''')

write("css3", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<path d="M3 2h14l-1.3 14.6L10 18l-5.7-1.4L3 2Z" fill="#1572B6"/>
<path d="M10 3.3H4.3l.35 3.9H10v-3.9Z" fill="#fff" opacity=".85"/>
<path d="M10 10.9H6.9l.25 2.7L10 14.5v-3.6Z" fill="#fff" opacity=".85"/>
</svg>''')

write("jwt", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<rect x="1" y="4" width="18" height="12" rx="3" fill="#0a0d0d"/>
<text x="10" y="13" text-anchor="middle" font-family="Arial,sans-serif" font-size="6.5" font-weight="800" fill="#FB015B">JWT</text>
</svg>''')

write("oauth", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<rect x="4" y="9" width="12" height="9" rx="2" fill="#4a4a4a"/>
<path d="M6.5 9V6.5a3.5 3.5 0 0 1 7 0V9" fill="none" stroke="#4a4a4a" stroke-width="1.8"/>
<circle cx="10" cy="13" r="1.6" fill="#fff"/>
</svg>''')

write("redux", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<g fill="none" stroke="#764ABC" stroke-width="1.7">
<path d="M13.5 8c1.6 1 2 2.7.9 4"/>
<path d="M7.8 4.3c-1.8.3-2.9 1.8-2.6 3.4"/>
<path d="M9 15.6c-1.7-.6-2.5-2.2-1.9-3.8"/>
</g>
<circle cx="14.7" cy="12.5" r="1.5" fill="#764ABC"/>
<circle cx="5.6" cy="6.6" r="1.5" fill="#764ABC"/>
<circle cx="10.3" cy="16" r="1.5" fill="#764ABC"/>
<circle cx="10" cy="9.5" r="2.4" fill="#764ABC"/>
</svg>''')

write("tailwind", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<path d="M6 8.5c.6-2.2 2-3.3 4-3.3 2.7 0 3 2 4.4 2.3-.6 2.2-2 3.3-4 3.3-2.7 0-3-2-4.4-2.3Z" fill="#38BDF8"/>
<path d="M2 12.8c.6-2.2 2-3.3 4-3.3 2.7 0 3 2 4.4 2.3-.6 2.2-2 3.3-4 3.3-2.7 0-3-2-4.4-2.3Z" fill="#38BDF8"/>
</svg>''')

write("bootstrap", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<rect x="2" y="2" width="16" height="16" rx="4" fill="#7952B3"/>
<text x="10" y="14.5" text-anchor="middle" font-family="Georgia,serif" font-size="11" font-weight="700" fill="#fff">B</text>
</svg>''')

write("vscode", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<path d="M14 1.5 6.5 8 3 5.3 1.3 6.2 5.3 10l-4 3.8 1.7.9L6.5 12l7.5 6.5 4-2V3.5Zm0 4.3v8.4L8.6 10Z" fill="#007ACC"/>
</svg>''')

write("bitbucket", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<path d="M2.3 3.5h15.4a.8.8 0 0 1 .8.9l-2.1 12.6a1 1 0 0 1-1 .8H4.6a1 1 0 0 1-1-.8L1.5 4.4a.8.8 0 0 1 .8-.9Z" fill="#2684FF"/>
<path d="M12.6 12.3H7.4l-1-6h7.2Z" fill="#fff"/>
</svg>''')

write("reactrouter", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<circle cx="6" cy="15" r="1.8" fill="#CA4245"/>
<circle cx="15" cy="6" r="1.8" fill="#CA4245"/>
<path d="M6 15c0-6 3-9 9-9" fill="none" stroke="#CA4245" stroke-width="1.8" stroke-linecap="round"/>
<circle cx="6" cy="4.5" r="1.4" fill="#CA4245" opacity=".55"/>
</svg>''')

write("testinglibrary", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<rect x="2" y="4" width="16" height="12" rx="3" fill="#E33332"/>
<text x="10" y="13.2" text-anchor="middle" font-family="Arial,sans-serif" font-size="6.2" font-weight="800" fill="#fff">RTL</text>
</svg>''')

write("mocha", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<path d="M4 8h10.5a2.5 2.5 0 0 1 0 5H14v.5A3.5 3.5 0 0 1 10.5 17h-3A3.5 3.5 0 0 1 4 13.5Z" fill="#8D6748"/>
<path d="M14.5 9.3a1.4 1.4 0 0 1 0 2.7" fill="none" stroke="#8D6748" stroke-width="1.3"/>
<path d="M7 4.3c-.6.7-.6 1.3 0 2M10 4.3c-.6.7-.6 1.3 0 2" stroke="#8D6748" stroke-width="1.2" fill="none" stroke-linecap="round"/>
</svg>''')

write("mongoose", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
<rect x="2" y="2" width="16" height="16" rx="4" fill="#880000"/>
<text x="10" y="14" text-anchor="middle" font-family="Georgia,serif" font-size="10.5" font-weight="700" fill="#fff">M</text>
</svg>''')
