import React from 'react';

export default function Gugudan({x}) {

    const num = [1,2,3,4,5,6,7,8,9]

    return(
        <>  
            {
            num.map((v, i) => {
                return <div key={i}>{x}*{v}={x * v}</div>
            })
        }
                    
        </>
    )
}