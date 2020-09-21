import React from 'react';

function Hong() {
    const [student, setStudent] = React.useState(
        {name:'홍길동', math: 80, science:30, english:60}
        )
    const click = () => {
        setStudent({
            ...student, 
            math:0,
            science:0,
            english:0
        })
    }


    return(
        <div>
            <div>{JSON.stringify(student)}</div>
            <button onClick = {click}>클릭</button>
        </div>
    )   
}


export default Hong;