import React from 'react';
import './Button.css';

const Button = (props) => {
  return (

    <button className='Button' onClick={ props.onClick}>
      Generate
    </button>
    )
}

export default Button