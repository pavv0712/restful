import React from 'react'


export default function FormTest() {
    const[num1, setNum1] = React.useState()
    const[num2, setNum2] = React.useState()

    return (
        <>
            <input value={num1} onChange={e => setNum1(e.target.value)}/>
            '+'
            <input value={num2} onChange={e => setNum2(e.target.value)}/>
            '='
            <input value={Number(num1) + parseInt(num2)}/>
        </>
    )
}