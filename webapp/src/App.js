import React from 'react';
import Catalog from './components/Catalog';

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-indigo-600 text-white p-4 text-center text-xl font-bold">
        LavanderShop
      </header>
      <main className="p-4">
        <Catalog />
      </main>
    </div>
  );
}
export default App;