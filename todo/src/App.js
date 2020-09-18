import React from 'react';
import 'App.css';
import 'antd/dist/antd.css';
// import Change from 'change'
// import JsxTest from 'student';
// import Fruit from 'fruit';

function Parents()
{
  const [num, setNum] = React.useState(50)
  const changeNumber = (number) => {
    setNum(number);
  }
  return (
    <>
      {num}
      <Child changeNumber={changeNumber} 
             color={"red"}
             number={10}
             student={{name:'홍길동', age:35, address:'인천'}}
      />
    </>
  )
}
function Child({changeNumber, color, number, student})
{
  // const x = {name:"홍길동", age:35};
  // const {name, age} = x;  
  console.log(number)
  console.log(color)
  console.log(student)
  const click = () => {
    changeNumber(10)
  }
  return(
    <>
    <button onClick={click}>클릭</button>
    </>
  )
}


function App() {
  return (
    <div>
      <Parents/>
    </div>
)
}
export default App;