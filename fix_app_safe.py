import re

with open('App.js', 'r') as f:
    content = f.read()

# 1. Add Category Icons Logic
icons = """
const getCategoryIcon = (cat) => {
  const mapping = { 'Crypto': '₿', 'Gold': '🪙', 'Cash': '💵', 'Stocks': '📈', 'Other': '📦' };
  return mapping[cat] || '📦';
};
"""

# 2. Add Category Selector Component
selector = """
const CategorySelector = ({ selected, onSelect }) => {
  const categories = ['Crypto', 'Gold', 'Cash', 'Stocks', 'Other'];
  return (
    <View style={{ flexDirection: 'row', justifyContent: 'space-around', marginVertical: 10 }}>
      {categories.map((cat) => (
        <TouchableOpacity key={cat} onPress={() => onSelect(cat)} style={{ padding: 5, backgroundColor: selected === cat ? '#3b82f6' : '#1f2937', borderRadius: 8 }}>
          <Text style={{ color: 'white' }}>{cat}</Text>
        </TouchableOpacity>
      ))}
    </View>
  );
};
"""

# Apply
content = content.replace('const [assets, setAssets]', icons + '\n' + selector + '\n  const [category, setCategory] = useState("Other");\n  const [assets, setAssets]')

# 3. Update addAsset (Find the function and inject category)
# This looks for the addAsset function body
content = re.sub(r'(const addAsset.*?\n.*?\{)', r'\1\n    const newAsset = { ...asset, category };', content) 
# (نکته: در اینجا فرض بر این است که منطق addAsset شما باید category را به آبجکت دارایی اضافه کند)

# 4. FIX THE CRASH: Update render logic to be safe
# This regex looks for where icons are rendered in the list and replaces '💰' with dynamic icon
# It uses (item.category || 'Other') to prevent crash on old data
content = content.replace("'💰'", "getCategoryIcon(item.category || 'Other')")

with open('App.js', 'w') as f:
    f.write(content)
print("App.js fixed safely!")
