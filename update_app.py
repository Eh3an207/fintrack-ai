import os
import shutil

file_path = 'App.js'
backup_path = 'App.js.bak'

# 1. Backup
shutil.copyfile(file_path, backup_path)
print("Backup created as App.js.bak")

with open(file_path, 'r') as f:
    content = f.read()

# 2. Add State (Assuming useState is imported)
if 'const [category, setCategory]' not in content:
    content = content.replace('const [assets, setAssets]', 'const [category, setCategory] = useState("Other");\n  const [assets, setAssets]')

# 3. Add Component Definition (Before return)
selector_component = """
const CategorySelector = ({ selected, onSelect }) => {
  const categories = [
    { name: 'Crypto', icon: '₿' },
    { name: 'Gold', icon: '🪙' },
    { name: 'Cash', icon: '💵' },
    { name: 'Stocks', icon: '📈' },
    { name: 'Other', icon: '📦' }
  ];
  return (
    <View style={styles.categoryContainer}>
      {categories.map((cat) => (
        <TouchableOpacity key={cat.name} style={[styles.categoryChip, selected === cat.name && styles.categoryChipActive]} onPress={() => onSelect(cat.name)}>
          <Text style={[styles.categoryLabel, selected === cat.name && styles.categoryLabelActive]}>{cat.icon} {cat.name}</Text>
        </TouchableOpacity>
      ))}
    </View>
  );
};
"""

if 'const CategorySelector' not in content:
    # Insert before the first function definition or return
    content = content.replace('const addAsset', selector_component + '\nconst addAsset')

# 4. Update addAsset (Ensure category is added)
if 'category: category' not in content:
    content = content.replace('value: parseFloat(assetValue)', 'value: parseFloat(assetValue), category')

# 5. Inject into JSX
if '<CategorySelector' not in content:
    content = content.replace('<TextInput', '<CategorySelector selected={category} onSelect={setCategory} />\n        <TextInput')

with open(file_path, 'w') as f:
    f.write(content)
print("App.js updated successfully!")
