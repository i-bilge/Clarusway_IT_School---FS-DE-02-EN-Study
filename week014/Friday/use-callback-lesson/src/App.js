import './App.css';
import {useState} from 'react'
import List from './List';

function App() {

  const [number, setNumber] = useState(1)
  const [dark, setDark] = useState(false)

  const getItems = ()=>{
    return [number, number + 1, number + 2]
  }

  const theme = {
    backgroundColor: dark? 'black' : 'white',
    color: dark? 'white' : 'black'
  }

  return (
    <div style={theme}>
      <input type="number" value={number} onChange = {e=>setNumber(parseInt(e.target.value))} />
      <button onClick={()=>setDark(prevDark=>!prevDark)}>Toggle Theme</button>
      <List getItems={getItems} />
    </div>
  );
}

export default App;
