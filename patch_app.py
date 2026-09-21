import re

with open('App.js', 'r') as f:
    content = f.read()

# 1. Fix addAsset function
old_add_asset = """    const newAsset = {
      id: Date.now().toString(),
      name: trimmedName,
      amount: numericAmount, // Stored consistently in USD
      icon: getCategoryIcon(item.category || 'Other')
    };"""

new_add_asset = """    const newAsset = {
      id: Date.now().toString(),
      name: trimmedName,
      amount: numericAmount,
      category: category,
      icon: getCategoryIcon(category)
    };"""

content = content.replace(old_add_asset, new_add_asset)

# 2. Inject CategorySelector into Input Form
# We look for the first TextInput to inject the selector before it
insertion_point = '<TextInput'
if insertion_point in content and '<CategorySelector' not in content:
    selector_injection = '<CategorySelector selected={category} onSelect={setCategory} />\n          <TextInput'
    content = content.replace(insertion_point, selector_injection, 1)

with open('App.js', 'w') as f:
    f.write(content)

print("App.js patched successfully!")
