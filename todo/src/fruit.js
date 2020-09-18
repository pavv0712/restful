import React from 'react';

function Fruit(){
    const [fruit, setFruit] = React.useState('')
    
    const change1 = () =>{
        setFruit('바나나')
    }
    const change2 = () =>{
        setFruit('사과')
    }
    const change3 = () =>{
        setFruit('딸기')
    }
    

    return(
        <div>
            <div>{fruit}</div>
            <button onClick={change1}>바나나</button>
            <button onClick={change2}>사과</button>
            <button onClick={change3}>딸기</button>
        </div>

    )

}
export default Fruit;