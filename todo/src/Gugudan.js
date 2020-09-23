import React from 'react';

export default function Gugudan() {
    const [num,setNum] = React.useState('')
    const nums = [1,2,3,4,5,6,7,8,9]
    const onChange = (e) => {
        setNum(e.target.value)
    }

    return(
        <>  
            <input value = {num} onChange = {onChange}></input>
            {
            nums.map((v, i) => {
                return <div key={i}>{num}*{v}={num * v}</div>
            })
        }
                    
        </>
    )
}