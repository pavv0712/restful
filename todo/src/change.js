import React from 'react';

function Change() {

  const [cl, setCl] = React.useState(true)
 
  
  const click = (e) =>{
      if (cl == true) {
          setCl(false);
      }
      else {
          setCl(true);
      }
     
    }
  return (
      <div>
        <div>{cl ? <div>True</div>: <div>False</div>}</div>
        <button onClick={click}>클릭</button>
      </div>
  );
}

export default Change;