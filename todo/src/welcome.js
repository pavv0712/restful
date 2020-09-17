import React from 'react';

function Welcome(){
    const [txt, setTxt] = React.useState('안녕하세요 환영합니다')

    return (
      <div>
        <div>{txt}</div>
      </div>
    );
    }
  
  export default Welcome;