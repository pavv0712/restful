import React, { useState } from 'react';

function Act() {
    const [txt, setTxt] = useState('리액트로 만든 웹사이트입니다.')
    
    return (
    <div>
        <div>{txt}</div>
    </div>
    )
}

export default Act;