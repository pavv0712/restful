import React from 'react';

export default function InputBox() {
    
    const[list, setList] = React.useState([]);
    const[text, setText] = React.useState('')

    const click = () => {
        setList([...list, text]);
        setText("");
    }
    const press = (e) =>{
        if(e.key === 'Enter'){
            click()
    }}
    const pressdelete = (index) => {
        setList([...list.slice(0, index),
                ...list.slice(idex + 1, list.length)]);

    }
    return (
        <>
            <input value = {text} onChange = {(e)=>setText(e.target.value)} onKeyPress={press}></input>
            <button onClick = {click}>추가</button>
            <div>{list}</div>
        </>
    )    
}

function pressdelete = (e) => {

}