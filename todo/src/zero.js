import React from 'react';

export default function Zero() {
    const[num, setNumber] = React.useState(
        [1,2,3,4,5,6,7,8,9]
        )
    const click = () => {
        setNumber([...num.slice(0,4), 0, 0, ...num.slice(6,9)])
    }

    return(
        <div>
            <div>{JSON.stringify(num)}</div>
            <button onClick = {click}>클릭</button>
        </div>
    )

}