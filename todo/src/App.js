import React from 'react';
import 'App.css';
import 'antd/dist/antd.css';
// import FormTest from 'Formtest';
// import Add from 'Add';
// import Gugudan from 'Gugudan';
// import InputBox from 'InputBox';
// import ContextApiText from 'ContextApiTest';
// import AxiosTest from 'AxiosTest';
// import Gugudan from 'Gugudan';
// import CssTest1 from 'CssTest1';
// import RouterTest from 'RouterTest';
// import Box from 'CssTest2';
import InputBox from 'InputBox';



// function Parents()
// {
//   const [num, setNum] = React.useState(50)
//   const changeNumber = (number) => {
//     setNum(number);
//   }
//   return (
//     <>
//       {num}
//       <Child changeNumber={changeNumber} 
//              color={"red"}
//              number={10}
//              student={{name:'홍길동', age:35, address:'인천'}}
//       />
//     </>
//   )
// }
// function Child({changeNumber, color, number, student})
// {
//   // const x = {name:"홍길동", age:35};
//   // const {name, age} = x;  
//   console.log(number)
//   console.log(color)
//   console.log(student)
//   const click = () => {
//     changeNumber(10)
//   }
//   return(
//     <>
//     <button onClick={click}>클릭</button>
//     </>
//   )
// }


function App() {
  return (
    <div>
      <InputBox/>
    </div>
)
}
export default App;