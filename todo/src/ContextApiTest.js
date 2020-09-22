import React from 'react';


export default function ContextApiText() {


    const[cnt, setCnt] = React.useState(100); 

    return(
    <>
        <Child1 cnt = {cnt}/>
    </> 

    )
}
function Child1({cnt}){
    return(
    <div>
        <Child2 cnt={cnt}/>
    </div>
    )
    }
   
    function Child2({cnt}){
    return(
    <div>
    
        <Child3 cnt={cnt}/>
    </div>
    )
    }

    function Child3({cnt}){
        return(
        <div>
            {cnt}
        </div>
        )
        }