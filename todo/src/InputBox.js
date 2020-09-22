import React from 'react';

export default function InputBox() {
    
    todos = ['저녁먹기', '점심먹기', '공부하기']
    
    const[num, setNum] = React.useState()

    const onChange = (e) => {
        setNum(e.target.value)
    }

    const onClick = () => {
        

    }


    return (
        <>
            <input value = {num} onChange = {onChange}></input>
            <button onClick = {onClick}>추가</button>
            <div>{todo}</div>
        </>
    )

    
}