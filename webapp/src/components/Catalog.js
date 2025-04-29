import React from 'react';
export default function Catalog() {
  return (
    <div className="p-4">
      <h2 className="text-lg font-semibold">Каталог</h2>
      <div className="grid grid-cols-2 gap-4 mt-4">
        <div className="bg-white rounded-xl shadow p-4">
          <h3 className="font-bold">Пример товара</h3>
          <p className="text-sm">Описание товара</p>
          <p className="text-green-600 mt-2">100 ₽</p>
        </div>
      </div>
    </div>
  );
}
