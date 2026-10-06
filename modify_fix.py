with open("build_full_website.py", "r", encoding="utf-8") as f:
    content = f.read()

old_switch = "for (let i = 1; i <= 5; i++) {{"
new_switch = "for (let i = 1; i <= 6; i++) {{"
content = content.replace(old_switch, new_switch)

with open("build_full_website.py", "w", encoding="utf-8") as f:
    f.write(content)
