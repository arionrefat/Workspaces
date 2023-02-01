import * as React from 'react';
import './style.css';
import TextGenerate from './TextGenerate';

export default function App() {
  return (
    <div>
      <h1 style={{ textAlign: 'center' }}>
        Algochurn: Generate Text On The Go
      </h1>
      <TextGenerate />
    </div>
  );
}
