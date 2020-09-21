import React from 'react';

function CountArray() {
    const[cnt,setCnt] = React.useState(0);
    
    console.log('실행')
    
    React.useEffect(() => {
        console.log('처음')
        return () => {
            console.log('삭제시')
        }
    }, [])

    React.useEffect(() => {
        console.log('cnt변경')

    },[cnt])


    const click = () => {
        setCnt(cnt + 1)
    } 
    return(
        <div>
            {cnt}
            <button onClick={click}>클릭</button>
        </div>
    )
}

export default CountArray;