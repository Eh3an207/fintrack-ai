import re

with open('App.js', 'r') as f:
    content = f.read()

# Increase the padding/margin or width of the category buttons style
# Assuming CategorySelector uses a style object like 'categoryButton'
new_style = "categoryButton: { paddingHorizontal: 12, paddingVertical: 8, margin: 2,"
content = re.sub(r'categoryButton: \{.*\}', new_style, content)

with open('App.js', 'w') as f:
    f.write(content)

print("UI Fixed: Padding updated.")
