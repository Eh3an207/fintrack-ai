import re

with open("App.js", "r", encoding="utf-8") as f:
    code = f.read()

# 1. تعریف لیست دسته‌بندی‌ها و آیکون‌ها
cat_defs = """
const CATEGORIES = [
  { id: 'crypto', label: 'Crypto', icon: '₿' },
  { id: 'gold', label: 'Gold', icon: '🪙' },
  { id: 'cash', label: 'Cash', icon: '💵' },
  { id: 'stocks', label: 'Stocks', icon: '📈' },
  { id: 'other', label: 'Other', icon: '📦' },
];

const getCategoryIcon = (catId) => {
  const found = CATEGORIES.find(c => c.id === catId);
  return found ? found.icon : '💰';
};
"""

if "const CATEGORIES =" not in code:
    code = cat_defs + "\n" + code

# 2. اضافه کردن state انتخاب دسته
if "const [selectedCategory, setSelectedCategory]" not in code:
    code = re.sub(
        r"(const \[assetValue,\s*setAssetValue\]\s*=\s*useState\([^)]*\);)",
        r"\1\n  const [selectedCategory, setSelectedCategory] = useState('crypto');",
        code
    )

# 3. افزودن فیلد category به دارایی جدید در تابع addAsset
code = re.sub(
    r"({\s*id:\s*Date\.now\(\)\..

بیایید با رعایت تمام اصول (بکاپ، تزریق تمیز و اعتبارسنجی سینتکس) کد دسته‌بندی‌ها را به صورت کامل روی `App.js` اعمال کنیم.

---

### گام ۱: ساخت بکاپ و پچ کردن مستقیم `App.js`

دستورات زیر را در ترموکس کپی و اجرا کنید:
```bash
cd ~/fin-asset-tracker
mkdir -p backups
cp App.js backups/App.js.bak_$(date +%Y%m%d_%H%M%S)

cat << 'EOF' > patch_category_full.py
import re

with open("App.js", "r", encoding="utf-8") as f:
code = f.read()

# 1. تعریف لیست دسته‌بندی‌ها و آیکون‌ها
cat_defs = """
const CATEGORIES = [
  { id: 'crypto', label: 'Crypto', icon: '₿' },
  { id: 'gold', label: 'Gold', icon: '🪙' },
  { id: 'cash', label: 'Cash', icon: '💵' },
  { id: 'stocks', label: 'Stocks', icon: '📈' },
  { id: 'other', label: 'Other', icon: '📦' },
];

const getCategoryIcon = (catId) => {
  const found = CATEGORIES.find(c => c.id === catId);
  return found ? found.icon : '💰';
};
"""

if "const CATEGORIES =" not in code:
code = cat_defs + "\n" + code

# 2. اضافه کردن state انتخاب دسته
if "const [selectedCategory, setSelectedCategory]" not in code:
code = re.sub(
r"(const \[assetValue,\s*setAssetValue\]\s*=\s*useState\([^)]*\);)",
r"\1\n  const [selectedCategory, setSelectedCategory] = useState('crypto');",
code
)

# 3. افزودن فیلد category به دارایی جدید در تابع addAsset
code = re.sub(
r"({\s*id:\s*Date\.now\(\)\.toString\(\),\s*name:\s*assetName,\s*value:\s*parsedValue)([\s,}])",
r"\1, category: selectedCategory\2",
code
)

# 4    marginBottom: 2,
  },
  catChipText: {
color: '#94A3B8',
fontSize: 10,
fontWeight: '600',
  },
  catChipTextActive: {
color: '#FFFFFF',
  },
"""

if "catContainer:" not in code:
code = re.sub(
r"(const styles = StyleSheet\.create\(\{)",
r"\1" + extra_styles,
code
)

with open("App.js", "w", encoding="utf-8") as f:
f.write(code)

print("SUCCESS: Category patching applied successfully!")
