with open('App.js', 'w') as f:
    f.write('''import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, FlatList, SafeAreaView } from 'react-native';

export default function App() {
  const [assetName, setAssetName] = useState('');
  const [value, setValue] = useState('');
  const [category, setCategory] = useState('Crypto');
  const [assets, setAssets] = useState([]);

  const addAsset = () => {
    if (assetName && value) {
      setAssets([...assets, { id: Date.now().toString(), name: assetName, value, category }]);
      setAssetName('');
      setValue('');
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>FinTrack</Text>
      <View style={styles.categoryContainer}>
        {['Crypto', 'Gold', 'Cash', 'Stocks', 'Other'].map((cat) => (
          <TouchableOpacity key={cat} style={[styles.catButton, category === cat && styles.activeCat]} onPress={() => setCategory(cat)}>
            <Text style={styles.catText}>{cat}</Text>
          </TouchableOpacity>
        ))}
      </View>
      <TextInput style={styles.input} placeholder="Asset Name" placeholderTextColor="#888" value={assetName} onChangeText={setAssetName} />
      <TextInput style={styles.input} placeholder="Value ($)" placeholderTextColor="#888" value={value} onChangeText={setValue} keyboardType="numeric" />
      <TouchableOpacity style={styles.addButton} onPress={addAsset}>
        <Text style={styles.addButtonText}>Add Asset</Text>
      </TouchableOpacity>
      <FlatList 
        data={assets}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.assetItem}>
            <Text style={styles.assetText}>{item.name} ({item.category})</Text>
            <Text style={styles.assetText}>${item.value}</Text>
          </View>
        )}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0f172a', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', color: '#fff', marginBottom: 20, textAlign: 'center' },
  categoryContainer: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 15 },
  catButton: { paddingVertical: 10, paddingHorizontal: 12, backgroundColor: '#1e293b', borderRadius: 8 },
  activeCat: { backgroundColor: '#3b82f6' },
  catText: { color: '#fff', fontSize: 12 },
  input: { height: 45, backgroundColor: '#1e293b', borderRadius: 8, paddingHorizontal: 15, color: '#fff', marginBottom: 10 },
  addButton: { height: 45, backgroundColor: '#3b82f6', borderRadius: 8, justifyContent: 'center', alignItems: 'center', marginBottom: 20 },
  addButtonText: { color: '#fff', fontWeight: 'bold' },
  assetItem: { flexDirection: 'row', justifyContent: 'space-between', padding: 15, backgroundColor: '#1e293b', borderRadius: 8, marginBottom: 10 },
  assetText: { color: '#fff', fontSize: 16 }
});''')
print("App.js reset complete.")
