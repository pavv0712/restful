import React from "react";

export default function Box(){

    const[txt, setTxt] = React.useState(0)

    const style = {
        width:'100px',
        height:'100px',
        fontSize:'20px',
        backgroundColor:'yellow',
        textAlign:'center',
        lineHeight:'100px'
    }
    const over = () => {
        setTxt(1)
    }
    
    const down = () => {
        setTxt(0)
    }

    return(
        <>
            <div style={style}
                onMouseOver={over}
                onMouseOut={down}
                >{txt}</div>
        
        </>
    )
}
